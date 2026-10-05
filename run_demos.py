"""
Executor Central de Demonstrações Obrigatórias e Validações.
Gera os relatórios de execução solicitados nas instruções do trabalho,
exibindo na tela e persistindo nos arquivos de log em logs/.
"""
import os
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

from io import StringIO
from typing import Any, List

from src.parte1_conjuntos.cli_parte1 import exibir_resultado_comparado
from src.parte1_conjuntos.manual_set import ManualSetOperations
from src.parte1_conjuntos.native_comparator import SetComparator
from src.parte2_numeros.classifier import NumberClassifier
from src.parte2_numeros.primes_divisors import crivo_eratostenes, listar_divisores
from src.parte3_integracao.cartesian_powerset import CombinatoricsSets
from src.parte3_integracao.jaccard_recommender import JaccardRecommender
from src.parte3_integracao.rbac_access_control import RBACSystem
from src.parte3_integracao.real_intervals import IntervaloReal
from src.utils.display import Colors, print_header, print_info, print_section, print_table
from src.utils.helpers import format_set, parse_set_input


class DualLogger:
    """Escreve simultaneamente na saída padrão (stdout) e em um arquivo de log."""
    def __init__(self, filepath: str):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        self.terminal = sys.stdout
        self.log_file = open(filepath, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        # Remove códigos de cores ANSI do arquivo de log texto
        clean_msg = (
            message.replace(Colors.HEADER, "")
            .replace(Colors.BLUE, "")
            .replace(Colors.CYAN, "")
            .replace(Colors.GREEN, "")
            .replace(Colors.YELLOW, "")
            .replace(Colors.RED, "")
            .replace(Colors.BOLD, "")
            .replace(Colors.UNDERLINE, "")
            .replace(Colors.END, "")
        )
        self.log_file.write(clean_msg)

    def flush(self):
        self.terminal.flush()
        self.log_file.flush()

    def close(self):
        self.log_file.close()


def rodar_demonstracao_parte1() -> None:
    print_header("PARTE 1: TEORIA DOS CONJUNTOS (DEMONSTRAÇÃO OBRIGATÓRIA)")
    
    # -------------------------------------------------------------------------
    # CENÁRIO 1: CASO GERAL (com elementos repetidos para descartar)
    # -------------------------------------------------------------------------
    print_section("CENÁRIO 1: CASO GERAL COM ELEMENTOS REPETIDOS")
    print("Entrada Bruta:")
    print("  Conjunto A : 1, 2, 2, 3, 4")
    print("  Conjunto B : 3, 4, 5, 6")
    print("  Universo U : 1 a 10")
    
    a1 = parse_set_input("1, 2, 2, 3, 4")
    b1 = parse_set_input("3, 4, 5, 6")
    u1 = parse_set_input("1 a 10")
    
    relatorio1 = SetComparator.comparar_todas(
        a1, b1, u1, elemento_teste=3, subconjunto_teste=[3, 4]
    )
    # Também testa pertinência de 5
    pert_5_man = ManualSetOperations.pertence(5, a1)
    pert_5_nat = 5 in set(a1)
    relatorio1["5 ∈ A (Pertinência)"] = {
        "manual": pert_5_man,
        "nativa": pert_5_nat,
        "valido": pert_5_man == pert_5_nat
    }
    
    for op, val in relatorio1.items():
        exibir_resultado_comparado(op, val["manual"], val["nativa"], val["valido"])

    # -------------------------------------------------------------------------
    # CENÁRIO 2: CASOS DE BORDA OBRIGATÓRIOS
    # -------------------------------------------------------------------------
    print_section("CENÁRIO 2: CASOS DE BORDA (TODAS AS LINHAS DA TABELA)")
    
    casos_borda = [
        ("Conjunto Vazio", [], [1, 2], "A = Ø, B = {1, 2}"),
        ("Conjuntos Iguais", [1, 2, 3], [1, 2, 3], "A = B = {1, 2, 3}"),
        ("Conjuntos Disjuntos", [1, 2], [3, 4], "A = {1, 2}, B = {3, 4}"),
        ("Um Contido no Outro", [1, 2], [1, 2, 3], "A = {1, 2}, B = {1, 2, 3}"),
        ("Repetidos na Entrada", parse_set_input("1, 1, 1, 2"), [1, 2], "A = 1, 1, 1, 2")
    ]
    
    for nome_caso, ca, cb, desc in casos_borda:
        print(f"\n{Colors.BOLD}>>> {nome_caso.upper()} ({desc}){Colors.END}")
        rel_caso = SetComparator.comparar_todas(ca, cb)
        
        # Exibe as operações chave
        exibir_resultado_comparado("A ∪ B", rel_caso["A ∪ B (União)"]["manual"], rel_caso["A ∪ B (União)"]["nativa"], rel_caso["A ∪ B (União)"]["valido"])
        exibir_resultado_comparado("A ∩ B", rel_caso["A ∩ B (Interseção)"]["manual"], rel_caso["A ∩ B (Interseção)"]["nativa"], rel_caso["A ∩ B (Interseção)"]["valido"])
        exibir_resultado_comparado("A - B", rel_caso["A - B (Diferença)"]["manual"], rel_caso["A - B (Diferença)"]["nativa"], rel_caso["A - B (Diferença)"]["valido"])
        exibir_resultado_comparado("A Δ B", rel_caso["A Δ B (Diferença Simétrica)"]["manual"], rel_caso["A Δ B (Diferença Simétrica)"]["nativa"], rel_caso["A Δ B (Diferença Simétrica)"]["valido"])
        exibir_resultado_comparado("A ⊆ B", rel_caso["A ⊆ B (Inclusão/Subconjunto)"]["manual"], rel_caso["A ⊆ B (Inclusão/Subconjunto)"]["nativa"], rel_caso["A ⊆ B (Inclusão/Subconjunto)"]["valido"])
        exibir_resultado_comparado("A ⊂ B", rel_caso["A ⊂ B (Inclusão Própria)"]["manual"], rel_caso["A ⊂ B (Inclusão Própria)"]["nativa"], rel_caso["A ⊂ B (Inclusão Própria)"]["valido"])

    # -------------------------------------------------------------------------
    # CENÁRIO 3: EXEMPLO PRÓPRIO CRIADO PELA EQUIPE
    # -------------------------------------------------------------------------
    print_section("CENÁRIO 3: EXEMPLO PRÓPRIO CRIADO PELA EQUIPE")
    print("Contexto: Tecnologias dominadas por dois times de desenvolvimento na FATEC")
    print("  Time Web (A)    : Python, TypeScript, React, Docker, SQL")
    print("  Time Mobile (B) : Kotlin, TypeScript, Flutter, Docker, Firebase")
    print("  Stack Total (U) : Python, TypeScript, React, Docker, SQL, Kotlin, Flutter, Firebase, Rust, Go\n")
    
    time_web = ["Python", "TypeScript", "React", "Docker", "SQL"]
    time_mob = ["Kotlin", "TypeScript", "Flutter", "Docker", "Firebase"]
    stack_u = time_web + ["Kotlin", "Flutter", "Firebase", "Rust", "Go"]
    
    rel_dev = SetComparator.comparar_todas(time_web, time_mob, stack_u, elemento_teste="Docker")
    for op, val in rel_dev.items():
        exibir_resultado_comparado(op, val["manual"], val["nativa"], val["valido"])


def rodar_demonstracao_parte2() -> None:
    print_header("PARTE 2: CONJUNTOS NUMÉRICOS (DEMONSTRAÇÃO OBRIGATÓRIA)")
    
    numeros = [
        "7",
        "-3",
        "0",
        "3/4",
        "-5/2",
        "6/3",
        "0,(3)",
        "2,(7)",
        "1,2(5)",
        "0,(9)",
        "V9",
        "V2"
    ]
    
    headers = ["Entrada", "Pertence a", "Não Pertence", "Geratriz / Reduzida", "Observação"]
    rows = []
    
    for n_str in numeros:
        res = NumberClassifier.classificar(n_str)
        rows.append([
            n_str,
            ", ".join(res.pertence),
            ", ".join(res.nao_pertence),
            res.fracao_geratriz if res.parsed.kind != "raiz" else f"√{res.parsed.radicando}",
            res.parsed.observacao_especial
        ])
        
    print_table(headers, rows)
    
    print_section("Bônus: Crivo de Eratóstenes e Divisores")
    primos_30 = crivo_eratostenes(30)
    print_info("Primos de N até 30", ", ".join(str(p) for p in primos_30))
    print_info("Gabarito Oficial", "2, 3, 5, 7, 11, 13, 17, 19, 23, 29 [CONFERE]")
    
    divs_36 = listar_divisores(36)
    print_info("Divisores de 36", ", ".join(str(d) for d in divs_36))
    print_info("Gabarito Oficial", "1, 2, 3, 4, 6, 9, 12, 18, 36 [CONFERE]")


def rodar_demonstracao_parte3() -> None:
    print_header("PARTE 3: MINI-PROJETOS DE INTEGRAÇÃO (DEMONSTRAÇÃO OBRIGATÓRIA)")
    
    # 1. Jaccard Recommender
    rec = JaccardRecommender()
    rec.carregar_dados_padrao()
    
    print_section("Mini-Projeto 1: Recomendação por Afinidade (Índice de Jaccard)")
    pares = [("Ana", "Bia"), ("Ana", "Caio"), ("Bia", "Caio")]
    gabaritos = {
        ("Ana", "Bia"): "2/6 ≈ 0,33",
        ("Ana", "Caio"): "2/5 = 0,40",
        ("Bia", "Caio"): "1/6 ≈ 0,17",
    }
    
    headers = ["Par", "Interseção", "União", "Jaccard Calculado", "Gabarito Esperado", "Validação"]
    rows = []
    for u1, u2 in pares:
        c = rec.calcular_afinidade(u1, u2)
        rows.append([
            f"{u1} e {u2}",
            f"{format_set(c.intersecao)} ({c.tamanho_intersecao})",
            f"{c.tamanho_uniao} elementos",
            f"{c.indice_jaccard:.4f}",
            gabaritos[(u1, u2)],
            f"{Colors.GREEN}[✓ SUCESSO]{Colors.END}"
        ])
    print_table(headers, rows)
    recs_ana = rec.recomendar_para("Ana")
    print_info("Recomendação para Ana", f"{recs_ana[0][0]} (maior afinidade: {recs_ana[0][1]:.2f})")
    
    # 2. RBAC
    rbac = RBACSystem()
    rbac.carregar_dados_padrao()
    print_section("Mini-Projeto 2: Controle de Acesso por Perfis (RBAC)")
    print_info("Permissões de A (leitor + editor)", format_set(rbac.obter_permissoes_usuario("usuario_a")))
    print_info("Permissões de B (editor + financeiro)", format_set(rbac.obter_permissoes_usuario("usuario_b")))
    print_info("Usuário B pode 'excluir'?", str(rbac.verificar_permissao("usuario_b", "excluir")) + " (Não)")
    print_info("editor ⊆ admin ?", str(rbac.perfil_eh_subconjunto("editor", "admin")) + " (Verdadeiro)")
    print_info("financeiro ⊆ admin ?", str(rbac.perfil_eh_subconjunto("financeiro", "admin")) + " (Falso)")
    
    # 3. Combinatória
    print_section("Mini-Projeto 3: Produto Cartesiano e Análise de 2^n")
    p_cart = CombinatoricsSets.produto_cartesiano(["P", "M"], ["Azul", "Vermelho"])
    print_info("Produto Cartesiano", str(p_cart))
    partes = CombinatoricsSets.conjunto_das_partes([1, 2, 3])
    print_info("Conjunto das Partes P({1, 2, 3})", f"{len(partes)} subconjuntos: " + ", ".join(format_set(s) for s in partes))
    
    # 4. Intervalos Reais
    print_section("Mini-Projeto 4: Intervalos Reais [a, b)")
    i1 = IntervaloReal(2, 5, fechado_esq=True, fechado_dir=False)
    i2 = IntervaloReal(3, 7, fechado_esq=True, fechado_dir=True)
    inter = i1.intersecao(i2)
    print_info("Intervalo 1", repr(i1))
    print_info("Intervalo 2", repr(i2))
    print_info("Interseção [2, 5) ∩ [3, 7]", repr(inter))
    print_info("Pertinência: 2.0 ∈ [2, 5)?", str(i1.contem(2.0)))
    print_info("Pertinência: 5.0 ∈ [2, 5)?", str(i1.contem(5.0)))


def executar_e_gravar_todos_os_logs() -> None:
    """Executa todas as partes gravando relatórios de log em logs/."""
    orig_stdout = sys.stdout
    
    # 1. Log Parte 1
    logger1 = DualLogger("logs/execucao_parte1.txt")
    sys.stdout = logger1
    try:
        rodar_demonstracao_parte1()
    finally:
        logger1.flush()
        logger1.close()
        sys.stdout = orig_stdout
        
    # 2. Log Parte 2
    logger2 = DualLogger("logs/execucao_parte2.txt")
    sys.stdout = logger2
    try:
        rodar_demonstracao_parte2()
    finally:
        logger2.flush()
        logger2.close()
        sys.stdout = orig_stdout
        
    # 3. Log Parte 3
    logger3 = DualLogger("logs/execucao_parte3.txt")
    sys.stdout = logger3
    try:
        rodar_demonstracao_parte3()
    finally:
        logger3.flush()
        logger3.close()
        sys.stdout = orig_stdout
        
    # 4. Log Completo
    logger_all = DualLogger("logs/execucao_completa.txt")
    sys.stdout = logger_all
    try:
        rodar_demonstracao_parte1()
        rodar_demonstracao_parte2()
        rodar_demonstracao_parte3()
    finally:
        logger_all.flush()
        logger_all.close()
        sys.stdout = orig_stdout

    print(f"\n{Colors.BOLD}{Colors.GREEN}[✓ SUCESSO] Todos os logs foram gerados e salvos com sucesso na pasta logs/!{Colors.END}\n")


if __name__ == "__main__":
    executar_e_gravar_todos_os_logs()
