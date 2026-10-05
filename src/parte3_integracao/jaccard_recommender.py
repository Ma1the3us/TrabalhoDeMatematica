"""
Mini-Projeto 1: Sistema de Recomendação Simples por Afinidade.
Utiliza a Teoria dos Conjuntos para calcular o Índice de Similaridade de Jaccard:
  Jaccard(A, B) = |A ∩ B| / |A ∪ B|
"""
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple
from src.parte1_conjuntos.manual_set import ManualSetOperations


@dataclass
class JaccardComparison:
    usuario_1: str
    usuario_2: str
    intersecao: List[str]
    uniao: List[str]
    tamanho_intersecao: int
    tamanho_uniao: int
    indice_jaccard: float


class JaccardRecommender:
    """
    Sistema de recomendação baseado no coeficiente de similaridade de Jaccard.
    """

    def __init__(self):
        self.usuarios: Dict[str, List[str]] = {}

    def adicionar_usuario(self, nome: str, interesses: List[str]) -> None:
        """Cadastra ou atualiza o perfil de interesses de um usuário."""
        # Limpa e descarta duplicados artesanalmente
        unicos = ManualSetOperations.eliminar_repetidos([i.strip().lower() for i in interesses if i.strip()])
        self.usuarios[nome] = unicos

    def carregar_dados_padrao(self) -> None:
        """Carrega os dados de exemplo fornecidos na atividade."""
        self.adicionar_usuario("Ana", ["rock", "jazz", "cinema", "games"])
        self.adicionar_usuario("Bia", ["jazz", "cinema", "séries", "viagens"])
        self.adicionar_usuario("Caio", ["games", "tecnologia", "cinema"])

    def calcular_afinidade(self, nome1: str, nome2: str) -> JaccardComparison:
        """Calcula o índice de Jaccard entre dois usuários."""
        if nome1 not in self.usuarios or nome2 not in self.usuarios:
            raise KeyError("Usuário não encontrado na base.")

        int1 = self.usuarios[nome1]
        int2 = self.usuarios[nome2]

        # Operações manuais com conjuntos
        inter = ManualSetOperations.intersecao(int1, int2)
        uniao = ManualSetOperations.uniao(int1, int2)

        len_inter = ManualSetOperations.cardinalidade(inter)
        len_uniao = ManualSetOperations.cardinalidade(uniao)

        indice = (len_inter / len_uniao) if len_uniao > 0 else 0.0

        return JaccardComparison(
            usuario_1=nome1,
            usuario_2=nome2,
            intersecao=inter,
            uniao=uniao,
            tamanho_intersecao=len_inter,
            tamanho_uniao=len_uniao,
            indice_jaccard=indice
        )

    def recomendar_para(self, nome_alvo: str) -> List[Tuple[str, float, JaccardComparison]]:
        """
        Retorna uma lista ordenada decrescente de recomendações
        de usuários para o usuário alvo com base na afinidade.
        """
        if nome_alvo not in self.usuarios:
            raise KeyError(f"Usuário '{nome_alvo}' não encontrado.")

        resultados = []
        for outro_nome in self.usuarios:
            if outro_nome == nome_alvo:
                continue
            comp = self.calcular_afinidade(nome_alvo, outro_nome)
            resultados.append((outro_nome, comp.indice_jaccard, comp))

        # Ordenação decrescente pelo índice
        resultados.sort(key=lambda x: x[1], reverse=True)
        return resultados
