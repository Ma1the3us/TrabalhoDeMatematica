"""
Mini-Projeto 2: Controle de Acesso Baseado em Perfis (RBAC - Role-Based Access Control).
Representa permissões como conjuntos finitos e utiliza teoria dos conjuntos
(união, inclusão de subconjuntos e pertinência) para autorização de recursos.
"""
from typing import Dict, List, Set
from src.parte1_conjuntos.manual_set import ManualSetOperations


class RBACSystem:
    """
    Sistema de Controle de Acesso Baseado em Perfis.
    """

    def __init__(self):
        self.perfis: Dict[str, List[str]] = {}
        self.usuarios: Dict[str, List[str]] = {}  # usuario -> lista de perfis

    def carregar_dados_padrao(self) -> None:
        """Carrega os perfis e permissões da atividade."""
        self.perfis = {
            "leitor": ["ler"],
            "editor": ["ler", "editar"],
            "admin": ["ler", "editar", "excluir", "gerir_usuarios"],
            "financeiro": ["ver_relatorios"],
        }
        self.usuarios = {
            "usuario_a": ["leitor", "editor"],
            "usuario_b": ["editor", "financeiro"],
            "super_user": ["admin"]
        }

    def cadastrar_perfil(self, nome_perfil: str, permissoes: List[str]) -> None:
        """Adiciona ou atualiza um perfil com seu conjunto de permissões."""
        self.perfis[nome_perfil] = ManualSetOperations.eliminar_repetidos(permissoes)

    def associar_perfis_usuario(self, nome_usuario: str, perfis: List[str]) -> None:
        """Associa um conjunto de perfis a um usuário."""
        for p in perfis:
            if p not in self.perfis:
                raise KeyError(f"Perfil '{p}' não existe no sistema.")
        self.usuarios[nome_usuario] = ManualSetOperations.eliminar_repetidos(perfis)

    def obter_permissoes_usuario(self, nome_usuario: str) -> List[str]:
        """
        Calcula as permissões efetivas do usuário através da UNIÃO
        das permissões de todos os perfis associados a ele:
          Permissoes_Efetivas = ⋃ (Permissoes(P_i))
        """
        if nome_usuario not in self.usuarios:
            raise KeyError(f"Usuário '{nome_usuario}' não cadastrado.")

        perfis_do_usuario = self.usuarios[nome_usuario]
        permissoes_totais: List[str] = []

        for p in perfis_do_usuario:
            perms = self.perfis.get(p, [])
            permissoes_totais = ManualSetOperations.uniao(permissoes_totais, perms)

        return permissoes_totais

    def verificar_permissao(self, nome_usuario: str, permissao: str) -> bool:
        """
        Verifica pertinência: permissao ∈ Permissoes_Efetivas.
        """
        permissoes = self.obter_permissoes_usuario(nome_usuario)
        return ManualSetOperations.pertence(permissao, permissoes)

    def perfil_eh_subconjunto(self, perfil_origem: str, perfil_destino: str) -> bool:
        """
        Verifica se um perfil é subconjunto de outro:
          Permissoes(origem) ⊆ Permissoes(destino)
        """
        if perfil_origem not in self.perfis or perfil_destino not in self.perfis:
            raise KeyError("Um dos perfis informados não existe.")

        p_origem = self.perfis[perfil_origem]
        p_destino = self.perfis[perfil_destino]
        return ManualSetOperations.subconjunto(p_origem, p_destino)
