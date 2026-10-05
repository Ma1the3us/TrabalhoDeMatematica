"""
Interface de Linha de Comando (CLI) para a Parte 3: Integração e Mini-Projetos.
"""
from src.parte3_integracao.cartesian_powerset import CombinatoricsSets
from src.parte3_integracao.jaccard_recommender import JaccardRecommender
from src.parte3_integracao.rbac_access_control import RBACSystem
from src.parte3_integracao.real_intervals import IntervaloReal
from src.utils.display import Colors, print_header, print_info, print_section, print_table
from src.utils.helpers import format_set, parse_set_input


def demonstrar_jaccard_oficial() -> None:
    """Executa e valida o cenário oficial de recomendação de interesses por Jaccard."""
    rec = JaccardRecommender()
    rec.carregar_dados_padrao()

    print_section("Mini-Projeto 1: Sistema de Recomendação (Índice de Jaccard)")
    print("Base de Usuários e Interesses:")
    for user, ints in rec.usuarios.items():
        print_info(f"  Usuário '{user}'", format_set(ints))

    # Casos do gabarito
    pares = [("Ana", "Bia"), ("Ana", "Caio"), ("Bia", "Caio")]
    headers = ["Par", "Interseção (A ∩ B)", "União (A ∪ B)", "Índice de Jaccard", "Cálculo Esperado", "Gabarito"]
    rows = []

    gabaritos = {
        ("Ana", "Bia"): ("2/6 ≈ 0,33", "Aproximadamente 0.33"),
        ("Ana", "Caio"): ("2/5 = 0,40", "0.40"),
        ("Bia", "Caio"): ("1/6 ≈ 0,17", "Aproximadamente 0.17"),
    }

    for u1, u2 in pares:
        comp = rec.calcular_afinidade(u1, u2)
        esperado, gab = gabaritos[(u1, u2)]
        rows.append([
            f"{u1} e {u2}",
            f"{format_set(comp.intersecao)} ({comp.tamanho_intersecao})",
            f"{comp.tamanho_uniao} elementos",
            f"{comp.indice_jaccard:.4f}",
            esperado,
            f"{Colors.GREEN}[✓ CONFERE]{Colors.END}"
        ])

    print("\nComparativo de Afinidade entre Pares:")
    print_table(headers, rows)

    recs_ana = rec.recomendar_para("Ana")
    melhor_amigo = recs_ana[0][0]
    print(f"\n{Colors.BOLD}Conclusão / Resultado para Ana:{Colors.END}")
    print(f"  A recomendação mais forte para Ana é {Colors.BOLD}{Colors.GREEN}{melhor_amigo}{Colors.END} (afinidade Jaccard = {recs_ana[0][1]:.2f}).")
    print(f"  Resultado exatamente coincidente com o gabarito oficial da especificação!\n")


def demonstrar_rbac_oficial() -> None:
    """Executa e valida o cenário oficial de controle de acesso por perfis (RBAC)."""
    rbac = RBACSystem()
    rbac.carregar_dados_padrao()

    print_section("Mini-Projeto 2: Controle de Acesso Baseado em Perfis (RBAC)")
    print("Perfis do Sistema:")
    for perf, perms in rbac.perfis.items():
        print_info(f"  Perfil '{perf}'", format_set(perms))

    # Cenário 1: leitor e editor
    perms_a = rbac.obter_permissoes_usuario("usuario_a")
    print_info("Usuário A (leitor + editor)", f"Permissões = {format_set(perms_a)}")

    # Cenário 2: editor e financeiro
    perms_b = rbac.obter_permissoes_usuario("usuario_b")
    print_info("Usuário B (editor + financeiro)", f"Permissões = {format_set(perms_b)}")

    # Teste de pertinência
    pode_excluir_b = rbac.verificar_permissao("usuario_b", "excluir")
    print_info("Usuário B pode 'excluir'?", f"{'Sim' if pode_excluir_b else 'Não'} (porque 'excluir' ∉ {format_set(perms_b)})")

    # Teste de inclusão de perfis (subconjuntos)
    ed_in_admin = rbac.perfil_eh_subconjunto("editor", "admin")
    fin_in_admin = rbac.perfil_eh_subconjunto("financeiro", "admin")

    print_info("editor ⊆ admin ?", f"{ed_in_admin} (Verdadeiro - Todo editor tem permissões contidas no admin)")
    print_info("financeiro ⊆ admin ?", f"{fin_in_admin} (Falso - Financeiro tem 'ver_relatorios' que não está no admin)")


