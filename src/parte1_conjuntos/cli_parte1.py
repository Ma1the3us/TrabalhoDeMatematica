"""
Interface de Linha de Comando (CLI) para a Parte 1: Teoria dos Conjuntos.
"""
from typing import Any, List
from src.parte1_conjuntos.manual_set import ManualSetOperations
from src.parte1_conjuntos.native_comparator import SetComparator
from src.utils.display import Colors, print_header, print_info, print_section, print_table
from src.utils.helpers import format_set, parse_set_input


CONCEITOS_OPERACOES = {
    "Conjunto A": "Conjunto de entrada A com elementos repetidos eliminados para garantir a unicidade matemática.",
    "Conjunto B": "Conjunto de entrada B com elementos repetidos eliminados.",
    "|A| (Cardinalidade de A)": "A cardinalidade (|A|) representa a quantidade total de elementos únicos pertencentes a A.",
    "|B| (Cardinalidade de B)": "A cardinalidade (|B|) representa a quantidade total de elementos únicos pertencentes a B.",
    "A ∪ B (União)": "A união representa a junção de dois conjuntos, ignorando os números repetidos e criando um conjunto que possui todos os elementos do conjunto A e B.",
    "A ∩ B (Interseção)": "A interseção representa os elementos comuns, ou seja, apenas os elementos que pertencem simultaneamente a A e a B. Se não houver elementos comuns, resulta no conjunto vazio (Ø).",
    "A - B (Diferença)": "A diferença (A - B) representa os elementos que pertencem exclusivamente a A e NÃO pertencem a B. A ordem dos conjuntos importa!",
    "B - A (Diferença)": "A diferença (B - A) representa os elementos que pertencem exclusivamente a B e NÃO pertencem a A.",
    "A Δ B (Diferença Simétrica)": "A diferença simétrica representa os elementos que pertencem a A ou a B, mas NÃO a ambos ao mesmo tempo ((A-B) ∪ (B-A)). É o 'OU exclusivo' (XOR) da teoria dos conjuntos.",
    "A ⊆ B (Inclusão/Subconjunto)": "A inclusão A ⊆ B indica que TODO elemento do conjunto A também está contido no conjunto B.",
    "A ⊂ B (Inclusão Própria)": "A inclusão própria A ⊂ B exige que A seja subconjunto de B e que B tenha pelo menos um elemento a mais que A (A ≠ B).",
    "Complemento de A em U": "O complemento relativo (U - A) representa todos os elementos do Universo U que NÃO pertencem ao conjunto A."
}


def exibir_resultado_comparado(nome_operacao: str, valor_manual: Any, valor_nativo: Any, valido: bool, explicacao: str = "") -> None:
    """Exibe o resultado com indicador visual de validação e texto didático explicando a operação."""
    status = f"{Colors.GREEN}[✓ VALIDADO]{Colors.END}" if valido else f"{Colors.RED}[✗ ERRO]{Colors.END}"
    
    rep_manual = format_set(valor_manual) if isinstance(valor_manual, list) else str(valor_manual)
    rep_nativo = format_set(valor_nativo) if isinstance(valor_nativo, set) else str(valor_nativo)
    
    texto_conceito = explicacao or CONCEITOS_OPERACOES.get(nome_operacao, "")
    
    print(f"  {Colors.BOLD}{nome_operacao:<32}{Colors.END}:")
    print(f"     -> Implementação Manual : {rep_manual}")
    print(f"     -> Solução Nativa (set) : {rep_nativo}  {status}")
    if texto_conceito:
        print(f"     {Colors.CYAN}📖 Conceito:{Colors.END} {texto_conceito}")


def executar_comparativo_completo(lista_a: List[Any], lista_b: List[Any], lista_u: List[Any] = None) -> None:
    """Executa e exibe toda a suíte de operações com conjuntos e suas explicações didáticas."""
    if lista_u is None:
        lista_u = list(range(1, 11))
        
    relatorio = SetComparator.comparar_todas(lista_a, lista_b, lista_u)
    
    print_section("Resultados das Operações (Manual vs Nativa)")
    for operacao, dados in relatorio.items():
        exibir_resultado_comparado(operacao, dados["manual"], dados["nativa"], dados["valido"])


