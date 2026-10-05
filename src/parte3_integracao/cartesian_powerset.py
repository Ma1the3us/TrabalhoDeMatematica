"""
Mini-Projeto 3: Produto Cartesiano e Conjunto das Partes (Power Set).
Implementação de gerador combinatório com análise de complexidade temporal e espacial (2^n).
"""
from typing import Any, List, Tuple
from src.parte1_conjuntos.manual_set import ManualSetOperations


class CombinatoricsSets:
    """
    Operações combinatórias estruturadas na Teoria dos Conjuntos.
    """

    @staticmethod
    def produto_cartesiano(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Tuple[Any, Any]]:
        """
        Calcula o Produto Cartesiano:
          A × B = {(a, b) | a ∈ A e b ∈ B}
        Cardinalidade: |A × B| = |A| * |B|
        """
        unicos_a = ManualSetOperations.eliminar_repetidos(conjunto_a)
        unicos_b = ManualSetOperations.eliminar_repetidos(conjunto_b)
        
        produto = []
        for a in unicos_a:
            for b in unicos_b:
                produto.append((a, b))
        return produto

    @staticmethod
    def conjunto_das_partes(conjunto: List[Any]) -> List[List[Any]]:
        """
        Gera o Conjunto das Partes P(A), ou seja, todos os subconjuntos de A.
        Cardinalidade: |P(A)| = 2^n, onde n = |A|.
        Implementado iterativamente com laços manuais.
        """
        unicos = ManualSetOperations.eliminar_repetidos(conjunto)
        partes: List[List[Any]] = [[]]  # Começa com o conjunto vazio Ø
        
        for elemento in unicos:
            novos_subconjuntos = []
            for subconjunto in partes:
                # Cria um novo subconjunto incluindo o elemento atual
                novo = list(subconjunto)
                novo.append(elemento)
                novos_subconjuntos.append(novo)
            partes.extend(novos_subconjuntos)
            
        return partes

    @staticmethod
    def analise_crescimento_partes(tamanhos: List[int]) -> List[Tuple[int, int, str]]:
        """
        Retorna tabela comparativa do crescimento da cardinalidade 2^n
        e o impacto computacional esperado.
        """
        dados = []
        for n in tamanhos:
            cardinalidade = 2 ** n
            if n <= 10:
                impacto = "Instantâneo (< 1 ms)"
            elif n <= 20:
                impacto = "Moderado (~1 milhão de elementos, memória OK)"
            elif n <= 25:
                impacto = "Crítico (~33 milhões de elementos, alto consumo de RAM)"
            else:
                impacto = "Inviável (Explosão Combinatória / Estouro de Memória)"
            dados.append((n, cardinalidade, impacto))
        return dados
