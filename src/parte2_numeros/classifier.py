"""
Classificador de números nos conjuntos numéricos:
N (Naturais), Z (Inteiros), Q (Racionais), I (Irracionais) e R (Reais).
Gera justificativas matemáticas formais para cada classificação.
"""
from dataclasses import dataclass
from typing import List
from src.parte2_numeros.parser import ParsedNumber, parse_numero


@dataclass
class ClassificationResult:
    parsed: ParsedNumber
    pertence: List[str]
    nao_pertence: List[str]
    justificativas: List[str]
    fracao_geratriz: str


class NumberClassifier:
    """
    Classifica números e fornece justificativas completas com base na teoria matemática.
    Convenção adotada: O conjunto N inclui o zero: N = {0, 1, 2, 3, ...}.
    """

    @classmethod
    def classificar(cls, entrada_ou_parsed) -> ClassificationResult:
        if isinstance(entrada_ou_parsed, str):
            parsed = parse_numero(entrada_ou_parsed)
        else:
            parsed = entrada_ou_parsed

        pertence: List[str] = []
        nao_pertence: List[str] = []
        justificativas: List[str] = []

        # Caso 1: Raiz irracional (não exata)
        if parsed.kind == "raiz" and not parsed.raiz_exata:
            pertence = ["I", "R"]
            nao_pertence = ["N", "Z", "Q"]
            justificativas = [
                f"Raiz quadrada de {parsed.radicando} não é um quadrado perfeito.",
                "Não pode ser representado pela razão p/q de dois números inteiros.",
                "Possui infinitas casas decimais não periódicas.",
                "Logo, pertence ao conjunto dos Irracionais (I) e dos Reais (R).",
                "Não pertence a N, Z nem Q pois Q e I são conjuntos disjuntos (Q ∩ I = Ø)."
            ]
            fracao_str = "Não possui fração geratriz (número irracional)"
            return ClassificationResult(
                parsed=parsed,
                pertence=pertence,
                nao_pertence=nao_pertence,
                justificativas=justificativas,
                fracao_geratriz=fracao_str
            )

        # Caso 2: Número Racional (inteiros, frações, decimais exatos, dízimas e raízes exatas)
        num = parsed.numerador
        den = parsed.denominador

        if den == 1:
            fracao_str = f"{num}/1"
            if parsed.kind == "dizima_periodica" and parsed.periodo == "9":
                fracao_str = f"{parsed.numerador_bruto}/{parsed.denominador_bruto} = {num}/1 = {num}"
            elif parsed.kind == "fracao":
                fracao_str = f"{parsed.raw_input} = {num}"
        else:
            if parsed.numerador_bruto and parsed.denominador_bruto:
                fracao_str = f"{parsed.numerador_bruto}/{parsed.denominador_bruto} = {num}/{den}"
            else:
                fracao_str = f"{num}/{den}"

        # Teste de conjunto N, Z, Q, I, R
        if den == 1:
            # É inteiro
            if num >= 0:
                # Natural e inteiro não negativo
                pertence = ["N", "Z", "Q", "R"]
                nao_pertence = ["I"]
                justificativas.append(f"É inteiro e maior ou igual a zero (num = {num}), logo pertence a N.")
                justificativas.append(f"Pertence a Z pois todo número natural é também número inteiro (N ⊂ Z).")
                justificativas.append(f"Pertence a Q pois pode ser expresso como a fração {num}/1 (Z ⊂ Q).")
                justificativas.append("Pertence a R pois todo número racional é real (Q ⊂ R).")
                justificativas.append("Não pertence a I pois Q e I são mutuamente exclusivos.")
            else:
                # Inteiro negativo
                pertence = ["Z", "Q", "R"]
                nao_pertence = ["N", "I"]
                justificativas.append(f"Não pertence a N porque é estritamente negativo ({num} < 0).")
                justificativas.append(f"Pertence a Z pois é um número inteiro ({num}).")
                justificativas.append(f"Pertence a Q pois pode ser representado como a fração {num}/1.")
                justificativas.append("Pertence a R pois é um número racional (Q ⊂ R).")
                justificativas.append("Não pertence a I por ser racional.")
        else:
            # Fração estrita (não inteira)
            pertence = ["Q", "R"]
            nao_pertence = ["N", "Z", "I"]
            justificativas.append(f"Não pertence a N nem a Z pois possui parte fracionária não inteira ({num}/{den} = {parsed.valor_float}).")
            justificativas.append(f"Pertence a Q pois é a razão exata entre os inteiros {num} e {den} (denominador ≠ 0).")
            justificativas.append("Pertence a R pois os reais englobam todos os números racionais (Q ⊂ R).")
            justificativas.append("Não pertence a I pois todo número com fração geratriz é racional.")

        return ClassificationResult(
            parsed=parsed,
            pertence=pertence,
            nao_pertence=nao_pertence,
            justificativas=justificativas,
            fracao_geratriz=fracao_str
        )
