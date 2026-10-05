"""
Testes unitários para a Parte 3: Integração e Mini-Projetos Avançados.
Cobre Jaccard, RBAC, Análise Combinatória (2^n) e Intervalos Reais.
"""
import unittest
from src.parte3_integracao.cartesian_powerset import CombinatoricsSets
from src.parte3_integracao.jaccard_recommender import JaccardRecommender
from src.parte3_integracao.rbac_access_control import RBACSystem
from src.parte3_integracao.real_intervals import IntervaloReal


class TestParte3Integracao(unittest.TestCase):

    def test_jaccard_recomendador_oficial(self):
        """Testa o gabarito oficial de afinidade de Jaccard."""
        rec = JaccardRecommender()
        rec.carregar_dados_padrao()

        # Ana e Bia: 2/6 ≈ 0.3333
        c_ab = rec.calcular_afinidade("Ana", "Bia")
        self.assertEqual(sorted(c_ab.intersecao), ["cinema", "jazz"])
        self.assertEqual(c_ab.tamanho_intersecao, 2)
        self.assertEqual(c_ab.tamanho_uniao, 6)
        self.assertAlmostEqual(c_ab.indice_jaccard, 2 / 6, places=2)

        # Ana e Caio: 2/5 = 0.40
        c_ac = rec.calcular_afinidade("Ana", "Caio")
        self.assertEqual(sorted(c_ac.intersecao), ["cinema", "games"])
        self.assertEqual(c_ac.tamanho_intersecao, 2)
        self.assertEqual(c_ac.tamanho_uniao, 5)
        self.assertAlmostEqual(c_ac.indice_jaccard, 0.40, places=2)

        # Bia e Caio: 1/6 ≈ 0.17
        c_bc = rec.calcular_afinidade("Bia", "Caio")
        self.assertEqual(sorted(c_bc.intersecao), ["cinema"])
        self.assertEqual(c_bc.tamanho_intersecao, 1)
        self.assertEqual(c_bc.tamanho_uniao, 6)
        self.assertAlmostEqual(c_bc.indice_jaccard, 1 / 6, places=2)

        # Recomendação para Ana deve ser Caio em 1º lugar
        recs_ana = rec.recomendar_para("Ana")
        self.assertEqual(recs_ana[0][0], "Caio")
        self.assertEqual(recs_ana[1][0], "Bia")

    def test_rbac_controle_acesso(self):
        """Testa o controle de acesso por união e subconjuntos de perfis."""
        rbac = RBACSystem()
        rbac.carregar_dados_padrao()

        # Usuário A (leitor + editor)
        perms_a = rbac.obter_permissoes_usuario("usuario_a")
        self.assertEqual(sorted(perms_a), ["editar", "ler"])

        # Usuário B (editor + financeiro)
        perms_b = rbac.obter_permissoes_usuario("usuario_b")
        self.assertEqual(sorted(perms_b), ["editar", "ler", "ver_relatorios"])

        # Pertinência: usuário B pode excluir? Não!
        self.assertFalse(rbac.verificar_permissao("usuario_b", "excluir"))
        # Usuário B pode ver_relatorios? Sim!
        self.assertTrue(rbac.verificar_permissao("usuario_b", "ver_relatorios"))

        # Inclusão: editor ⊆ admin? Verdadeiro
        self.assertTrue(rbac.perfil_eh_subconjunto("editor", "admin"))
        # financeiro ⊆ admin? Falso
        self.assertFalse(rbac.perfil_eh_subconjunto("financeiro", "admin"))

    def test_combinatoria_e_conjunto_das_partes(self):
        """Testa produto cartesiano e cardinalidade 2^n das partes."""
        a = ["A", "B"]
        b = [1, 2, 3]
        prod = CombinatoricsSets.produto_cartesiano(a, b)
        self.assertEqual(len(prod), 6)
        self.assertIn(("A", 1), prod)
        self.assertIn(("B", 3), prod)

        # Partes de {1, 2, 3} -> 2^3 = 8 subconjuntos
        partes = CombinatoricsSets.conjunto_das_partes([1, 2, 3])
        self.assertEqual(len(partes), 8)
        self.assertIn([], partes)
        self.assertIn([1, 2, 3], partes)

    def test_intervalos_reais(self):
        """Testa pertinência e interseção de intervalos contínuos."""
        i1 = IntervaloReal(2, 5, fechado_esq=True, fechado_dir=False)  # [2, 5)
        i2 = IntervaloReal(3, 7, fechado_esq=True, fechado_dir=True)   # [3, 7]

        # Pertinência em I1 [2, 5)
        self.assertTrue(i1.contem(2.0))
        self.assertTrue(i1.contem(4.999))
        self.assertFalse(i1.contem(5.0))
        self.assertFalse(i1.contem(1.9))

        # Interseção [2, 5) ∩ [3, 7] = [3, 5)
        inter = i1.intersecao(i2)
        self.assertIsNotNone(inter)
        self.assertEqual(inter.inicio, 3.0)
        self.assertEqual(inter.fim, 5.0)
        self.assertTrue(inter.fechado_esq)
        self.assertFalse(inter.fechado_dir)
        self.assertEqual(repr(inter), "[3, 5)")


if __name__ == "__main__":
    unittest.main()
