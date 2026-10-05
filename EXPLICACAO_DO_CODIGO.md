# 📘 Explicação Técnica Completa do Código: Onde e Como as Operações São Realizadas

Este documento detalha **a arquitetura completa do projeto**, explicando em **qual arquivo e linha** cada operação matemática foi programada, **qual lógica algorítmica** foi utilizada e **como o código atende rigorosamente às exigências acadêmicas** da FATEC Osasco.

---

## 🗺️ 1. Mapa de Arquitetura do Projeto

```text
trabalhoDeMatemativca/
│
├── main.py                     # Ponto de entrada com menu interativo unificado
├── run_tests.py                # Runner nativo dos 25 testes automatizados (0% dependência externa)
├── run_demos.py                # Bateria oficial de testes que gera todos os relatórios e logs
├── executar.bat                # Launcher de 1 clique para Windows
├── COMO_RODAR.md               # Guia rápido de execução e roteiro de apresentação oral
├── EXPLICACAO_DO_CODIGO.md     # [ESTE ARQUIVO] Documentação técnica detalhada
├── RELATORIO.md                # Relatório acadêmico respondendo às duas questões centrais
│
├── src/
│   ├── parte1_conjuntos/       # Módulo da Teoria dos Conjuntos Pura
│   │   ├── manual_set.py       # [CRUCIAL] Operações manuais na raça (laços for e condicionais if)
│   │   ├── native_comparator.py# Comparador que valida o manual contra o 'set' nativo do Python
│   │   └── cli_parte1.py       # Terminal interativo com conceitos didáticos em tempo real
│   │
│   ├── parte2_numeros/         # Módulo dos Conjuntos Numéricos
│   │   ├── parser.py           # Analisador sintático (Regex) para frações, dízimas e raízes
│   │   ├── generator_fraction.py# Algoritmo de Euclides (MDC) e cálculo de Fração Geratriz
│   │   ├── classifier.py       # Classificador hierárquico nos conjuntos N, Z, Q, I, R
│   │   ├── primes_divisors.py  # Crivo de Eratóstenes e listagem de divisores
│   │   └── cli_parte2.py       # Terminal interativo de classificação numérica
│   │
│   ├── parte3_integracao/      # Módulo dos Mini-Projetos de Engenharia de Software
│   │   ├── jaccard_recommender.py # Sistema de Recomendação por Afinidade (Índice de Jaccard)
│   │   ├── rbac_access_control.py # Controle de Acesso por Papéis (RBAC com união e subconjuntos)
│   │   ├── cartesian_powerset.py  # Produto Cartesiano e explosão combinatória das Partes (2^n)
│   │   ├── real_intervals.py      # Álgebra contínua de intervalos na reta real [a, b)
│   │   └── cli_parte3.py          # Terminal interativo da Parte 3
│   │
│   └── utils/
│       ├── display.py          # Formatação de tabelas, cores ANSI e compatibilidade UTF-8 Windows
│       └── helpers.py          # Formatadores de texto e conversor de entradas de usuário
│
├── tests/                      # Suíte de Testes Unitários Automatizados
│   ├── test_parte1.py          # Testes de borda e equivalência para a Parte 1
│   ├── test_parte2.py          # Testes de classificação e frações para a Parte 2
│   └── test_parte3.py          # Testes com gabarito oficial para a Parte 3
│
└── logs/                       # Arquivos de log gerados automaticamente
    ├── execucao_parte1.txt
    ├── execucao_parte2.txt
    ├── execucao_parte3.txt
    └── execucao_completa.txt
```

---

## 🧩 2. Parte 1: Teoria dos Conjuntos

