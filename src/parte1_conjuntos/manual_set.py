"""
Implementação Manual da Teoria dos Conjuntos.
Atende ao desafio de NÃO usar operadores prontos de conjuntos da linguagem.
Todas as operações utilizam estritamente laços (for/while) e condicionais (if/else).
"""
from typing import Any, List


class ManualSetOperations:
    """
    Coleção de operações fundamentais de teoria dos conjuntos
    implementadas artesanalmente com laços e condicionais sobre listas.
    """

    @staticmethod
    def eliminar_repetidos(elementos: List[Any]) -> List[Any]:
        """
        Garante a unicidade dos elementos de um conjunto.
        Percorre a lista e insere apenas os elementos ainda não vistos.
        """
        unicos: List[Any] = []
        for x in elementos:
            ja_existe = False
            for u in unicos:
                if u == x:
                    ja_existe = True
                    break
            if not ja_existe:
                unicos.append(x)
        return unicos

    @staticmethod
    def pertence(elemento: Any, conjunto: List[Any]) -> bool:
        """
        Verificação de pertinência: x ∈ A.
        Retorna True se o elemento está presente no conjunto, False caso contrário.
        """
        for item in conjunto:
            if item == elemento:
                return True
        return False

    @staticmethod
    def cardinalidade(conjunto: List[Any]) -> int:
        """
        Calcula a cardinalidade (|A|), contando manualmente os elementos únicos.
        """
        unicos = ManualSetOperations.eliminar_repetidos(conjunto)
        contador = 0
        for _ in unicos:
            contador += 1
        return contador

    @staticmethod
    def uniao(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Any]:
        """
        União: A ∪ B = {x | x ∈ A ou x ∈ B}.
        """
        resultado: List[Any] = []
        
        # Adiciona todos os elementos únicos de A
        for item in conjunto_a:
            if not ManualSetOperations.pertence(item, resultado):
                resultado.append(item)
                
        # Adiciona elementos de B que ainda não estão no resultado
        for item in conjunto_b:
            if not ManualSetOperations.pertence(item, resultado):
                resultado.append(item)
                
        return resultado

    @staticmethod
    def intersecao(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Any]:
        """
        Interseção: A ∩ B = {x | x ∈ A e x ∈ B}.
        """
        resultado: List[Any] = []
        for item in conjunto_a:
            if ManualSetOperations.pertence(item, conjunto_b):
                if not ManualSetOperations.pertence(item, resultado):
                    resultado.append(item)
        return resultado

    @staticmethod
    def diferenca(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Any]:
        """
        Diferença: A - B = {x | x ∈ A e x ∉ B}.
        """
        resultado: List[Any] = []
        for item in conjunto_a:
            if not ManualSetOperations.pertence(item, conjunto_b):
                if not ManualSetOperations.pertence(item, resultado):
                    resultado.append(item)
        return resultado

    @staticmethod
    def diferenca_simetrica(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Any]:
        """
        Diferença Simétrica: A Δ B = (A - B) ∪ (B - A).
        Implementado com laços: elementos que pertencem a A ou a B, mas não a ambos.
        """
        diff_a_b = ManualSetOperations.diferenca(conjunto_a, conjunto_b)
        diff_b_a = ManualSetOperations.diferenca(conjunto_b, conjunto_a)
        return ManualSetOperations.uniao(diff_a_b, diff_b_a)

    @staticmethod
    def subconjunto(conjunto_a: List[Any], conjunto_b: List[Any]) -> bool:
        """
        Inclusão: A ⊆ B (A está contido em B).
        Todo elemento de A deve pertencer a B.
        O conjunto vazio (Ø) está contido em qualquer conjunto.
        """
        for item in conjunto_a:
            if not ManualSetOperations.pertence(item, conjunto_b):
                return False
        return True

    @staticmethod
    def subconjunto_proprio(conjunto_a: List[Any], conjunto_b: List[Any]) -> bool:
        """
        Inclusão Própria: A ⊂ B.
        A ⊆ B e A ≠ B (ou seja, existe pelo menos um elemento em B que não está em A).
        """
        if not ManualSetOperations.subconjunto(conjunto_a, conjunto_b):
            return False
        
        card_a = ManualSetOperations.cardinalidade(conjunto_a)
        card_b = ManualSetOperations.cardinalidade(conjunto_b)
        return card_a < card_b

    @staticmethod
    def complemento(conjunto_a: List[Any], universo: List[Any]) -> List[Any]:
        """
        Complementar de A em relação a U: A^c = U - A.
        Elementos que pertencem ao universo U mas não pertencem a A.
        """
        return ManualSetOperations.diferenca(universo, conjunto_a)
