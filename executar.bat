@echo off
chcp 65001 > nul
title Laboratório de Conjuntos - FATEC Osasco

:menu
cls
echo ===========================================================================
echo            LABORATORIO DE CONJUNTOS E CONJUNTOS NUMERICOS
echo      FATEC Osasco - DSM - Fundamentos Matematicos para Computacao
echo ===========================================================================
echo.
echo Escolha o que deseja executar:
echo.
echo   [1] Abrir Menu Interativo Principal (main.py)
echo   [2] Rodar Testes Unitarios Automatizados (run_tests.py)
echo   [3] Rodar Demonstracoes e Atualizar Logs (run_demos.py)
echo   [4] Abrir o Guia de Apresentacao (COMO_RODAR.md)
echo   [5] Abrir a Explicacao Detalhada do Codigo (EXPLICACAO_DO_CODIGO.md)
echo   [0] Sair
echo.
set /p opcao=Digite a opcao desejada (0-5): 

if "%opcao%"=="1" (
    cls
    python main.py || py main.py
    pause
    goto menu
)
if "%opcao%"=="2" (
    cls
    python run_tests.py || py run_tests.py
    pause
    goto menu
)
if "%opcao%"=="3" (
    cls
    python run_demos.py || py run_demos.py
    pause
    goto menu
)
if "%opcao%"=="4" (
    start notepad COMO_RODAR.md
    goto menu
)
if "%opcao%"=="5" (
    start notepad EXPLICACAO_DO_CODIGO.md
    goto menu
)
if "%opcao%"=="0" (
    exit
)

echo Opcao invalida!
pause
goto menu