O arquivo principal é [`src/parte1_conjuntos/manual_set.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte1_conjuntos/manual_set.py).  
Ele cumpre a regra de **não usar operadores prontos de conjuntos** (`|`, `&`, `-`, `^`, `issubset`). Todas as operações foram criadas artesanalmente com `for` e `if` sobre listas normais.

### 2.1 Eliminação de Repetidos (Garantia de Unicidade)
* **Local:** `manual_set.py` $\rightarrow$ Método `eliminar_repetidos(elementos)` (linhas 16 a 30).
* **Fundamento Matemático:** Na teoria dos conjuntos, um conjunto não admite repetição: $\{1, 2, 2, 3\} \equiv \{1, 2, 3\}$.
* **Como o código faz:**
  ```python
  unicos = []
  for x in elementos:
      ja_existe = False
      for u in unicos:
          if u == x:
              ja_existe = True
              break
      if not ja_existe:
          unicos.append(x)
  return unicos
  ```
  O algoritmo percorre cada item da entrada bruta e só o insere na lista final se uma varredura interna não encontrar nenhum elemento idêntico.

---

### 2.2 Pertinência ($x \in A$)
* **Local:** `manual_set.py` $\rightarrow$ Método `pertence(elemento, conjunto)` (linhas 33 a 41).
* **Fundamento Matemático:** Predicado de primeira ordem que testa se um indivíduo $x$ integra a coleção $A$.
* **Como o código faz:**
  ```python
  for item in conjunto:
      if item == elemento:
          return True
  return False
  ```
  Itera linearmente pelo conjunto. Se encontrar correspondência exata, interrompe imediatamente e retorna `True`. Se esgotar os elementos, retorna `False`.

---

### 2.3 Cardinalidade ($|A|$)
* **Local:** `manual_set.py` $\rightarrow$ Método `cardinalidade(conjunto)` (linhas 44 a 52).
* **Fundamento Matemático:** Quantidade de elementos distintos contidos no conjunto.
* **Como o código faz:**
  Primeiro sanitiza o conjunto com `eliminar_repetidos(conjunto)`. Em seguida, utiliza um contador manual com laço `for _ in unicos: contador += 1`, sem invocar funções mágicas.

---

### 2.4 União ($A \cup B$)
* **Local:** `manual_set.py` $\rightarrow$ Método `uniao(conjunto_a, conjunto_b)` (linhas 55 a 71).
* **Fórmula Matemática:** $A \cup B = \{x \mid x \in A \lor x \in B\}$.
* **Como o código faz:**
  1. Cria uma lista vazia `resultado = []`.
  2. Percorre `conjunto_a`: se o elemento ainda não estiver em `resultado` (testado via `pertence`), adiciona.
  3. Percorre `conjunto_b`: se o elemento ainda não estiver em `resultado`, adiciona.
  4. Retorna a lista contendo todos os elementos de ambos, sem duplicações.

---

### 2.5 Interseção ($A \cap B$)
* **Local:** `manual_set.py` $\rightarrow$ Método `intersecao(conjunto_a, conjunto_b)` (linhas 74 a 83).
* **Fórmula Matemática:** $A \cap B = \{x \mid x \in A \land x \in B\}$.
* **Como o código faz:**
  ```python
  resultado = []
  for item in conjunto_a:
      if ManualSetOperations.pertence(item, conjunto_b):
          if not ManualSetOperations.pertence(item, resultado):
              resultado.append(item)
  return resultado
  ```
  Varre cada elemento de $A$. Apenas os elementos que **também pertencem a $B$** são adicionados à saída.

---

### 2.6 Diferença ($A \setminus B$ e $B \setminus A$)
* **Local:** `manual_set.py` $\rightarrow$ Método `diferenca(conjunto_a, conjunto_b)` (linhas 86 a 95).
* **Fórmula Matemática:** $A \setminus B = \{x \mid x \in A \land x \notin B\}$.
* **Como o código faz:**
  Varre os elementos de $A$. Se o elemento **NÃO pertencer a $B$** (`not pertence(item, conjunto_b)`), ele é adicionado à lista resultante. A operação é não-comutativa ($A - B \neq B - A$).

---

### 2.7 Diferença Simétrica ($A \ \Delta \ B$)
* **Local:** `manual_set.py` $\rightarrow$ Método `diferenca_simetrica(conjunto_a, conjunto_b)` (linhas 98 a 105).
* **Fórmula Matemática:** $A \ \Delta \ B = (A \setminus B) \cup (B \setminus A)$.
* **Como o código faz:**
  Reaproveita as operações manuais anteriores: calcula `diff_a_b = diferenca(A, B)` e `diff_b_a = diferenca(B, A)`, retornando a `uniao(diff_a_b, diff_b_a)`. Representa os elementos que estão em apenas um dos conjuntos (XOR lógico).

---

### 2.8 Inclusão / Subconjunto ($A \subseteq B$)
* **Local:** `manual_set.py` $\rightarrow$ Método `subconjunto(conjunto_a, conjunto_b)` (linhas 108 a 117).
* **Fórmula Matemática:** $A \subseteq B \iff \forall x (x \in A \implies x \in B)$.
* **Como o código faz:**
  ```python
  for item in conjunto_a:
      if not ManualSetOperations.pertence(item, conjunto_b):
          return False
  return True
  ```
  Varre $A$. Se encontrar **qualquer** elemento que não esteja em $B$, retorna `False`. Se terminar o laço sem falhas, retorna `True`.  
  *Tratamento do conjunto vazio ($\emptyset$):* Se $A = []$, o laço não roda nenhuma iteração e o código retorna `True` diretamente, satisfazendo o teorema de que o conjunto vazio é subconjunto de qualquer conjunto.

---

### 2.9 Inclusão Própria ($A \subset B$)
* **Local:** `manual_set.py` $\rightarrow$ Método `subconjunto_proprio(conjunto_a, conjunto_b)` (linhas 120 a 130).
* **Fórmula Matemática:** $A \subset B \iff A \subseteq B \land A \neq B \iff A \subseteq B \land |A| < |B|$.
* **Como o código faz:**
  Primeiro verifica se `subconjunto(A, B)` é verdadeiro. Depois compara se `cardinalidade(A) < cardinalidade(B)`. Isso garante que $B$ tenha obrigatoriamente elementos que não estão em $A$. Se $A = B$, retorna `False`.

---

### 2.10 Complemento Relativo ($A^c = U \setminus A$)
* **Local:** `manual_set.py` $\rightarrow$ Método `complemento(conjunto_a, universo)` (linhas 133 a 138).
* **Como o código faz:**
  Invoca `diferenca(universo, conjunto_a)`.

---

### 2.11 Validação com a Solução Nativa
* **Local:** [`src/parte1_conjuntos/native_comparator.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte1_conjuntos/native_comparator.py)
* **Como faz:** A classe `SetComparator` executa paralelamente a operação manual e a operação nativa do Python (`set | set`, `set & set`, etc.) e compara os conjuntos resultantes. Se forem matematicamente idênticos, adiciona o status `'valido': True` com a tag visual `[✓ VALIDADO]`.

