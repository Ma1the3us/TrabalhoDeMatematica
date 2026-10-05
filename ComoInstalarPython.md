# Como Instalar o Python no Windows (Passo a Passo Rápido)

Como você mencionou que ainda não possui o Python instalado na sua máquina, aqui estão as **duas maneiras mais rápidas e fáceis** de instalá-lo para rodar este projeto:

---

### Opção 1: Pela Microsoft Store (Mais Rápida e Fácil - 1 Minuto)

1. Abra o menu Iniciar do Windows e digite **Microsoft Store**.
2. Na barra de busca da Microsoft Store, digite **Python 3.12** (ou Python 3.11).
3. Clique em **Obter** ou **Instalar**.
4. Pronto! O Windows já configura tudo automaticamente no seu sistema.

---

### Opção 2: Pelo Site Oficial (Recomendada para Desenvolvedores)

1. Acesse o site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Clique no botão amarelo **Download Python 3.x.x**.
3. Abra o instalador baixado.
4. ⚠️ **MUITO IMPORTANTE:** Na primeira tela do instalador, marque a caixinha:  
   ☑️ **Add python.exe to PATH** (ou *Adicionar Python ao PATH*).  
   *(Se não marcar essa opção, o comando `python` não será reconhecido no terminal).*
5. Clique em **Install Now** (Instalar Agora).
6. Ao finalizar, feche o instalador.

---

### Como Testar e Rodar o Projeto

Depois de instalar, feche o terminal/PowerShell atual e abra um novo terminal na pasta `trabalhoDeMatemativca`.

1. **Testar se o Python está funcionando:**
   ```powershell
   python --version
   ```
   Deve exibir algo como: `Python 3.12.x`.

2. **Rodar o Menu Principal do Trabalho:**
   ```powershell
   python main.py
   ```

3. **Rodar Todas as Demonstrações e Gerar os Logs Oficiais:**
   ```powershell
   python run_demos.py
   ```

4. **Rodar os Testes Automatizados:**
   ```powershell
   python run_tests.py
   ```

---
*Todos os arquivos, códigos, testes, relatórios e logs do seu projeto já estão 100% prontos e organizados nesta pasta!*