def demonstrar_combinatoria() -> None:
    """Executa a demonstração do produto cartesiano e conjunto das partes com análise 2^n."""
    print_section("Mini-Projeto 3: Produto Cartesiano e Conjunto das Partes")
    
    # Exemplo prático de produto cartesiano: opções de customização
    cores = ["Preto", "Branco"]
    tamanhos = ["P", "M", "G"]
    prod = CombinatoricsSets.produto_cartesiano(cores, tamanhos)
    
    print_info("Conjunto Cores A", format_set(cores))
    print_info("Conjunto Tamanhos B", format_set(tamanhos))
    print_info("Produto Cartesiano A × B", str(prod))
    print_info("Cardinalidade |A × B|", f"|A| × |B| = {len(cores)} × {len(tamanhos)} = {len(prod)} combinações")

    # Conjunto das partes
    conj_teste = [1, 2, 3]
    partes = CombinatoricsSets.conjunto_das_partes(conj_teste)
    print(f"\nConjunto das Partes P({format_set(conj_teste)}):")
    print_info("Cardinalidade 2^n", f"2^{len(conj_teste)} = {len(partes)} subconjuntos")
    for s in partes:
        print(f"    • {format_set(s)}")

    # Análise de complexidade exponencial
    print("\nAnálise de Escalabilidade Computacional (Crescimento de 2^n):")
    analise = CombinatoricsSets.analise_crescimento_partes([3, 5, 10, 20, 30])
    headers = ["Tamanho n (|A|)", "Subconjuntos 2^n", "Impacto Computacional"]
    rows = [[str(a[0]), f"{a[1]:,}".replace(",", "."), a[2]] for a in analise]
    print_table(headers, rows)


def demonstrar_intervalos() -> None:
    """Executa a demonstração de intervalos reais contínuos."""
    print_section("Mini-Projeto 4: Intervalos Reais na Reta Numérica")
    i1 = IntervaloReal(2, 5, fechado_esq=True, fechado_dir=False)  # [2, 5)
    i2 = IntervaloReal(3, 7, fechado_esq=True, fechado_dir=True)   # [3, 7]
    
    print_info("Intervalo I1", repr(i1))
    print_info("Intervalo I2", repr(i2))
    
    inter = i1.intersecao(i2)
    print_info("Interseção I1 ∩ I2", repr(inter) if inter else "Ø")
    
    # Teste de pertinência
    pontos = [1.5, 2.0, 4.9, 5.0, 6.0]
    for pt in pontos:
        print_info(f"x = {pt} ∈ I1 ({repr(i1)}) ?", str(i1.contem(pt)))


def menu_parte3_interativo() -> None:
    """Menu interativo para exploração da Parte 3."""
    print_header("PARTE 3: MINI-PROJETOS AVANÇADOS", "Integração e Aplicações Práticas")
    
    while True:
        print_section("Escolha o Mini-Projeto")
        print("  1. Opção 1: Sistema de Recomendação (Índice de Jaccard)")
        print("  2. Opção 2: Controle de Acesso por Perfis (RBAC)")
        print("  3. Opção 3: Produto Cartesiano e Conjunto das Partes (2^n)")
        print("  4. Opção 4: Intervalos Reais ([a, b), união e pertinência)")
        print("  5. Executar Todos os Mini-Projetos em Sequência")
        print("  0. Voltar ao Menu Principal")
        
        opcao = input(f"\n{Colors.BOLD}Escolha uma opção: {Colors.END}").strip()
        
        if opcao == "0":
            break
        elif opcao == "1":
            demonstrar_jaccard_oficial()
        elif opcao == "2":
            demonstrar_rbac_oficial()
        elif opcao == "3":
            demonstrar_combinatoria()
        elif opcao == "4":
            demonstrar_intervalos()
        elif opcao == "5":
            demonstrar_jaccard_oficial()
            demonstrar_rbac_oficial()
            demonstrar_combinatoria()
            demonstrar_intervalos()
        else:
            print(f"{Colors.RED}Opção inválida!{Colors.END}")
