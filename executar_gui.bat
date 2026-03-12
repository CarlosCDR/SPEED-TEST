@echo off
REM Script para executar o Speed Test com Interface Gráfica
REM Instala dependências automaticamente se necessário

echo Verificando dependencias...
pip show speedtest-cli >nul 2>&1

if errorlevel 1 (
    echo.
    echo Instalando speedtest-cli...
    pip install speedtest-cli
    echo.
)

echo.
echo Iniciando Speed Test com Interface Gráfica...
echo.
python speed_test_gui.py

pause
