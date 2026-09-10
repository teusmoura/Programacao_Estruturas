@echo off
setlocal EnableExtensions EnableDelayedExpansion
cd /d "%~dp0"

set "PASTA_VENV=%~dp0.venv"
set "PYTHON_VENV=%PASTA_VENV%\Scripts\python.exe"

if not exist "%PYTHON_VENV%" (
    set "PYTHON_COMANDO="

    py -3 --version >nul 2>&1
    if not errorlevel 1 (
        set "PYTHON_COMANDO=py -3"
    ) else (
        python --version >nul 2>&1
        if not errorlevel 1 (
            set "PYTHON_COMANDO=python"
        )
    )

    if not defined PYTHON_COMANDO (
        echo.
        echo ERRO: Python nao foi encontrado.
        echo Instale o Python 3 e marque a opcao para adiciona-lo ao PATH.
        echo.
        pause
        exit /b 1
    )

    echo Criando ambiente virtual do curso...
    !PYTHON_COMANDO! -m venv "%PASTA_VENV%"
    if errorlevel 1 (
        echo.
        echo ERRO: nao foi possivel criar o ambiente virtual.
        pause
        exit /b 1
    )
)

echo Instalando dependencias do curso...
"%PYTHON_VENV%" -m pip install --upgrade pip
if errorlevel 1 (
    echo.
    echo ERRO: falha ao atualizar o pip.
    pause
    exit /b 1
)

"%PYTHON_VENV%" -m pip install -r "%~dp0requirements.txt"
if errorlevel 1 (
    echo.
    echo ERRO: falha ao instalar as dependencias.
    pause
    exit /b 1
)

echo.
echo Ambiente pronto para as atividades.
echo.
echo O que fazer agora:
echo   1. Verifique se o MySQL do XAMPP esta rodando.
echo   2. Padrao XAMPP: usuario=root, senha=vazia, host=localhost, porta=3306
echo   3. Se o ambiente tiver senha diferente, defina as variaveis:

echo      set MYSQL_USER=root

echo      set MYSQL_PASSWORD=sua_senha

echo      set MYSQL_HOST=localhost

echo      set MYSQL_PORT=3306

echo   4. Crie e popular o banco:

echo      "%PYTHON_VENV%" database\criar_banco.py

echo   5. Quando precisar resetar os dados:

echo      "%PYTHON_VENV%" database\reiniciar_banco.py

echo.
echo Abrindo um prompt com o ambiente do curso ativado...
call "%PASTA_VENV%\Scripts\activate.bat"
cmd /k
