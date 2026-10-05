"""
Testes unitários para a Parte 1: Teoria dos Conjuntos.
Verifica todos os casos de borda e a equivalência exata entre implementação manual e nativa.
"""
import unittest
from src.parte1_conjuntos.manual_set import ManualSetOperations
from src.parte1_conjuntos.native_comparator import SetComparator
from src.utils.helpers import parse_set_input


class TestParte1Conjuntos(unittest.TestCase):

    def test_caso_geral_e_repetidos(self):
        """Testa eliminação de repetidos: A = 1, 2, 2, 3, 4 -> A = {1, 2, 3, 4}, |A| = 4."""
        entrada_a = parse_set_input("1, 2, 2, 3, 4")
        self.assertEqual(sorted(entrada_a), [1, 2, 3, 4])
        self.assertEqual(ManualSetOperations.cardinalidade(entrada_a), 4)

        entrada_b = parse_set_input("3, 4, 5, 6")
        self.assertEqual(sorted(entrada_b), [3, 4, 5, 6])

        # Operações
        uniao = ManualSetOperations.uniao(entrada_a, entrada_b)
        self.assertEqual(sorted(uniao), [1, 2, 3, 4, 5, 6])

        inter = ManualSetOperations.intersecao(entrada_a, entrada_b)
        self.assertEqual(sorted(inter), [3, 4])

        diff_ab = ManualSetOperations.diferenca(entrada_a, entrada_b)
        self.assertEqual(sorted(diff_ab), [1, 2])

        diff_ba = ManualSetOperations.diferenca(entrada_b, entrada_a)
        self.assertEqual(sorted(diff_ba), [5, 6])

        diff_sim = ManualSetOperations.diferenca_simetrica(entrada_a, entrada_b)
        self.assertEqual(sorted(diff_sim), [1, 2, 5, 6])

        universo = list(range(1, 11))
        comp_a = ManualSetOperations.complemento(entrada_a, universo)
        self.assertEqual(sorted(comp_a), [5, 6, 7, 8, 9, 10])

        # Pertinência
        self.assertTrue(ManualSetOperations.pertence(3, entrada_a))
        self.assertFalse(ManualSetOperations.pertence(5, entrada_a))

        # Inclusão
        sub = [3, 4]
        self.assertTrue(ManualSetOperations.subconjunto(sub, entrada_a))
        self.assertTrue(ManualSetOperations.subconjunto_proprio(sub, entrada_a))

    def test_caso_borda_conjunto_vazio(self):
        """A = Ø, B = {1, 2} -> A ∪ B = {1, 2}, A ∩ B = Ø, A ⊆ B é True."""
        a = []
        b = [1, 2]
        self.assertEqual(sorted(ManualSetOperations.uniao(a, b)), [1, 2])
        self.assertEqual(ManualSetOperations.intersecao(a, b), [])
        self.assertTrue(ManualSetOperations.subconjunto(a, b))
        self.assertTrue(ManualSetOperations.subconjunto_proprio(a, b))

    def test_caso_borda_conjuntos_iguais(self):
        """A = B = {1, 2, 3} -> A - B = Ø, A Δ B = Ø, A ⊆ B é True, A ⊂ B é False."""
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertEqual(ManualSetOperations.diferenca(a, b), [])
        self.assertEqual(ManualSetOperations.diferenca_simetrica(a, b), [])
        self.assertTrue(ManualSetOperations.subconjunto(a, b))
        self.assertFalse(ManualSetOperations.subconjunto_proprio(a, b))

    def test_caso_borda_conjuntos_disjuntos(self):
        """A = {1, 2}, B = {3, 4} -> A ∩ B = Ø, A ∪ B = {1, 2, 3, 4}, A Δ B = {1, 2, 3, 4}."""
        a = [1, 2]
        b = [3, 4]
        self.assertEqual(ManualSetOperations.intersecao(a, b), [])
        self.assertEqual(sorted(ManualSetOperations.uniao(a, b)), [1, 2, 3, 4])
        self.assertEqual(sorted(ManualSetOperations.diferenca_simetrica(a, b)), [1, 2, 3, 4])

    def test_caso_borda_um_contido_no_outro(self):
        """A = {1, 2}, B = {1, 2, 3} -> A ⊂ B é True, B ⊆ A é False, B - A = {3}."""
        a = [1, 2]
        b = [1, 2, 3]
        self.assertTrue(ManualSetOperations.subconjunto_proprio(a, b))
        self.assertFalse(ManualSetOperations.subconjunto(b, a))
        self.assertEqual(sorted(ManualSetOperations.diferenca(b, a)), [3])

    def test_repetidos_na_entrada(self):
        """A = 1, 1, 1, 2 -> A = {1, 2}; |A| = 2."""
        a = parse_set_input("1, 1, 1, 2")
        self.assertEqual(sorted(a), [1, 2])
        self.assertEqual(ManualSetOperations.cardinalidade(a), 2)

    def test_validacao_completa_contra_solucao_nativa(self):
        """Compara todas as operações com a solução nativa Python set."""
        a = [10, 20, 30, 40]
        b = [30, 40, 50, 60]
        u = [10, 20, 30, 40, 50, 60, 70, 80]
        
        relatorio = SetComparator.comparar_todas(a, b, u, elemento_teste=20, subconjunto_teste=[10, 20])
        for chave, item in relatorio.items():
            self.assertTrue(item["valido"], f"Falha na validação nativa para: {chave}")


if __name__ == "__main__":
    unittest.main()
