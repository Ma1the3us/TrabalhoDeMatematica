"""
Comparador e validador nativo de conjuntos.
Executa as operações usando os tipos e operadores nativos do Python (set / frozenset)
e valida os resultados com a implementação manual.
"""
from typing import Any, Dict, List, Set
from src.parte1_conjuntos.manual_set import ManualSetOperations


class NativeSetOperations:
    """Implementação nativa de referência usando Python set."""

    @staticmethod
    def eliminar_repetidos(elementos: List[Any]) -> Set[Any]:
        return set(elementos)

    @staticmethod
    def pertence(elemento: Any, conjunto: Set[Any]) -> bool:
        return elemento in conjunto

    @staticmethod
    def cardinalidade(conjunto: Set[Any]) -> int:
        return len(conjunto)

    @staticmethod
    def uniao(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> Set[Any]:
        return conjunto_a | conjunto_b

    @staticmethod
    def intersecao(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> Set[Any]:
        return conjunto_a & conjunto_b

    @staticmethod
    def diferenca(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> Set[Any]:
        return conjunto_a - conjunto_b

    @staticmethod
    def diferenca_simetrica(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> Set[Any]:
        return conjunto_a ^ conjunto_b

    @staticmethod
    def subconjunto(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> bool:
        return conjunto_a <= conjunto_b

    @staticmethod
    def subconjunto_proprio(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> bool:
        return conjunto_a < conjunto_b

    @staticmethod
    def complemento(conjunto_a: Set[Any], universo: Set[Any]) -> Set[Any]:
        return universo - conjunto_a


class SetComparator:
    """
    Compara e valida a implementação manual contra a implementação nativa.
    """

    @classmethod
    def comparar_todas(
        cls,
        lista_a: List[Any],
        lista_b: List[Any],
        lista_u: List[Any] = None,
        elemento_teste: Any = None,
        subconjunto_teste: List[Any] = None
    ) -> Dict[str, Dict[str, Any]]:
        """
        Executa todas as operações em ambas as abordagens e retorna um dicionário
        com os valores obtidos e o status de validação (identidade comprovada).
        """
        if lista_u is None:
            # Se não informado, universo é a união dos elementos ou 1 a 10
            lista_u = list(range(1, 11))

        # 1. Sanitização
        manual_a = ManualSetOperations.eliminar_repetidos(lista_a)
        manual_b = ManualSetOperations.eliminar_repetidos(lista_b)
        manual_u = ManualSetOperations.eliminar_repetidos(lista_u)

        native_a = NativeSetOperations.eliminar_repetidos(lista_a)
        native_b = NativeSetOperations.eliminar_repetidos(lista_b)
        native_u = NativeSetOperations.eliminar_repetidos(lista_u)

        # 2. Operações
        op_manual_uniao = ManualSetOperations.uniao(manual_a, manual_b)
        op_native_uniao = NativeSetOperations.uniao(native_a, native_b)

        op_manual_inter = ManualSetOperations.intersecao(manual_a, manual_b)
        op_native_inter = NativeSetOperations.intersecao(native_a, native_b)

        op_manual_diff_ab = ManualSetOperations.diferenca(manual_a, manual_b)
        op_native_diff_ab = NativeSetOperations.diferenca(native_a, native_b)

        op_manual_diff_ba = ManualSetOperations.diferenca(manual_b, manual_a)
        op_native_diff_ba = NativeSetOperations.diferenca(native_b, manual_b if False else native_a)

        op_manual_diff_sim = ManualSetOperations.diferenca_simetrica(manual_a, manual_b)
        op_native_diff_sim = NativeSetOperations.diferenca_simetrica(native_a, native_b)

        op_manual_card_a = ManualSetOperations.cardinalidade(manual_a)
        op_native_card_a = NativeSetOperations.cardinalidade(native_a)

        op_manual_card_b = ManualSetOperations.cardinalidade(manual_b)
        op_native_card_b = NativeSetOperations.cardinalidade(native_b)

        op_manual_sub_ab = ManualSetOperations.subconjunto(manual_a, manual_b)
        op_native_sub_ab = NativeSetOperations.subconjunto(native_a, native_b)

        op_manual_subp_ab = ManualSetOperations.subconjunto_proprio(manual_a, manual_b)
        op_native_subp_ab = NativeSetOperations.subconjunto_proprio(native_a, native_b)

        op_manual_comp_a = ManualSetOperations.complemento(manual_a, manual_u)
        op_native_comp_a = NativeSetOperations.complemento(native_a, native_u)

        relatorio: Dict[str, Dict[str, Any]] = {
            "Conjunto A": {
                "manual": manual_a,
                "nativa": native_a,
                "valido": set(manual_a) == native_a
            },
            "Conjunto B": {
                "manual": manual_b,
                "nativa": native_b,
                "valido": set(manual_b) == native_b
            },
            "|A| (Cardinalidade de A)": {
                "manual": op_manual_card_a,
                "nativa": op_native_card_a,
                "valido": op_manual_card_a == op_native_card_a
            },
            "|B| (Cardinalidade de B)": {
                "manual": op_manual_card_b,
                "nativa": op_native_card_b,
                "valido": op_manual_card_b == op_native_card_b
            },
            "A ∪ B (União)": {
                "manual": op_manual_uniao,
                "nativa": op_native_uniao,
                "valido": set(op_manual_uniao) == op_native_uniao
            },
            "A ∩ B (Interseção)": {
                "manual": op_manual_inter,
                "nativa": op_native_inter,
                "valido": set(op_manual_inter) == op_native_inter
            },
            "A - B (Diferença)": {
                "manual": op_manual_diff_ab,
                "nativa": op_native_diff_ab,
                "valido": set(op_manual_diff_ab) == op_native_diff_ab
            },
            "B - A (Diferença)": {
                "manual": op_manual_diff_ba,
                "nativa": op_native_diff_ba,
                "valido": set(op_manual_diff_ba) == op_native_diff_ba
            },
            "A Δ B (Diferença Simétrica)": {
                "manual": op_manual_diff_sim,
                "nativa": op_native_diff_sim,
                "valido": set(op_manual_diff_sim) == op_native_diff_sim
            },
            "A ⊆ B (Inclusão/Subconjunto)": {
                "manual": op_manual_sub_ab,
                "nativa": op_native_sub_ab,
                "valido": op_manual_sub_ab == op_native_sub_ab
            },
            "A ⊂ B (Inclusão Própria)": {
                "manual": op_manual_subp_ab,
                "nativa": op_native_subp_ab,
                "valido": op_manual_subp_ab == op_native_subp_ab
            },
            "Complemento de A em U": {
                "manual": op_manual_comp_a,
                "nativa": op_native_comp_a,
                "valido": set(op_manual_comp_a) == op_native_comp_a
            },
        }

        # Pertinência se testado
        if elemento_teste is not None:
            relatorio[f"{elemento_teste} ∈ A (Pertinência)"] = {
                "manual": ManualSetOperations.pertence(elemento_teste, manual_a),
                "nativa": NativeSetOperations.pertence(elemento_teste, native_a),
                "valido": ManualSetOperations.pertence(elemento_teste, manual_a) == NativeSetOperations.pertence(elemento_teste, native_a)
            }

        # Subconjunto de teste se fornecido
        if subconjunto_teste is not None:
            sub_manual = ManualSetOperations.eliminar_repetidos(subconjunto_teste)
            sub_native = NativeSetOperations.eliminar_repetidos(subconjunto_teste)
            relatorio[f"{sub_manual} ⊆ A"] = {
                "manual": ManualSetOperations.subconjunto(sub_manual, manual_a),
                "nativa": NativeSetOperations.subconjunto(sub_native, native_a),
                "valido": ManualSetOperations.subconjunto(sub_manual, manual_a) == NativeSetOperations.subconjunto(sub_native, native_a)
            }
            relatorio[f"{sub_manual} ⊂ A"] = {
                "manual": ManualSetOperations.subconjunto_proprio(sub_manual, manual_a),
                "nativa": NativeSetOperations.subconjunto_proprio(sub_native, native_a),
                "valido": ManualSetOperations.subconjunto_proprio(sub_manual, manual_a) == NativeSetOperations.subconjunto_proprio(sub_native, native_a)
            }

        return relatorio
