"""
Interface de Linha de Comando (CLI) para a Parte 2: Conjuntos Numéricos.
"""
from src.parte2_numeros.classifier import NumberClassifier
from src.parte2_numeros.primes_divisors import crivo_eratostenes, listar_divisores
from src.utils.display import Colors, print_header, print_info, print_section, print_table


def exibir_resultado_classificacao(resultado) -> None:
    """Exibe a classificação detalhada de um número."""
    p = resultado.parsed
    print_section(f"Classificação Numérica: '{p.raw_input}'")
    
    print_info("Formato Identificado", p.kind.replace("_", " ").title())
    if p.kind == "dizima_periodica":
        print_info("Parte Inteira", str(p.parte_inteira))
        print_info("Parte Não Periódica", p.antiperiodo or "Nenhuma")
        print_info("Período", p.periodo)
        print_info("Fração Geratriz", resultado.fracao_geratriz)
    elif p.kind == "fracao":
        print_info("Fração Simplificada", resultado.fracao_geratriz)
    elif p.kind == "raiz":
        print_info("Radicando", str(p.radicando))
        print_info("Raiz Exata?", "Sim" if p.raiz_exata else "Não")
        print_info("Valor da Raiz", f"{p.valor_raiz:.6f}" if not p.raiz_exata else str(int(p.valor_raiz)))
        
    print_info("Pertence a", ", ".join(resultado.pertence))
    print_info("Não pertence a", ", ".join(resultado.nao_pertence))
    
    if p.observacao_especial:
        print_info("Observação", p.observacao_especial)
        
    print(f"\n  {Colors.BOLD}Justificativa Formal:{Colors.END}")
    for j in resultado.justificativas:
        print(f"    • {j}")


def executar_bateria_sugerida() -> None:
    """Executa a classificação completa para todos os 12 números da tabela oficial."""
    numeros_teste = [
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
    
    headers = ["Entrada", "Pertence a", "Não Pertence", "Geratriz / Valor", "Observação"]
    rows = []
    
    for num_str in numeros_teste:
        res = NumberClassifier.classificar(num_str)
        rows.append([
            num_str,
            ", ".join(res.pertence),
            ", ".join(res.nao_pertence),
            res.fracao_geratriz if res.parsed.kind != "raiz" else f"√{res.parsed.radicando}",
            res.parsed.observacao_especial
        ])
        
    print_section("Tabela de Resultados Oficiais - Parte 2")
    print_table(headers, rows)


def menu_parte2_interativo() -> None:
    """Menu interativo para exploração da Parte 2."""
    print_header("PARTE 2: CONJUNTOS NUMÉRICOS", "Classificador, Dízimas e Primos")
    
    while True:
        print_section("Menu de Opções")
        print("  1. Classificar um Número (Entrada Personalizada)")
        print("  2. Executar Tabela Oficial Completa (12 números da especificação)")
        print("  3. Bônus: Gerar Primos até n (Crivo de Eratóstenes)")
        print("  4. Bônus: Listar Divisores de um Número")
        print("  0. Voltar ao Menu Principal")
        
        opcao = input(f"\n{Colors.BOLD}Escolha uma opção: {Colors.END}").strip()
        
        if opcao == "0":
            break
        elif opcao == "1":
            print("\nExemplos válidos:")
            print("  - Inteiros: 7, -3, 0")
            print("  - Frações: 3/4, -5/2, 6/3")
            print("  - Decimais: 0.75 ou 0,75, -2.5")
            print("  - Dízimas periódicas: 0,(3), 2,(7), 1,2(5), 0,(9)")
            print("  - Raízes: V9, V2, sqrt(16), raiz(5)\n")
            entrada = input(f"{Colors.BOLD}Digite o número: {Colors.END}").strip()
            if entrada:
                try:
                    res = NumberClassifier.classificar(entrada)
                    exibir_resultado_classificacao(res)
                except Exception as err:
                    print(f"{Colors.RED}Erro ao processar: {err}{Colors.END}")
        elif opcao == "2":
            executar_bateria_sugerida()
        elif opcao == "3":
            entrada_limite = input(f"{Colors.BOLD}Gerar primos até qual número? (Padrão 30): {Colors.END}").strip() or "30"
            try:
                lim = int(entrada_limite)
                primos = crivo_eratostenes(lim)
                print_section(f"Primos até {lim} (Crivo de Eratóstenes)")
                print(f"  Total encontrado: {len(primos)}")
                print(f"  Primos: {', '.join(str(p) for p in primos)}")
            except ValueError:
                print(f"{Colors.RED}Digite um número inteiro válido!{Colors.END}")
        elif opcao == "4":
            entrada_num = input(f"{Colors.BOLD}Listar divisores de qual número? (Padrão 36): {Colors.END}").strip() or "36"
            try:
                val = int(entrada_num)
                divs = listar_divisores(val)
                print_section(f"Divisores inteiros positivos de {val}")
                print(f"  Quantidade de divisores: {len(divs)}")
                print(f"  Divisores: {', '.join(str(d) for d in divs)}")
            except ValueError:
                print(f"{Colors.RED}Digite um número inteiro válido!{Colors.END}")
        else:
            print(f"{Colors.RED}Opção inválida!{Colors.END}")
