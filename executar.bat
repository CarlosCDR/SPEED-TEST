@echo off
REM Script para executar o teste de velocidade da internet
REM Automaticamente instala dependências se necessário

echo Verificando dependencias...
pip show speedtest-cli >nul 2>&1

if errorlevel 1 (
    echo.
    echo Instalando speedtest-cli...
    pip install speedtest-cli
    echo.
)

echo.
echo Iniciando teste de velocidade...
echo.
python speed_test.py

pause
