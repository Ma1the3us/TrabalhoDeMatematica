# 🚀 Guia Rápido: Como Rodar o Projeto para Apresentação

Este guia foi elaborado para que você consiga executar e apresentar o projeto de forma rápida, segura e impressionante para o professor e a turma da FATEC Osasco.

---

## ⚡ 1. Como Abrir o Projeto no Terminal (30 Segundos)

### Método Mais Fácil (Pelo Windows Explorer):
1. Abra a pasta do projeto: `trabalhoDeMatemativca`
2. Clique na **barra de endereço** no topo da pasta (onde fica o caminho da pasta).
3. Digite `cmd` ou `powershell` e aperte **Enter**.
4. O terminal já vai abrir diretamente dentro da pasta certa!

### Ou via Atalho Rápido de Duplo Clique:
- Você também pode dar **dois cliques no arquivo `executar.bat`** na pasta do projeto. Ele abrirá o menu imediatamente!

---

## 🎯 2. Comandos Principais para a Apresentação

Você pode executar qualquer um dos três comandos abaixo no terminal:

### A) Menu Interativo Completo (O Principal)
```bash
python main.py
```
> *(Se o comando `python` não responder no seu terminal, use `py main.py`)*

Permite navegar ao vivo entre as opções:
- **1:** Testar a Parte 1 interativamente (você pode digitar conjuntos na hora).
- **2:** Testar o Classificador Numérico (digitar frações, raízes, dízimas).
- **3:** Explorar os 4 Mini-Projetos de Integração (Jaccard, RBAC, etc.).
- **4:** Executar a bateria completa de demonstrações e atualizar os logs.
- **5:** Executar a suíte de testes unitários.

---

### B) Rodar os Testes Unitários Automatizados (Efeito "Uau" com o Professor)
```bash
python run_tests.py
```
- **Tempo de execução:** ~2 milissegundos.
- **Resultado:** **25 testes executados, 25 aprovados (100% de sucesso)**.
- **O que mostrar:** Demonstra rigor de engenharia de software, cobrindo todos os casos de borda (conjunto vazio $\emptyset$, conjuntos iguais, disjuntos, repetidos e validação contra o tipo `set` nativo).

---

### C) Rodar Todas as Demonstrações Obrigatórias de Uma Vez
```bash
python run_demos.py
```
- Executa e imprime na tela todas as tabelas e comparações solicitadas no enunciado oficial:
  - Caso geral com remoção de duplicados.
  - Todos os casos de borda comparando implementação manual vs nativa.
  - Exemplo próprio da equipe (tecnologias Web vs Mobile).
  - Tabela completa de classificação numérica (dízimas compostas $1{,}2(5)$, $0{,}(9)$, $\sqrt{9}$, $\sqrt{2}$).
  - Crivo de Eratóstenes até 30 e Divisores de 36.
  - Mini-projetos com comparação direta contra os gabaritos oficiais.
- Salva automaticamente os arquivos formatados na pasta `logs/`.

---

## 🎙️ 3. Roteiro Sugerido de Apresentação (5 a 8 Minutos)

Se você tiver que falar e apresentar o trabalho, siga esta ordem matadora:

### Passo 1: Abertura (1 minuto)
- *"Nosso projeto foi desenvolvido para a disciplina de Fundamentos Matemáticos/Matemática Discreta do curso de DSM."*
- *"O objetivo foi aplicar a Teoria dos Conjuntos e Conjuntos Numéricos em lógica pura de programação, sem atalhos ou bibliotecas prontas, provando sua equivalência matemática com testes automatizados."*

### Passo 2: Mostrar os Testes Automatizados (1 minuto)
- No terminal, rode: `python run_tests.py`
- Destaque: *"Antes de tudo, implementamos 25 testes unitários cobrindo todos os cenários e casos de borda. Todos passam com 100% de aprovação."*

### Passo 3: Parte 1 - Conjuntos Manuais vs Nativos (2 minutos)
- Abra o menu: `python main.py` -> Opção `1` ou execute `python run_demos.py`.
- Mostre:
  1. A eliminação automática de duplicidades (ex: `1, 2, 2, 3, 4` $\rightarrow$ `{1, 2, 3, 4}`).
  2. As operações de União, Interseção, Diferença, Diferença Simétrica, Inclusão ($\subseteq$ e $\subset$) e Complemento.
  3. Destaque: *"Construímos todas as operações manualmente usando laços `for` e `if`, e nosso comparador valida cada operação contra o `set` nativo do Python, garantindo resultado idêntico."*

### Passo 4: Parte 2 - Conjuntos Numéricos e Dízimas (2 minutos)
- No menu, opção `2` ou mostre a tabela do `run_demos.py`.
- Pontos altos para impressionar o professor:
  - **Dízima periódica composta $1{,}2(5)$**: o algoritmo decompõe a parte inteira, antiperíodo e período, deduzindo algebricamente a fração irredutível $\frac{113}{90}$.
  - **O caso curioso de $0{,}(9)$**: demonstra algebricamente que $\frac{9}{9} = 1$, pertencendo aos Naturais ($\mathbb{N}$) e Inteiros ($\mathbb{Z}$).
  - **Raízes**: separa $\sqrt{9} = 3 \in \mathbb{N}$ de $\sqrt{2} \in \mathbb{I}$ (irracional).
  - **Bônus**: Crivo de Eratóstenes até 30 e Divisores de 36 conferindo 100% com o gabarito.

### Passo 5: Parte 3 - Mini-Projetos de Integração (2 minutos)
- Destaque que a equipe foi além do solicitado: **implementamos os 4 mini-projetos sugeridos**:
  1. **Sistema de Recomendação (Jaccard):** calcula afinidade entre usuários por $\frac{|A \cap B|}{|A \cup B|}$ (Ana, Bia e Caio conferindo com o gabarito $0{,}33$, $0{,}40$ e $0{,}17$).
  2. **Controle de Acesso (RBAC):** segurança baseada em união e inclusão de permissões.
  3. **Combinatória ($2^n$):** demonstração do crescimento exponencial do Conjunto das Partes.
  4. **Intervalos Reais:** operações topológicas com intervalos contínuos $[a, b)$.

### Passo 6: Fechamento com o Relatório Acadêmico (1 minuto)
- Abra o arquivo `RELATORIO.md` para mostrar a resposta às duas perguntas exigidas pelo professor:
  1. **Onde a teoria apareceu?** (Na garantia de unicidade, na hierarquia numérica $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$, e nas aplicações práticas de Jaccard e RBAC).
  2. **Qual foi a operação mais difícil?** (O cálculo algébrico da fração geratriz de dízimas compostas e o rigor nos casos limites de inclusão própria com conjunto vazio).

---

## 🛠️ 4. Solução de Problemas Comuns

- **Erro `python não é reconhecido como comando interno`:**
  - Tente digitar `py main.py` ou `py -3 main.py`.
- **Acentos ou símbolos estranhos no terminal:**
  - O código já foi configurado com codificação UTF-8 automática para Windows. Se necessário, digite `chcp 65001` no terminal antes de rodar.

---

## 📖 5. Onde e Como o Código Faz Cada Operação?

Para uma explicação minuciosa de cada linha, fórmula matemática e arquivo de código (ideal para responder a qualquer pergunta do professor), consulte o arquivo:
👉 **`EXPLICACAO_DO_CODIGO.md`**

