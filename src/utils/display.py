import sys
from typing import List, Tuple

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



class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def print_header(title: str, subtitle: str = "") -> None:
    """Imprime um cabeçalho estilizado de destaque."""
    width = 75
    border = "=" * width
    print(f"\n{Colors.BOLD}{Colors.CYAN}{border}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{title.center(width)}{Colors.END}")
    if subtitle:
        print(f"{Colors.CYAN}{subtitle.center(width)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{border}{Colors.END}\n")


def print_section(title: str) -> None:
    """Imprime uma seção intermediária."""
    width = 75
    print(f"\n{Colors.BOLD}{Colors.BLUE}--- {title} {'-' * max(2, width - len(title) - 6)}{Colors.END}")


def print_success(message: str) -> None:
    """Imprime mensagem de sucesso com validação."""
    print(f"{Colors.GREEN}[✓ SUCESSO]{Colors.END} {message}")


def print_info(label: str, value: str) -> None:
    """Imprime uma linha chave-valor formatada."""
    print(f"  {Colors.BOLD}{label:<30}{Colors.END}: {value}")


def print_table(headers: List[str], rows: List[List[str]], col_widths: List[int] = None) -> None:
    """Imprime uma tabela ASCII elegante."""
    if not col_widths:
        col_widths = []
        for i in range(len(headers)):
            max_len = len(headers[i])
            for row in rows:
                if i < len(row):
                    max_len = max(max_len, len(str(row[i])))
            col_widths.append(max_len + 2)
            
    header_line = "|".join(headers[i].center(col_widths[i]) for i in range(len(headers)))
    sep_line = "+".join("-" * col_widths[i] for i in range(len(headers)))
    
    print(f"+{sep_line}+")
    print(f"|{header_line}|")
    print(f"+{sep_line}+")
    for row in rows:
        row_str = "|".join(str(row[i]).center(col_widths[i]) if i < len(row) else " " * col_widths[i] for i in range(len(headers)))
        print(f"|{row_str}|")
    print(f"+{sep_line}+")