def menu_parte1_interativo() -> None:
    """Menu interativo para exploração manual da Parte 1."""
    print_header("PARTE 1: TEORIA DOS CONJUNTOS", "Laboratório Prático - FATEC Osasco")
    
    print("Digite os elementos dos conjuntos separados por vírgula.")
    print("Exemplos: '1, 2, 2, 3, 4' ou 'rock, jazz, cinema' ou 'vazio' para conjunto vazio.\n")
    
    entrada_a = input(f"{Colors.BOLD}Informe o Conjunto A: {Colors.END}") or "1, 2, 2, 3, 4"
    entrada_b = input(f"{Colors.BOLD}Informe o Conjunto B: {Colors.END}") or "3, 4, 5, 6"
    entrada_u = input(f"{Colors.BOLD}Informe o Universo U (Enter para 1 a 10): {Colors.END}") or "1 a 10"
    
    conj_a = parse_set_input(entrada_a)
    conj_b = parse_set_input(entrada_b)
    conj_u = parse_set_input(entrada_u)
    
    while True:
        print_section("Menu de Operações")
        print("  1. Executar Todas as Operações (com Explicação Didática e Comparação)")
        print("  2. União (A ∪ B)")
        print("  3. Interseção (A ∩ B)")
        print("  4. Diferenças (A - B e B - A)")
        print("  5. Diferença Simétrica (A Δ B)")
        print("  6. Testar Pertinência (x ∈ A e x ∈ B)")
        print("  7. Testar Inclusão (A ⊆ B e A ⊂ B)")
        print("  8. Cardinalidade e Complemento em U")
        print("  9. Alterar Conjuntos A e B")
        print("  0. Voltar ao Menu Principal")
        
        opcao = input(f"\n{Colors.BOLD}Escolha uma opção: {Colors.END}").strip()
        
        if opcao == "0":
            break
        elif opcao == "1":
            executar_comparativo_completo(conj_a, conj_b, conj_u)
        elif opcao == "2":
            res_manual = ManualSetOperations.uniao(conj_a, conj_b)
            res_nativo = set(conj_a) | set(conj_b)
            exibir_resultado_comparado(
                "A ∪ B (União)",
                res_manual,
                res_nativo,
                set(res_manual) == res_nativo,
                explicacao="A união representa a junção de dois conjuntos ignorando os números repetidos e criando um conjunto que possui todos os elementos do conjunto A e B."
            )
        elif opcao == "3":
            res_manual = ManualSetOperations.intersecao(conj_a, conj_b)
            res_nativo = set(conj_a) & set(conj_b)
            exibir_resultado_comparado(
                "A ∩ B (Interseção)",
                res_manual,
                res_nativo,
                set(res_manual) == res_nativo,
                explicacao="A interseção representa os elementos comuns, ou seja, apenas os elementos que estão simultaneamente em A e em B. Se não houver elementos comuns, resulta no conjunto vazio (Ø)."
            )
        elif opcao == "4":
            res_manual_ab = ManualSetOperations.diferenca(conj_a, conj_b)
            res_nativo_ab = set(conj_a) - set(conj_b)
            exibir_resultado_comparado(
                "A - B",
                res_manual_ab,
                res_nativo_ab,
                set(res_manual_ab) == res_nativo_ab,
                explicacao="A diferença (A - B) representa os elementos que pertencem exclusivamente a A e NÃO pertencem a B. A ordem dos conjuntos importa!"
            )
            
            res_manual_ba = ManualSetOperations.diferenca(conj_b, conj_a)
            res_nativo_ba = set(conj_b) - set(conj_a)
            exibir_resultado_comparado(
                "B - A",
                res_manual_ba,
                res_nativo_ba,
                set(res_manual_ba) == res_nativo_ba,
                explicacao="A diferença (B - A) representa os elementos que pertencem exclusivamente a B e NÃO pertencem a A."
            )
        elif opcao == "5":
            res_manual = ManualSetOperations.diferenca_simetrica(conj_a, conj_b)
            res_nativo = set(conj_a) ^ set(conj_b)
            exibir_resultado_comparado(
                "A Δ B (Diferença Simétrica)",
                res_manual,
                res_nativo,
                set(res_manual) == res_nativo,
                explicacao="A diferença simétrica representa os elementos que pertencem a A ou a B, mas NÃO a ambos ao mesmo tempo ((A-B) ∪ (B-A)). É o 'OU exclusivo' (XOR) da teoria dos conjuntos."
            )
        elif opcao == "6":
            val_x = input(f"{Colors.BOLD}Digite o elemento x para testar pertinência: {Colors.END}").strip()
            elem: Any
            try:
                elem = int(val_x)
            except ValueError:
                elem = val_x
            pert_a_man = ManualSetOperations.pertence(elem, conj_a)
            pert_a_nat = elem in set(conj_a)
            exibir_resultado_comparado(
                f"{elem} ∈ A ?",
                pert_a_man,
                pert_a_nat,
                pert_a_man == pert_a_nat,
                explicacao="A pertinência (∈) avalia se um elemento individual pertence ou não a um determinado conjunto."
            )
            pert_b_man = ManualSetOperations.pertence(elem, conj_b)
            pert_b_nat = elem in set(conj_b)
            exibir_resultado_comparado(
                f"{elem} ∈ B ?",
                pert_b_man,
                pert_b_nat,
                pert_b_man == pert_b_nat,
                explicacao="A pertinência (∈) avalia se um elemento individual pertence ou não a um determinado conjunto."
            )
        elif opcao == "7":
            sub_ab_man = ManualSetOperations.subconjunto(conj_a, conj_b)
            sub_ab_nat = set(conj_a) <= set(conj_b)
            exibir_resultado_comparado(
                "A ⊆ B",
                sub_ab_man,
                sub_ab_nat,
                sub_ab_man == sub_ab_nat,
                explicacao="A inclusão (A ⊆ B) indica que TODO elemento do conjunto A também está presente no conjunto B."
            )
            
            subp_ab_man = ManualSetOperations.subconjunto_proprio(conj_a, conj_b)
            subp_ab_nat = set(conj_a) < set(conj_b)
            exibir_resultado_comparado(
                "A ⊂ B",
                subp_ab_man,
                subp_ab_nat,
                subp_ab_man == subp_ab_nat,
                explicacao="A inclusão própria (A ⊂ B) indica que A está contido em B e que B possui ao menos um elemento a mais que A (A ≠ B)."
            )
        elif opcao == "8":
            card_a = ManualSetOperations.cardinalidade(conj_a)
            card_b = ManualSetOperations.cardinalidade(conj_b)
            comp_a = ManualSetOperations.complemento(conj_a, conj_u)
            print_info("|A| (Cardinalidade de A)", f"{card_a}  (Quantidade de elementos únicos em A)")
            print_info("|B| (Cardinalidade de B)", f"{card_b}  (Quantidade de elementos únicos em B)")
            exibir_resultado_comparado(
                "Complemento de A em U",
                comp_a,
                set(conj_u) - set(conj_a),
                set(comp_a) == (set(conj_u) - set(conj_a)),
                explicacao="O complemento relativo (U - A) representa todos os elementos do conjunto Universo U que NÃO pertencem a A."
            )
        elif opcao == "9":
            entrada_a = input(f"{Colors.BOLD}Informe o novo Conjunto A: {Colors.END}")
            entrada_b = input(f"{Colors.BOLD}Informe o novo Conjunto B: {Colors.END}")
            conj_a = parse_set_input(entrada_a)
            conj_b = parse_set_input(entrada_b)
        else:
            print(f"{Colors.RED}Opção inválida!{Colors.END}")

