"""
Runner de Testes Automatizados.
Executa toda a suíte de testes com unittest nativo do Python (não exige pacotes externos).
"""
import sys
import unittest
from io import StringIO

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

from src.utils.display import Colors, print_header, print_section



def executar_testes() -> bool:
    """Executa todos os testes e exibe relatório visual."""
    print_header("SUÍTE DE TESTES UNITÁRIOS", "Laboratório de Conjuntos e Conjuntos Numéricos")
    
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")
    
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)
    
    output_log = stream.getvalue()
    print(output_log)
    
    print_section("Resumo da Execução dos Testes")
    total = result.testsRun
    erros = len(result.errors)
    falhas = len(result.failures)
    passaram = total - (erros + falhas)
    
    print(f"  Total de Testes Executados : {total}")
    print(f"  {Colors.GREEN}Testes Aprovados           : {passaram}{Colors.END}")
    if falhas > 0:
        print(f"  {Colors.RED}Falhas (Failures)          : {falhas}{Colors.END}")
    if erros > 0:
        print(f"  {Colors.RED}Erros (Errors)             : {erros}{Colors.END}")
        
    sucesso = result.wasSuccessful()
    if sucesso:
        print(f"\n{Colors.BOLD}{Colors.GREEN}>>> TODOS OS TESTES PASSARAM COM 100% DE SUCESSO! <<<{Colors.END}\n")
    else:
        print(f"\n{Colors.BOLD}{Colors.RED}>>> ALGUNS TESTES FALHARAM. VERIFIQUE O LOG ACIMA. <<<{Colors.END}\n")
        
    return sucesso


if __name__ == "__main__":
    sucesso = executar_testes()
    sys.exit(0 if sucesso else 1)
