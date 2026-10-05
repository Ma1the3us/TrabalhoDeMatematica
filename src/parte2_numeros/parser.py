"""
Parser de números em múltiplos formatos para conjuntos numéricos.
Identifica inteiros, frações, decimais finitos, dízimas periódicas e raízes.
"""
from dataclasses import dataclass
import math
import re
from typing import Optional
from src.parte2_numeros.generator_fraction import (
    fracao_decimal_exato,
    fracao_geratriz_dizima,
    simplificar_fracao,
)


@dataclass
class ParsedNumber:
    raw_input: str
    kind: str  # 'inteiro', 'fracao', 'decimal_exato', 'dizima_periodica', 'raiz'
    numerador: Optional[int] = None
    denominador: Optional[int] = None
    numerador_bruto: Optional[int] = None
    denominador_bruto: Optional[int] = None
    parte_inteira: Optional[int] = None
    antiperiodo: Optional[str] = None
    periodo: Optional[str] = None
    radicando: Optional[int] = None
    raiz_exata: Optional[bool] = None
    valor_raiz: Optional[float] = None
    valor_float: Optional[float] = None
    observacao_especial: str = ""


def parse_numero(entrada: str) -> ParsedNumber:
    """
    Analisa a string de entrada e extrai todas as propriedades matemáticas.
    """
    texto = entrada.strip()
    
    # 1. Raiz quadrada (ex: V9, v9, V2, v2, sqrt(9), raiz(9), √9)
    raiz_match = re.match(r"^(?:[Vv]|sqrt|raiz|√)\s*\(?(\d+)\)?$", texto, re.IGNORECASE)
    if raiz_match:
        radicando = int(raiz_match.group(1))
        raiz_float = math.isqrt(radicando)
        eh_perfeita = (raiz_float * raiz_float == radicando)
        val_real = math.sqrt(radicando)
        
        if eh_perfeita:
            return ParsedNumber(
                raw_input=texto,
                kind="raiz",
                radicando=radicando,
                raiz_exata=True,
                valor_raiz=float(raiz_float),
                valor_float=float(raiz_float),
                numerador=raiz_float,
                denominador=1,
                parte_inteira=raiz_float,
                observacao_especial=f"A raiz é exata e vale {raiz_float}."
            )
        else:
            return ParsedNumber(
                raw_input=texto,
                kind="raiz",
                radicando=radicando,
                raiz_exata=False,
                valor_raiz=val_real,
                valor_float=val_real,
                observacao_especial=f"Raiz não exata (√{radicando} ≈ {val_real:.6f}), portanto irracional."
            )

    # 2. Dízima periódica: notação com parênteses, ex: '1,2(5)', '0,(3)', '2,(7)', '0,(9)'
    dizima_match = re.match(r"^([+-]?\d+)[,\.](\d*)\((\d+)\)$", texto)
    if dizima_match:
        str_inteira = dizima_match.group(1)
        antiperiodo = dizima_match.group(2)
        periodo = dizima_match.group(3)
        negativo = str_inteira.startswith("-")
        p_int = abs(int(str_inteira))
        
        num_b, den_b, num_s, den_s = fracao_geratriz_dizima(
            p_int, antiperiodo, periodo, negativo=negativo
        )
        
        # Caso especial 0,(9) onde a fração resulta em 1
        obs = f"Dízima periódica (parte não periódica: {antiperiodo or 'nenhuma'}; período: {periodo})"
        if periodo == "9":
            obs += f". Caso curioso: a geratriz é {num_b}/{den_b} = {num_s}/{den_s} = {num_s}."
        
        val_float = num_s / den_s
        return ParsedNumber(
            raw_input=texto,
            kind="dizima_periodica",
            numerador=num_s,
            denominador=den_s,
            numerador_bruto=num_b,
            denominador_bruto=den_b,
            parte_inteira=p_int if not negativo else -p_int,
            antiperiodo=antiperiodo,
            periodo=periodo,
            valor_float=val_float,
            observacao_especial=obs
        )

    # 3. Fração no formato a/b (ex: 3/4, -5/2, 6/3)
    frac_match = re.match(r"^([+-]?\d+)\s*/\s*([+-]?\d+)$", texto)
    if frac_match:
        num = int(frac_match.group(1))
        den = int(frac_match.group(2))
        num_s, den_s = simplificar_fracao(num, den)
        val_float = num_s / den_s
        
        obs = f"Fração irredutível: {num_s}/{den_s}"
        if den_s == 1:
            obs += f" que simplifica para o número inteiro {num_s}."
        else:
            obs += f", equivalente ao decimal {val_float}."
            
        return ParsedNumber(
            raw_input=texto,
            kind="fracao",
            numerador=num_s,
            denominador=den_s,
            valor_float=val_float,
            observacao_especial=obs
        )

    # 4. Decimal exato com vírgula ou ponto (ex: 0.75, 0,75, -2.5, -2,5)
    dec_match = re.match(r"^([+-]?\d+)[,\.](\d+)$", texto)
    if dec_match:
        str_int = dec_match.group(1)
        str_dec = dec_match.group(2)
        negativo = str_int.startswith("-")
        p_int = abs(int(str_int))
        
        num_s, den_s = fracao_decimal_exato(p_int, str_dec, negativo=negativo)
        val_float = float(texto.replace(",", "."))
        
        return ParsedNumber(
            raw_input=texto,
            kind="decimal_exato",
            numerador=num_s,
            denominador=den_s,
            parte_inteira=p_int if not negativo else -p_int,
            valor_float=val_float,
            observacao_especial=f"Decimal exato equivalente à fração irredutível {num_s}/{den_s}."
        )

    # 5. Inteiro puro (ex: 7, -3, 0)
    int_match = re.match(r"^([+-]?\d+)$", texto)
    if int_match:
        val_int = int(int_match.group(1))
        return ParsedNumber(
            raw_input=texto,
            kind="inteiro",
            numerador=val_int,
            denominador=1,
            parte_inteira=val_int,
            valor_float=float(val_int),
            observacao_especial="Número inteiro."
        )

    raise ValueError(f"Formato numérico não reconhecido: '{entrada}'. "
                     f"Formatos válidos: inteiros (ex: 7, -3), frações (ex: 3/4), "
                     f"decimais (ex: 0.75 ou 0,75), dízimas (ex: 1,2(5), 0,(3)), raízes (ex: V9, V2).")
