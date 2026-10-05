"""
Bônus da Parte 2:
1. Geração de números primos até n via Crivo de Eratóstenes.
2. Listagem de todos os divisores inteiros positivos de um número.
"""
from typing import List


def crivo_eratostenes(limite: int) -> List[int]:
    """
    Gera todos os números primos de 2 até 'limite' utilizando o clássico
    algoritmo do Crivo de Eratóstenes.
    
    Exemplo: limite = 30 -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    if limite < 2:
        return []
        
    eh_primo = [True] * (limite + 1)
    eh_primo[0] = False
    eh_primo[1] = False
    
    p = 2
    while p * p <= limite:
        if eh_primo[p]:
            for multiplo in range(p * p, limite + 1, p):
                eh_primo[multiplo] = False
        p += 1
        
    primos = [i for i in range(2, limite + 1) if eh_primo[i]]
    return primos


def listar_divisores(numero: int) -> List[int]:
    """
    Lista todos os divisores inteiros positivos de um número dado.
    
    Exemplo: numero = 36 -> [1, 2, 3, 4, 6, 9, 12, 18, 36]
    """
    n = abs(numero)
    if n == 0:
        return []
        
    divisores = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisores.append(i)
            outro = n // i
            if outro != i:
                divisores.append(outro)
        i += 1
        
    divisores.sort()
    return divisores
