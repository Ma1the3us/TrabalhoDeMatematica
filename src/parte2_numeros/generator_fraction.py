"""
Cálculo de frações geratrizes para decimais exatos e dízimas periódicas.
Implementação manual dos algoritmos aritméticos e simplificação por MDC.
"""
from typing import Tuple


def mdc(a: int, b: int) -> int:
    """
    Calcula o Máximo Divisor Comum (MDC) usando o algoritmo de Euclides.
    """
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def simplificar_fracao(numerador: int, denominador: int) -> Tuple[int, int]:
    """
    Simplifica uma fração pelo MDC de forma irredutível.
    Garante que o sinal negativo fique no numerador.
    """
    if denominador == 0:
        raise ZeroDivisionError("Denominador não pode ser zero.")
        
    if denominador < 0:
        numerador = -numerador
        denominador = -denominador
        
    divisor = mdc(numerador, denominador)
    return numerador // divisor, denominador // divisor


def fracao_decimal_exato(parte_inteira: int, parte_decimal: str, negativo: bool = False) -> Tuple[int, int]:
    """
    Converte um decimal finito para fração geratriz irredutível.
    Exemplo: 0.75 -> 75/100 -> 3/4
             -2.5 -> -25/10 -> -5/2
    """
    casas = len(parte_decimal)
    denominador = 10 ** casas
    numerador = abs(parte_inteira) * denominador + int(parte_decimal if parte_decimal else "0")
    if negativo:
        numerador = -numerador
    return simplificar_fracao(numerador, denominador)


def fracao_geratriz_dizima(
    parte_inteira: int,
    antiperiodo: str,
    periodo: str,
    negativo: bool = False
) -> Tuple[int, int, int, int]:
    """
    Calcula a fração geratriz de uma dízima periódica (simples ou composta).
    
    Retorna uma tupla:
      (num_bruto, den_bruto, num_simplificado, den_simplificado)
      
    Fórmula:
      Numerador = (Número formado pela parte inteira, antiperíodo e período)
                - (Número formado pela parte inteira e antiperíodo)
      Denominador = (tantos noves quantos forem os dígitos do período)
                    seguidos de (tantos zeros quantos forem os dígitos do antiperíodo)
    """
    if not periodo:
        raise ValueError("O período não pode ser vazio para uma dízima periódica.")
        
    p_len = len(periodo)
    a_len = len(antiperiodo) if antiperiodo else 0
    
    str_inteira = str(abs(parte_inteira))
    
    # Número completo até o final do primeiro período
    str_total = str_inteira + (antiperiodo or "") + periodo
    val_total = int(str_total)
    
    # Número até antes do início do período
    str_nao_periodico = str_inteira + (antiperiodo or "")
    val_nao_periodico = int(str_nao_periodico)
    
    numerador_bruto = val_total - val_nao_periodico
    denominador_bruto = int(("9" * p_len) + ("0" * a_len))
    
    if negativo:
        numerador_bruto = -numerador_bruto
        
    num_simp, den_simp = simplificar_fracao(numerador_bruto, denominador_bruto)
    return numerador_bruto, denominador_bruto, num_simp, den_simp