---

## 🔢 3. Parte 2: Conjuntos Numéricos

### 3.1 Reconhecimento de Padrões e Parsing (Expressões Regulares)
* **Local:** [`src/parte2_numeros/parser.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte2_numeros/parser.py)
* **Como faz:**
  Utiliza expressões regulares para identificar a natureza da entrada do usuário:
  * **Inteiro:** `^[+-]?\d+$` (ex: `7`, `-3`, `0`).
  * **Fração:** `^[+-]?\d+\s*/\s*[+-]?\d+$` (ex: `3/4`, `-5/2`, `6/3`).
  * **Decimal Finito:** `^[+-]?\d+[\.,]\d+$` (ex: `0.75`, `2,5`).
  * **Dízima Periódica:** `^[+-]?(\d+)?[\.,](\d+)?\((\d+)\)$` (ex: `0,(3)` ou `1,2(5)`). Captura em grupos separados a *parte inteira*, o *antiperíodo* e o *período*.
  * **Raiz Quadrada:** `^[vV](\d+)$` (ex: `V9`, `V2`).

---

### 3.2 Algoritmo de Euclides para MDC e Simplificação de Fração
* **Local:** [`src/parte2_numeros/generator_fraction.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte2_numeros/generator_fraction.py) $\rightarrow$ Funções `mdc(a, b)` e `simplificar_fracao(num, den)`.
* **Como faz o MDC:**
  ```python
  while b:
      a, b = b, a % b
  return a
  ```
  Implementa o Algoritmo de Divisões Sucessivas de Euclides em $O(\log(\min(a, b)))$. A simplificação divide numerador e denominador por `mdc(num, den)`.

---

### 3.3 Dedução da Fração Geratriz de Dízimas Periódicas
* **Local:** `generator_fraction.py` $\rightarrow$ Função `fracao_geratriz_dizima(...)` (linhas 49 a 90).
* **Fórmula Algébrica Aplicada:**
  Dada uma dízima $I,A(P)$, onde $I$ é a parte inteira, $A$ é o antiperíodo (comprimento $k$) e $P$ é o período (comprimento $p$):
  $$\text{Numerador Bruto} = \text{Valor}(I \mathbin{\Vert} A \mathbin{\Vert} P) - \text{Valor}(I \mathbin{\Vert} A)$$
  $$\text{Denominador Bruto} = \underbrace{99\dots9}_{p\text{ noves}} \underbrace{00\dots0}_{k\text{ zeros}}$$
