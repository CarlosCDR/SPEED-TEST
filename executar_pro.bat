@echo off
REM Script para executar o Speed Test PRO com Interface Gráfica Avançada

REM ===== Defina o diretório do script =====
cd /d "%~dp0"

REM ===== Verifica se Python está instalado =====
python --version >nul 2>&1
if errorlevel 1 (
    echo Python nao encontrado no PATH.
    echo Instale o Python e marque "Add to PATH" na instalacao.
    pause
    exit /b
)

REM ===== Verifica dependencias =====
pip show speedtest-cli >nul 2>&1
if errorlevel 1 (
    echo Instalando speedtest-cli...
    pip install speedtest-cli
)

REM ===== Roda o script =====
echo.
echo Iniciando Speed Test PRO...
echo.
python speed_test_pro.py

REM ===== Pausa para ver erros =====
echo.
echo Pressione qualquer tecla para sair...
pause