# Laboratório de Conjuntos e Conjuntos Numéricos
> **Atividade Prática:** Teoria dos Conjuntos e Conjuntos Numéricos  
> **Instituição:** Fatec Osasco  
> **Curso:** Desenvolvimento de Software Multiplataforma (DSM)  
> **Linguagem:** Python 3 (100% Standard Library - Sem necessidade de instalar pacotes externos)

---

## 📌 Sumário
1. [Visão Geral do Projeto](#-visão-geral-do-projeto)
2. [Convenção Matemática Adotada ($\mathbb{N}$ e o Zero)](#-convenção-matemática-adotada-mathbbn-e-o-zero)
3. [Arquitetura e Decisões de Design](#-arquitetura-e-decisões-de-design)
4. [Estrutura de Pastas e Módulos](#-estrutura-de-pastas-e-módulos)
5. [Como Executar o Projeto](#-como-executar-o-projeto)
6. [Demonstrações e Logs de Execução](#-demonstrações-e-logs-de-execução)
   - [Parte 1: Teoria dos Conjuntos](#parte-1-teoria-dos-conjuntos-básico)
   - [Parte 2: Conjuntos Numéricos](#parte-2-conjuntos-numéricos-intermediário)
   - [Parte 3: Mini-Projetos de Integração](#parte-3-integração-avançado)
7. [Suíte de Testes Automatizados](#-suíte-de-testes-automatizados)
8. [Relatório de 1 Página](#-relatório-de-1-página)

---

## 🚀 Visão Geral do Projeto

Este projeto foi desenvolvido como instrumento prático para demonstrar a aplicação da **Teoria dos Conjuntos** e dos **Conjuntos Numéricos** na resolução de problemas reais de programação.

O software contempla todos os três níveis exigidos no programa acadêmico:
- **Parte 1 (Básico):** Operações fundamentais de conjuntos implementadas artesanalmente (com laços e condicionais puros, sem operadores nativos de conjuntos), validadas e comparadas automaticamente contra a solução nativa do Python (`set`).
- **Parte 2 (Intermediário):** Classificador numérico com identificação de inteiros, frações, decimais exatos, raízes e dízimas periódicas simples e compostas, incluindo dedução algébrica de fração geratriz, além de Crivo de Eratóstenes e listagem de divisores.
- **Parte 3 (Avançado):** Implementação completa dos 4 mini-projetos propostos:
  1. *Sistema de recomendação simples* baseado no Coeficiente de Similaridade de Jaccard;
  2. *Controle de acesso por perfis (RBAC)* com verificação de direitos via união e pertinência;
  3. *Produto cartesiano e Conjunto das Partes ($\mathcal{P}(A)$)* com análise do crescimento exponencial ($2^n$);
  4. *Intervalos reais na reta numérica* ($[a, b)$) com operações de pertinência e interseção.

---

## 📐 Convenção Matemática Adotada ($\mathbb{N}$ e o Zero)

> [!NOTE]
> **Definição Adotada:**  
> Neste projeto, adota-se a convenção de que **o número zero pertence ao conjunto dos Números Naturais ($\mathbb{N}$)**:
> $$\mathbb{N} = \{0, 1, 2, 3, 4, \dots\}$$
> $$\mathbb{N}^* = \{1, 2, 3, 4, \dots\} \quad (\text{Naturais não nulos})$$
>
> **Fundamentação:**  
> Esta convenção está em plena consonância com a norma internacional **ISO 80000-2**, com a **Base Nacional Comum Curricular (BNCC)** e com os padrões da Teoria Axiomática dos Conjuntos de Zermelo-Fraenkel (onde o zero representa a cardinalidade do conjunto vazio, $|\emptyset| = 0$).  
> Portanto, o número `0` é formalmente classificado como pertencente a $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$.

---

## 🏛 Arquitetura e Decisões de Design

1. **Zero Dependências Obrigatórias (Standard Library First):**  
   Todo o código foi construído utilizando exclusivamente os módulos nativos do Python (`math`, `re`, `typing`, `dataclasses`, `unittest`, `sys`, `os`). Não é necessário instalar nenhuma biblioteca externa via `pip` para rodar o menu interativo, as demonstrações ou a suíte de testes.
2. **Separação Estrita de Responsabilidades (Clean Architecture):**  
   - A lógica matemática manual (`manual_set.py`) é completamente desacoplada da CLI e dos utilitários.
   - O validador (`native_comparator.py`) atua como oráculo de teste em tempo de execução, garantindo que o resultado manual seja idêntico ao do interpretador nativo.
3. **Resiliência de Entrada (Parser Inteligente):**  
   O analisador aceita entradas nos formatos tradicionais da matemática e computação:
   - Notação de dízimas periódicas com parênteses: `1,2(5)`, `0,(3)`, `2,(7)`, `0,(9)`.
   - Raízes quadradas: `V9`, `v9`, `sqrt(9)`, `raiz(9)`, `√9`, `V2`.
   - Frações e decimais com vírgula ou ponto: `3/4`, `-5/2`, `0,75`, `0.75`.
   - Conjuntos com chaves, separados por vírgula, espaços ou intervalos: `{1, 2, 3}`, `1 a 10`, `vazio`, `Ø`.
4. **Logs Duplos Simultâneos:**  
   O executor de demonstrações (`run_demos.py`) exibe o output formatado com cores no terminal e, ao mesmo tempo, gera arquivos de texto puro na pasta `logs/` para auditoria e entrega.

---

## 📂 Estrutura de Pastas e Módulos

```text
trabalhoDeMatemativca/
│
├── main.py                     # Ponto de entrada CLI interativo completo
├── run_demos.py                # Executa todas as demonstrações e gera logs
├── run_tests.py                # Runner automatizado de testes unitários (25 testes)
├── README.md                   # Documentação técnica e gabaritos
├── RELATORIO.md                # Relatório acadêmico de 1 página
├── requirements.txt            # Dependências opcionais de desenvolvimento
├── .gitignore                  # Regras de exclusão do Git
├── ComoInstalarPython.md       # Guia rápido de instalação do Python
│
├── src/                        # Código-fonte modular
│   ├── __init__.py
│   ├── parte1_conjuntos/       # Módulo da Parte 1
│   │   ├── __init__.py
│   │   ├── manual_set.py       # Operações com laços e condicionais puros
│   │   ├── native_comparator.py# Comparação com operadores nativos (set)
│   │   └── cli_parte1.py       # Menu e exibição da Parte 1
│   │
│   ├── parte2_numeros/         # Módulo da Parte 2
│   │   ├── __init__.py
│   │   ├── generator_fraction.py# Algoritmo de fração geratriz e simplificação MDC
│   │   ├── parser.py           # Parser regex para raízes, frações e dízimas
│   │   ├── classifier.py       # Classificador em N, Z, Q, I, R com justificativas
│   │   ├── primes_divisors.py  # Crivo de Eratóstenes e divisores
│   │   └── cli_parte2.py       # Menu e exibição da Parte 2
│   │
│   ├── parte3_integracao/      # Módulo da Parte 3 (Mini-Projetos)
│   │   ├── __init__.py
│   │   ├── jaccard_recommender.py # Opção 1: Similaridade de Jaccard
│   │   ├── rbac_access_control.py # Opção 2: Controle de Acesso por Perfis
│   │   ├── cartesian_powerset.py  # Opção 3: Produto Cartesiano e 2^n
│   │   ├── real_intervals.py      # Opção 4: Intervalos Reais na Reta
│   │   └── cli_parte3.py          # Menu e demonstração dos mini-projetos
│   │
│   └── utils/                  # Utilitários gerais
│       ├── __init__.py
│       ├── display.py          # Formatação de cabeçalhos e tabelas no console
│       └── helpers.py          # Conversão de strings de conjuntos e formatação
│
├── tests/                      # Casos de Teste Unitários (unittest)
│   ├── __init__.py
│   ├── test_parte1.py          # Testes de conjuntos e casos de borda
│   ├── test_parte2.py          # Testes de classificação dos 12 números e bônus
│   └── test_parte3.py          # Testes de Jaccard, RBAC, partes e intervalos
│
└── logs/                       # Logs gravados das execuções
    ├── execucao_parte1.txt
    ├── execucao_parte2.txt
    ├── execucao_parte3.txt
    ├── execucao_completa.txt
    └── testes_unitarios.txt
```

---

## 💻 Como Executar o Projeto

### Pré-requisitos
Ter o Python 3.8+ instalado na máquina.  
*(Caso precise instalar, consulte o guia passo a passo em [ComoInstalarPython.md](ComoInstalarPython.md)).*

### 1. Executar o Menu Interativo Completo
Abra o terminal na pasta do projeto e digite:
```powershell
python main.py
```
Você verá o menu principal:
```
===========================================================================
               LABORATÓRIO DE CONJUNTOS E CONJUNTOS NUMÉRICOS              
          FATEC Osasco - Desenvolvimento de Software Multiplataforma       
===========================================================================

  1. Parte 1: Teoria dos Conjuntos (Básico: Operações Manuais vs Nativas)
  2. Parte 2: Conjuntos Numéricos (Intermediário: Classificador e Dízimas)
  3. Parte 3: Mini-Projetos de Integração (Avançado: Jaccard, RBAC, etc.)
  4. Executar Bateria Completa de Demonstrações (Gerar Logs)
  5. Executar Testes Unitários Automatizados
  0. Sair do Programa
```

### 2. Executar as Demonstrações Oficiais e Gerar Todos os Logs
```powershell
python run_demos.py
```

### 3. Rodar a Suíte de Testes Automatizados
```powershell
python run_tests.py
```
*(Ou, se tiver o `pytest` instalado: `pytest -v`).*

---

## 📊 Demonstrações e Logs de Execução

### Parte 1: Teoria dos Conjuntos (Básico)

#### Exemplo 1: Caso Geral (com descarte de repetidos)
- **Entrada:**
  - $A = 1, 2, 2, 3, 4 \implies A = \{1, 2, 3, 4\}$ (duplicatas descartadas)
  - $B = 3, 4, 5, 6 \implies B = \{3, 4, 5, 6\}$
  - $U = 1 \text{ a } 10 \implies U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$

| Operação | Implementação Manual | Solução Nativa (`set`) | Validação |
| :--- | :---: | :---: | :---: |
| **Cardinalidade $|A|$** | `4` | `4` | `[✓ VALIDADO]` |
| **Cardinalidade $|B|$** | `4` | `4` | `[✓ VALIDADO]` |
| **União $A \cup B$** | `{1, 2, 3, 4, 5, 6}` | `{1, 2, 3, 4, 5, 6}` | `[✓ VALIDADO]` |
| **Interseção $A \cap B$** | `{3, 4}` | `{3, 4}` | `[✓ VALIDADO]` |
| **Diferença $A - B$** | `{1, 2}` | `{1, 2}` | `[✓ VALIDADO]` |
| **Diferença $B - A$** | `{5, 6}` | `{5, 6}` | `[✓ VALIDADO]` |
| **Diferença Simétrica $A \ \Delta \ B$** | `{1, 2, 5, 6}` | `{1, 2, 5, 6}` | `[✓ VALIDADO]` |
| **Complemento de $A$ em $U$** | `{5, 6, 7, 8, 9, 10}` | `{5, 6, 7, 8, 9, 10}` | `[✓ VALIDADO]` |
| **Pertinência $3 \in A$** | `True` | `True` | `[✓ VALIDADO]` |
| **Pertinência $5 \in A$** | `False` | `False` | `[✓ VALIDADO]` |
| **Inclusão $\{3, 4\} \subseteq A$** | `True` | `True` | `[✓ VALIDADO]` |
| **Inclusão Própria $\{3, 4\} \subset A$**| `True` | `True` | `[✓ VALIDADO]` |

#### Exemplo 2: Casos de Borda da Especificação

| Situação | Entrada | Resultado Esperado | Resultado Obtido | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Conjunto Vazio** | $A = \emptyset, B = \{1, 2\}$ | $A \cup B = \{1, 2\}$; $A \cap B = \emptyset$; $A \subseteq B$ é True | $A \cup B = \{1, 2\}$; $A \cap B = \emptyset$; $A \subseteq B = \text{True}$ | `[✓ CONFERE]` |
| **Conjuntos Iguais** | $A = B = \{1, 2, 3\}$ | $A - B = \emptyset$; $A \ \Delta \ B = \emptyset$; $A \subseteq B$ é True; $A \subset B$ é False | $A - B = \emptyset$; $A \ \Delta \ B = \emptyset$; $A \subseteq B = \text{True}$; $A \subset B = \text{False}$ | `[✓ CONFERE]` |
| **Conjuntos Disjuntos** | $A = \{1, 2\}, B = \{3, 4\}$ | $A \cap B = \emptyset$; $A \cup B = \{1, 2, 3, 4\}$; $A \ \Delta \ B = \{1, 2, 3, 4\}$ | $A \cap B = \emptyset$; $A \cup B = \{1, 2, 3, 4\}$; $A \ \Delta \ B = \{1, 2, 3, 4\}$ | `[✓ CONFERE]` |
| **Um Contido no Outro** | $A = \{1, 2\}, B = \{1, 2, 3\}$ | $A \subset B$ é True; $B \subseteq A$ é False; $B - A = \{3\}$ | $A \subset B = \text{True}$; $B \subseteq A = \text{False}$; $B - A = \{3\}$ | `[✓ CONFERE]` |
| **Repetidos na Entrada**| $A = 1, 1, 1, 2$ | $A = \{1, 2\}$; $\|A\| = 2$ | $A = \{1, 2\}$; $\|A\| = 2$ | `[✓ CONFERE]` |

#### Exemplo 3: Exemplo Próprio da Equipe
- **Contexto:** Habilidades técnicas dominadas por dois times de desenvolvimento:
  - Time Web ($A$): `{Python, TypeScript, React, Docker, SQL}`
  - Time Mobile ($B$): `{Kotlin, TypeScript, Flutter, Docker, Firebase}`
  - Universo das Tecnologias ($U$): Todas acima mais `{Rust, Go}`
- **Resultados:**
  - $A \cap B = \{\text{Docker, TypeScript}\}$ (competências compartilhadas)
  - $A - B = \{\text{Python, React, SQL}\}$ (exclusivas do Web)
  - $B - A = \{\text{Firebase, Flutter, Kotlin}\}$ (exclusivas do Mobile)
  - $A \ \Delta \ B = \{\text{Firebase, Flutter, Kotlin, Python, React, SQL}\}$
  - $A^c = \{\text{Firebase, Flutter, Go, Kotlin, Rust}\}$

---

### Parte 2: Conjuntos Numéricos (Intermediário)

Todos os 12 números sugeridos na especificação foram classificados com identificação de tipo, cálculo da fração geratriz e justificativa teórica:

| Entrada | Pertence a | Não Pertence | Fração Geratriz / Simplificada | Justificativa Teórica |
| :---: | :---: | :---: | :---: | :--- |
| **7** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{I}$ | $7/1$ | Inteiro não-negativo ($\ge 0$). |
| **-3** | $\mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{I}$ | $-3/1$ | Inteiro estritamente negativo ($< 0$). |
| **0** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{I}$ | $0/1$ | Zero pertence a $\mathbb{N}$ segundo convenção adotada. |
| **3/4** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{I}$ | $3/4 = 0{,}75$ | Fração irredutível; decimal finito exato. |
| **-5/2** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{I}$ | $-5/2 = -2{,}5$ | Fração irredutível negativa. |
| **6/3** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{I}$ | $6/3 = 2/1 = 2$ | Fração aparente que simplifica para o natural $2$. |
| **0,(3)** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{I}$ | $\frac{3-0}{9} = \mathbf{1/3}$ | Dízima periódica simples (período 3). |
| **2,(7)** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{I}$ | $\frac{27-2}{9} = \mathbf{25/9}$ | Dízima periódica simples com parte inteira. |
| **1,2(5)** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{I}$ | $\frac{125-12}{90} = \mathbf{113/90}$ | Dízima periódica composta (antiperíodo 2, período 5). |
| **0,(9)** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{I}$ | $\frac{9-0}{9} = \mathbf{9/9 = 1}$ | Caso clássico de dízima cuja geratriz é $1 \in \mathbb{N}$. |
| **V9** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{I}$ | $\sqrt{9} = \mathbf{3}$ | Raiz exata (quadrado perfeito $3^2 = 9$). |
| **V2** | $\mathbb{I}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}$ | $\sqrt{2} \approx 1{,}414214$ | Raiz não exata; dízima não periódica irracional. |

#### Bônus da Parte 2
- **Crivo de Eratóstenes até 30:**
  `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]` *(Gabarito conferido: 10 números primos).*
- **Divisores Positivos de 36:**
  `[1, 2, 3, 4, 6, 9, 12, 18, 36]` *(Gabarito conferido: 9 divisores).*

---

### Parte 3: Integração (Avançado)

#### Opção 1: Sistema de Recomendação Simples (Índice de Jaccard)
Fórmula de afinidade:
$$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$

- **Perfis de Interesses:**
  - **Ana:** `{rock, jazz, cinema, games}`
  - **Bia:** `{jazz, cinema, séries, viagens}`
  - **Caio:** `{games, tecnologia, cinema}`

- **Comparação entre os Pares:**

| Par | Interseção ($A \cap B$) | União ($A \cup B$) | Índice de Jaccard ($J$) | Gabarito Esperado | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Ana e Bia** | `{cinema, jazz}` ($2$) | $6$ elementos | **$0{,}3333$** | $2/6 \approx 0{,}33$ | `[✓ CONFERE]` |
| **Ana e Caio** | `{cinema, games}` ($2$)| $5$ elementos | **$0{,}4000$** | $2/5 = 0{,}40$ | `[✓ CONFERE]` |
| **Bia e Caio** | `{cinema}` ($1$) | $6$ elementos | **$0{,}1667$** | $1/6 \approx 0{,}17$ | `[✓ CONFERE]` |

> **Resultado Final para Ana:**  
> A recomendação mais forte para a Ana é o **Caio** ($J = 0{,}40$), exatamente como exigido no gabarito oficial.

---

#### Opção 2: Controle de Acesso por Perfis (RBAC)
- **Perfis:**
  - `leitor = {ler}`
  - `editor = {ler, editar}`
  - `admin = {ler, editar, excluir, gerir_usuarios}`
  - `financeiro = {ver_relatorios}`
- **Cenários Testados:**
  1. Usuário com perfis `leitor` e `editor` $\implies$ Permissões efetivas por união = `{ler, editar}`.
  2. Usuário com perfis `editor` e `financeiro` $\implies$ Permissões = `{ler, editar, ver_relatorios}`.
  3. Esse usuário pode excluir? **Não**, pois $\text{excluir} \notin \{\text{ler, editar, ver_relatorios}\}$.
  4. Relações de Inclusão:
     - $\text{editor} \subseteq \text{admin} \implies$ **Verdadeiro** (`True`).
     - $\text{financeiro} \subseteq \text{admin} \implies$ **Falso** (`False`).

---

#### Opção 3: Produto Cartesiano e Conjunto das Partes ($\mathcal{P}(A)$)
- **Produto Cartesiano:**
  $$\{\text{P, M}\} \times \{\text{Azul, Vermelho}\} = \{(\text{P, Azul}), (\text{P, Vermelho}), (\text{M, Azul}), (\text{M, Vermelho})\}$$
  Cardinalidade: $2 \times 2 = 4$.
- **Conjunto das Partes:**
  $$\mathcal{P}(\{1, 2, 3\}) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}, \{3\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}$$
  Cardinalidade: $2^3 = 8$ subconjuntos.
- **Discussão de Complexidade:**  
  Para $n$ elementos, a geração possui complexidade de tempo e espaço de ordem $\mathcal{O}(2^n)$. Para $n=30$, seriam $1{,}07 \times 10^9$ subconjuntos, evidenciando a barreira intransponível da explosão combinatória na ausência de heurísticas.

---

#### Opção 4: Intervalos Reais na Reta Numérica
- Intervalo $I_1 = [2, 5)$
- Intervalo $I_2 = [3, 7]$
- **Interseção:** $I_1 \cap I_2 = [3, 5)$
- **Pertinência em $I_1$:**
  - $x = 2{,}0 \in [2, 5) \implies \text{True}$ (extremidade esquerda fechada).
  - $x = 4{,}999 \in [2, 5) \implies \text{True}$.
  - $x = 5{,}0 \in [2, 5) \implies \text{False}$ (extremidade direita aberta).

---

## 🧪 Suíte de Testes Automatizados

O projeto conta com **25 testes unitários** automatizados cobrindo todos os módulos:
- `test_parte1.py`: Casos de borda (vazio, iguais, disjuntos, contido, repetidos) e validação manual vs nativa.
- `test_parte2.py`: Todos os 12 números de exemplo da tabela do professor, frações geratrizes, Crivo de Eratóstenes e divisores.
- `test_parte3.py`: Validação numérica de Jaccard, permissões de RBAC, conjunto das partes e intervalos contínuos.

Para rodar todos os testes:
```powershell
python run_tests.py
```
**Resultado obtido:**
```
Ran 25 tests in 0.018s
OK - 100% dos testes aprovados com zero falhas e zero erros.
```

---

## 📄 Relatório de 1 Página

O relatório acadêmico de 1 página exigido nas instruções encontra-se redigido no arquivo [`RELATORIO.md`](RELATORIO.md), respondendo com rigor formal às questões:
1. *Onde a teoria dos conjuntos apareceu no código?*
2. *Qual operação foi mais difícil de implementar e por quê?*

---

## 👥 Equipe do Projeto
- **Curso:** Desenvolvimento de Software Multiplataforma (DSM)
- **Fatec Osasco**
