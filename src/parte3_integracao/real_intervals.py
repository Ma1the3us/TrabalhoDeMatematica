"""
Mini-Projeto 4: Intervalos Reais na Reta Numérica.
Classe que representa subconjuntos contínuos de R como [a, b], [a, b), (a, b] ou (a, b)
e implementa pertinência, interseção e união de intervalos.
"""
from typing import Optional, Union


class IntervaloReal:
    """
    Representa um intervalo na reta real.
    Exemplos:
      IntervaloReal(2, 5, fechado_esq=True, fechado_dir=False) -> [2, 5)
    """

    def __init__(self, inicio: float, fim: float, fechado_esq: bool = True, fechado_dir: bool = True):
        if inicio > fim:
            raise ValueError(f"Início ({inicio}) não pode ser maior que o fim ({fim}).")
        if inicio == fim and (not fechado_esq or not fechado_dir):
            raise ValueError("Intervalo degenerado aberto é conjunto vazio.")
            
        self.inicio = float(inicio)
        self.fim = float(fim)
        self.fechado_esq = fechado_esq
        self.fechado_dir = fechado_dir

    def contem(self, x: float) -> bool:
        """Verifica se x ∈ [a, b] (pertinência)."""
        val = float(x)
        valida_esq = (val >= self.inicio) if self.fechado_esq else (val > self.inicio)
        valida_dir = (val <= self.fim) if self.fechado_dir else (val < self.fim)
        return valida_esq and valida_dir

    def intersecao(self, outro: "IntervaloReal") -> Optional["IntervaloReal"]:
        """
        Calcula a interseção entre dois intervalos reais.
        Retorna um novo IntervaloReal ou None caso sejam disjuntos (Ø).
        """
        # Determina o início da interseção (máximo dos inícios)
        if self.inicio > outro.inicio:
            novo_inicio = self.inicio
            fech_esq = self.fechado_esq
        elif self.inicio < outro.inicio:
            novo_inicio = outro.inicio
            fech_esq = outro.fechado_esq
        else:
            novo_inicio = self.inicio
            fech_esq = self.fechado_esq and outro.fechado_esq

        # Determina o fim da interseção (mínimo dos fins)
        if self.fim < outro.fim:
            novo_fim = self.fim
            fech_dir = self.fechado_dir
        elif self.fim > outro.fim:
            novo_fim = outro.fim
            fech_dir = outro.fechado_dir
        else:
            novo_fim = self.fim
            fech_dir = self.fechado_dir and outro.fechado_dir

        # Verifica se a interseção é válida
        if novo_inicio > novo_fim:
            return None
        if novo_inicio == novo_fim and not (fech_esq and fech_dir):
            return None

        return IntervaloReal(novo_inicio, novo_fim, fech_esq, fech_dir)

    def __repr__(self) -> str:
        esq = "[" if self.fechado_esq else "("
        dir_ = "]" if self.fechado_dir else ")"
        # Formata números inteiros sem casa decimal .0 se possível
        ini_str = str(int(self.inicio)) if self.inicio.is_integer() else str(self.inicio)
        fim_str = str(int(self.fim)) if self.fim.is_integer() else str(self.fim)
        return f"{esq}{ini_str}, {fim_str}{dir_}"
