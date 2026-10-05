"""
Testes unitários para a Parte 2: Conjuntos Numéricos.
Verifica a classificação, cálculo de frações geratrizes e funções bônus.
"""
import unittest
from src.parte2_numeros.classifier import NumberClassifier
from src.parte2_numeros.generator_fraction import fracao_geratriz_dizima
from src.parte2_numeros.primes_divisors import crivo_eratostenes, listar_divisores


class TestParte2Numeros(unittest.TestCase):

    def test_classificacao_numero_natural(self):
        """7 -> N, Z, Q, R."""
        res = NumberClassifier.classificar("7")
        self.assertEqual(res.pertence, ["N", "Z", "Q", "R"])
        self.assertEqual(res.nao_pertence, ["I"])

    def test_classificacao_inteiro_negativo(self):
        """-3 -> Z, Q, R (não pertence a N nem I)."""
        res = NumberClassifier.classificar("-3")
        self.assertEqual(res.pertence, ["Z", "Q", "R"])
        self.assertIn("N", res.nao_pertence)
        self.assertIn("I", res.nao_pertence)

    def test_classificacao_zero(self):
        """0 -> N, Z, Q, R (convenção N inclui o zero)."""
        res = NumberClassifier.classificar("0")
        self.assertEqual(res.pertence, ["N", "Z", "Q", "R"])

    def test_classificacao_fracao_decimal(self):
        """3/4 -> Q, R."""
        res = NumberClassifier.classificar("3/4")
        self.assertEqual(res.pertence, ["Q", "R"])
        self.assertEqual(res.nao_pertence, ["N", "Z", "I"])
        self.assertEqual(res.parsed.valor_float, 0.75)

    def test_classificacao_fracao_negativa(self):
        """-5/2 -> Q, R."""
        res = NumberClassifier.classificar("-5/2")
        self.assertEqual(res.pertence, ["Q", "R"])
        self.assertEqual(res.parsed.valor_float, -2.5)

    def test_classificacao_fracao_redutivel_a_inteiro(self):
        """6/3 -> simplifica para 2 -> N, Z, Q, R."""
        res = NumberClassifier.classificar("6/3")
        self.assertEqual(res.pertence, ["N", "Z", "Q", "R"])
        self.assertEqual(res.parsed.numerador, 2)
        self.assertEqual(res.parsed.denominador, 1)

    def test_classificacao_dizima_simples_0_3(self):
        """0,(3) -> geratriz 1/3 -> Q, R."""
        res = NumberClassifier.classificar("0,(3)")
        self.assertEqual(res.pertence, ["Q", "R"])
        self.assertEqual(res.parsed.numerador, 1)
        self.assertEqual(res.parsed.denominador, 3)

    def test_classificacao_dizima_simples_2_7(self):
        """2,(7) -> geratriz 25/9 -> Q, R."""
        res = NumberClassifier.classificar("2,(7)")
        self.assertEqual(res.pertence, ["Q", "R"])
        self.assertEqual(res.parsed.numerador, 25)
        self.assertEqual(res.parsed.denominador, 9)

    def test_classificacao_dizima_composta_1_2_5(self):
        """1,2(5) -> geratriz 113/90 -> Q, R."""
        res = NumberClassifier.classificar("1,2(5)")
        self.assertEqual(res.pertence, ["Q", "R"])
        self.assertEqual(res.parsed.numerador, 113)
        self.assertEqual(res.parsed.denominador, 90)

    def test_classificacao_dizima_curiosa_0_9(self):
        """0,(9) -> geratriz 9/9 = 1 -> N, Z, Q, R."""
        res = NumberClassifier.classificar("0,(9)")
        self.assertEqual(res.pertence, ["N", "Z", "Q", "R"])
        self.assertEqual(res.parsed.numerador, 1)
        self.assertEqual(res.parsed.denominador, 1)

    def test_classificacao_raiz_exata(self):
        """V9 -> raiz exata 3 -> N, Z, Q, R."""
        res = NumberClassifier.classificar("V9")
        self.assertEqual(res.pertence, ["N", "Z", "Q", "R"])
        self.assertTrue(res.parsed.raiz_exata)
        self.assertEqual(res.parsed.valor_raiz, 3.0)

    def test_classificacao_raiz_irracional(self):
        """V2 -> raiz não exata -> I, R."""
        res = NumberClassifier.classificar("V2")
        self.assertEqual(res.pertence, ["I", "R"])
        self.assertEqual(res.nao_pertence, ["N", "Z", "Q"])
        self.assertFalse(res.parsed.raiz_exata)

    def test_crivo_eratostenes_ate_30(self):
        """Primos até 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29."""
        primos = crivo_eratostenes(30)
        esperado = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(primos, esperado)

    def test_divisores_de_36(self):
        """Divisores de 36: 1, 2, 3, 4, 6, 9, 12, 18, 36."""
        divs = listar_divisores(36)
        esperado = [1, 2, 3, 4, 6, 9, 12, 18, 36]
        self.assertEqual(divs, esperado)


if __name__ == "__main__":
    unittest.main()
