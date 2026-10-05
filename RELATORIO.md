# Relatório Acadêmico: Aplicação Prática da Teoria dos Conjuntos

**Instituição:** Faculdade de Tecnologia de Osasco (FATEC Osasco)  
**Curso:** Desenvolvimento de Software Multiplataforma (DSM)  
**Disciplina:** Matemática Discreta / Fundamentos Matemáticos para Computação  
**Atividade:** Laboratório de Conjuntos e Conjuntos Numéricos  

---

### 1. Onde a Teoria dos Conjuntos Apareceu no Código?

A teoria dos conjuntos não foi apenas uma referência conceitual, mas a espinha dorsal de toda a arquitetura desenvolvida neste projeto, manifestando-se em três camadas fundamentais:

1. **Na Estruturação de Dados e Unicidade (Parte 1):**  
   Um conjunto, por definição matemática, não admite multiplicidade de elementos ($A = \{x \mid P(x)\}$). No módulo `manual_set.py`, antes de qualquer cálculo, foi implementado o algoritmo artesanal de eliminação de redundâncias, garantindo que coleções de entrada como $[1, 2, 2, 3, 4]$ fossem canonicamente mapeadas para $\{1, 2, 3, 4\}$. As operações de **União** ($A \cup B = \{x \mid x \in A \lor x \in B\}$), **Interseção** ($A \cap B = \{x \mid x \in A \land x \in B\}$), **Diferença** ($A \setminus B = \{x \mid x \in A \land x \notin B\}$), **Diferença Simétrica** ($A \ \Delta \ B = (A \setminus B) \cup (B \setminus A)$) e **Complemento Relativo** ($A^c = U \setminus A$) foram escritas em lógica pura (laços `for` e predicados `if`), reproduzindo com fidelidade a semântica da lógica de predicados de primeira ordem.

2. **Na Classificação e Pertinência Numérica (Parte 2):**  
   A hierarquia dos conjuntos numéricos ($\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ e $\mathbb{I} \subset \mathbb{R}$, com $\mathbb{Q} \cap \mathbb{I} = \emptyset$) governou o classificador do módulo `classifier.py`. Cada número submetido teve sua pertinência determinada por propriedades matemáticas estruturais: a redutibilidade de frações pelo algoritmo de Euclides ($\gcd(a, b)$), a determinação de frações geratrizes para dízimas periódicas (atestando sua racionalidade $\mathbb{Q}$) e o teste de quadrados perfeitos para separar números racionais de irracionais ($\mathbb{I}$). O Crivo de Eratóstenes, por sua vez, representou a geração do subconjunto dos números primos $\mathbb{P} \subset \mathbb{N}$ por eliminação sistemática de múltiplos (diferença sucessiva de conjuntos).

3. **Nas Aplicações Reais de Engenharia de Software (Parte 3):**  
   A teoria dos conjuntos emergiu como solução direta para problemas clássicos de computação:
   - **Sistemas de Recomendação (Índice de Jaccard):** A similaridade contextual entre perfis de usuários foi modelada como a razão entre a cardinalidade da interseção e da união: $J(A, B) = \frac{|A \cap B|}{|A \cup B|}$.
   - **Segurança da Informação e RBAC:** Permissões de usuários foram modeladas como a união de conjuntos de direitos conferidos por perfis ($\bigcup P_i$), enquanto a hierarquia de privilégios foi expressa pela relação de inclusão ($P_{\text{editor}} \subseteq P_{\text{admin}}$).
   - **Análise Combinatória e Complexidade:** A geração do Conjunto das Partes ($\mathcal{P}(A)$) permitiu demonstrar a explosão combinatória assintótica de ordem $O(2^n)$, fundamental para testes de software e limites de processamento.
   - **Continuidade na Reta Real:** A modelagem de intervalos reais estendeu a teoria dos conjuntos discretos para a topologia da reta numérica contínua.

---

### 2. Qual Operação Foi Mais Difícil de Implementar e Por Quê?

A operação mais desafiadora do projeto foi o **Cálculo da Fração Geratriz e Tratamento das Dízimas Periódicas Compostas** (no módulo `generator_fraction.py` e `parser.py`), em conjunto com a **Inclusão Própria Estrita ($A \subset B$)** nos casos de borda:

- **Complexidade da Dízima Composta:**  
  Diferente de um número inteiro ou decimal finito cuja conversão é direta ($\frac{n}{10^k}$), uma dízima periódica composta — como $1{,}2(5)$ — exige a segregação estrita entre três grandezas: a parte inteira ($I$), a parte não periódica ou antiperíodo ($A$, de comprimento $k$) e o período repetitivo ($P$, de comprimento $p$). A dedução do algoritmo algébrico:
  $$\text{Numerador} = \text{Valor}(I \mathbin{\Vert} A \mathbin{\Vert} P) - \text{Valor}(I \mathbin{\Vert} A)$$
  $$\text{Denominador} = \underbrace{99\dots9}_{p} \underbrace{00\dots0}_{k}$$
  exigiu a criação de um analisador sintático (parser baseado em expressões regulares) robusto para desmembrar notações com vírgula ou ponto, seguido pela simplificação irredutível via MDC. Casos limites singulares, como o valor $0{,}(9) = \frac{9}{9} = 1$, desafiaram o fluxo de classificação ao transitar um número de representação periódica diretamente para o conjunto dos Naturais ($\mathbb{N}$), demandando tratamento elegante e coerente com a análise matemática real.

- **Rigor na Inclusão Própria e Conjuntos Vazios:**  
  Garantir a corretude da inclusão própria ($A \subset B \iff A \subseteq B \land A \neq B$) sem depender de funções prontas exigiu atenção especial aos casos de borda: o conjunto vazio ($\emptyset$), que está contido em qualquer conjunto mas não é subconjunto próprio de si mesmo, e conjuntos de mesma cardinalidade com elementos repetidos na entrada.

---
*Conclusão: A implementação artesanal em Python evidenciou como os axiomas da Teoria dos Conjuntos fornecem as bases lógicas para estruturas de dados, algoritmos de busca, bancos de dados relacionais e modelagem de sistemas seguros.*