* **Exemplo Prático - $1{,}2(5)$:**
  * Parte inteira = 1, antiperíodo = 2 (comprimento 1), período = 5 (comprimento 1).
  * Numerador = $125 - 12 = 113$.
  * Denominador = um nove seguido de um zero = $90$.
  * Fração geratriz bruta = $\frac{113}{90}$ (já irredutível).
* **O Caso Notável de $0{,}(9)$:**
  * Numerador = $9 - 0 = 9$.
  * Denominador = $9$.
  * Fração = $\frac{9}{9} = \frac{1}{1} = 1$. O sistema detecta automaticamente que simplifica para o inteiro $1$ e o classifica como Natural ($\mathbb{N}$).

---

### 3.4 Classificador Hierárquico nos Conjuntos Numéricos
* **Local:** [`src/parte2_numeros/classifier.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte2_numeros/classifier.py) $\rightarrow$ `NumberClassifier.classificar(...)`.
* **Lógica Hierárquica:**
  1. Se for raiz cujo radicando não é quadrado perfeito ($\sqrt{2}$), pertence a $\mathbb{I}$ e $\mathbb{R}$. Como $\mathbb{Q} \cap \mathbb{I} = \emptyset$, não pertence a $\mathbb{N}, \mathbb{Z}, \mathbb{Q}$.
  2. Para números racionais (denominador simplificado $den$):
     * Pertence sempre a $\mathbb{Q}$ e $\mathbb{R}$.
     * Se $den == 1$, a fração simplificou para um número inteiro $\rightarrow$ pertence a $\mathbb{Z}$.
     * Se além disso $num \ge 0$, pertence aos Naturais $\rightarrow \mathbb{N}$ (convenção adotada: $0 \in \mathbb{N}$).
     * Se $den > 1$, não pode ser inteiro nem natural $\rightarrow$ apenas $\mathbb{Q}$ e $\mathbb{R}$.

---

### 3.5 Crivo de Eratóstenes e Listagem de Divisores
* **Local:** [`src/parte2_numeros/primes_divisors.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte2_numeros/primes_divisors.py)
* **Crivo:** Cria uma lista booleana de tamanho $n+1$. Começa em $p = 2$ e marca todos os seus múltiplos como falsos ($2p, 3p, \dots$) até $\sqrt{n}$. Retorna todos os índices que permaneceram verdadeiros (subconjunto dos Primos $\mathbb{P} \subset \mathbb{N}$).
* **Divisores:** Varre de $1$ até $\lfloor\sqrt{n}\rfloor$. Se $i$ divide $n$, adiciona $i$ e $n // i$ aos divisores. Ordena e retorna a lista.

---

## 🚀 4. Parte 3: Mini-Projetos de Integração

O grupo implementou **todos os 4 mini-projetos propostos**:

### 4.1 Sistema de Recomendação por Afinidade (Índice de Jaccard)
* **Local:** [`src/parte3_integracao/jaccard_recommender.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte3_integracao/jaccard_recommender.py)
* **Fórmula Matemática:**
  $$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$
* **Como o código faz:**
  Invoca diretamente as funções manuais da Parte 1:
  ```python
  intersecao = ManualSetOperations.intersecao(interesses_u1, interesses_u2)
  uniao = ManualSetOperations.uniao(interesses_u1, interesses_u2)
  indice = len(intersecao) / len(uniao)
  ```
* **Conferência com o Gabarito Oficial:**
  * Ana & Bia: interesses em comum = {cinema, jazz} (2), união = 6 $\implies J = 2/6 \approx 0{,}3333$.
  * Ana & Caio: interesses em comum = {cinema, games} (2), união = 5 $\implies J = 2/5 = 0{,}4000$.
  * Bia & Caio: interesses em comum = {cinema} (1), união = 6 $\implies J = 1/6 \approx 0{,}1667$.
  * Recomendação para Ana: **Caio** (maior afinidade).

---

### 4.2 Controle de Acesso Baseado em Perfis (RBAC)
* **Local:** [`src/parte3_integracao/rbac_access_control.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte3_integracao/rbac_access_control.py)
* **Aplicação da Teoria:**
  * As permissões de um usuário são calculadas pela **união** dos direitos concedidos por cada um de seus papéis: $Perm(U) = \bigcup_{p \in Papéis} Perm(p)$.
  * A verificação se o usuário pode executar uma ação utiliza **pertinência**: $acao \in Perm(U)$.
  * A hierarquia de perfis (ex: verificar se `editor` é subconjunto de `admin`) utiliza **inclusão**: $Perm(\text{editor}) \subseteq Perm(\text{admin})$.

