"""
Ponto de Entrada Principal - Laboratório de Conjuntos
Curso: Desenvolvimento de Software Multiplataforma (DSM) - FATEC Osasco
"""
import sys

if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stdin, "reconfigure"):
            sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from src.parte1_conjuntos.cli_parte1 import menu_parte1_interativo
from src.parte2_numeros.cli_parte2 import menu_parte2_interativo
from src.parte3_integracao.cli_parte3 import menu_parte3_interativo
from src.utils.display import Colors, print_header, print_section
from run_demos import executar_e_gravar_todos_os_logs
from run_tests import executar_testes


def menu_principal() -> None:
    """Menu principal unificado do projeto."""
    while True:
        print_header(
            "LABORATÓRIO DE CONJUNTOS E CONJUNTOS NUMÉRICOS",
            "FATEC Osasco - Desenvolvimento de Software Multiplataforma"
        )
        print("  1. Parte 1: Teoria dos Conjuntos (Básico: Operações Manuais vs Nativas)")
        print("  2. Parte 2: Conjuntos Numéricos (Intermediário: Classificador e Dízimas)")
        print("  3. Parte 3: Mini-Projetos de Integração (Avançado: Jaccard, RBAC, etc.)")
        print("  4. Executar Bateria Completa de Demonstrações (Gerar Logs)")
        print("  5. Executar Testes Unitários Automatizados")
        print("  0. Sair do Programa")
        
        opcao = input(f"\n{Colors.BOLD}Selecione uma opção (0-5): {Colors.END}").strip()
        
        if opcao == "0":
            print(f"\n{Colors.GREEN}Encerrando o programa. Até logo!{Colors.END}\n")
            sys.exit(0)
        elif opcao == "1":
            menu_parte1_interativo()
        elif opcao == "2":
            menu_parte2_interativo()
        elif opcao == "3":
            menu_parte3_interativo()
        elif opcao == "4":
            executar_e_gravar_todos_os_logs()
            input(f"\n{Colors.BOLD}Pressione [Enter] para voltar ao menu...{Colors.END}")
        elif opcao == "5":
            executar_testes()
            input(f"\n{Colors.BOLD}Pressione [Enter] para voltar ao menu...{Colors.END}")
        else:
            print(f"{Colors.RED}Opção inválida! Escolha entre 0 e 5.{Colors.END}\n")


if __name__ == "__main__":
    menu_principal()
