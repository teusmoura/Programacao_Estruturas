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
        echo Instale o Python 3 e marque a opcao para adiciona-lo ao PATH,
        echo ou instale o Python Launcher ^(py^).
        echo.
        pause
        exit /b 1
    )

    echo Criando ambiente virtual...
    !PYTHON_COMANDO! -m venv "%PASTA_VENV%"
    if errorlevel 1 (
        echo.
        echo ERRO: nao foi possivel criar o ambiente virtual.
        pause
        exit /b 1
    )
)

echo Instalando dependencias...
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

rem Instala a raiz do projeto em modo editavel, tornando "database" importavel.
set "RAIZ=%~dp0"
set "RAIZ=%RAIZ:~0,-1%"
"%PYTHON_VENV%" -m pip install --no-deps -e "%RAIZ%"
if errorlevel 1 (
    echo.
    echo ERRO: falha ao instalar o projeto em modo editavel.
    pause
    exit /b 1
)

echo.
echo Ambiente pronto.
echo Interpretador: %PYTHON_VENV%
echo.
echo Para criar e popular o banco lojas_rede:
echo   "%PYTHON_VENV%" database\criar_banco.py
echo.
echo Para restaurar os dados iniciais:
echo   "%PYTHON_VENV%" database\reiniciar_banco.py
echo.
echo Abrindo um Prompt de Comando com o ambiente virtual ativado...
call "%PASTA_VENV%\Scripts\activate.bat"
cmd /k