---

### 4.3 Produto Cartesiano e Conjunto das Partes ($2^n$)
* **Local:** [`src/parte3_integracao/cartesian_powerset.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte3_integracao/cartesian_powerset.py)
* **Produto Cartesiano ($A \times B$):**
  Implementado com dois laços aninhados:
  ```python
  resultado = []
  for a in conjunto_a:
      for b in conjunto_b:
          resultado.append((a, b))
  ```
* **Conjunto das Partes ($\mathcal{P}(A)$):**
  Gera recursivamente todos os subconjuntos possíveis. Demonstra que a cardinalidade do conjunto das partes cresce exponencialmente como $|\mathcal{P}(A)| = 2^n$. Para um conjunto com 3 elementos, gera exatamente os $2^3 = 8$ subconjuntos: $\emptyset$, $\{1\}$, $\{2\}$, $\{1, 2\}$, $\{3\}$, $\{1, 3\}$, $\{2, 3\}$, $\{1, 2, 3\}$.

---

### 4.4 Álgebra de Intervalos Reais Contínuos
* **Local:** [`src/parte3_integracao/real_intervals.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/src/parte3_integracao/real_intervals.py)
* **Como faz:**
  Modela intervalos semiabertos e fechados $[a, b)$.
  * **Pertinência:** Avalia se $x \ge a$ (ou $>$) e $x \le b$ (ou $<$).
  * **Interseção:** $[a, b) \cap [c, d]$ calcula $\max(a, c)$ e $\min(b, d)$ ajustando as extremidades abertas/fechadas. Exemplo demonstrado: $[2, 5) \cap [3, 7] = [3, 5)$.

---

## 🧪 5. Como os Testes Garantem a Qualidade

O arquivo [`run_tests.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/run_tests.py) executa a suíte de 25 testes unitários em [`tests/`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/tests):
1. [`test_parte1.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/tests/test_parte1.py): Testa exaustivamente casos de borda (conjunto vazio, conjuntos disjuntos, conjuntos idênticos, elementos repetidos) e atesta que a saída do algoritmo manual é idêntica à do `set` em 100% das situações.
2. [`test_parte2.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/tests/test_parte2.py): Testa os 12 números de amostra obrigatória, frações irredutíveis e dízimas.
3. [`test_parte3.py`](file:///c:/Users/mathe/OneDrive/Desktop/trabalhoDeMatemativca/tests/test_parte3.py): Testa Jaccard contra o gabarito oficial, RBAC, Combinatória e Intervalos.

---

## 💡 6. Dicas Rápidas para a Apresentação Oral

Se o professor perguntar:

1. **"Onde está a operação de união sem usar biblioteca?"**  
   *Resposta:* *"Está em `src/parte1_conjuntos/manual_set.py`, no método `uniao()`. Criamos uma lista vazia, inserimos os elementos de A verificando se já não existem, e depois os elementos de B com a mesma verificação."*

2. **"Como vocês trataram o conjunto vazio na inclusão?"**  
   *Resposta:* *"No método `subconjunto()`, o laço `for` varre o primeiro conjunto. Como o conjunto vazio não possui elementos, o laço termina imediatamente sem encontrar nenhuma violação, retornando `True`, o que comprova matematicamente que $\emptyset \subseteq B$ para qualquer $B$."*

3. **"Como o programa resolve a dízima composta $1{,}2(5)$?"**  
   *Resposta:* *"No arquivo `src/parte2_numeros/generator_fraction.py`. Separamos a parte inteira (1), o antiperíodo (2) e o período (5). O numerador é calculado como $125 - 12 = 113$ e o denominador como $90$ (um 9 para o período e um 0 para o antiperíodo). Depois aplicamos o MDC de Euclides."*
