@echo off
setlocal
set "PASTA=%~1"
if not defined PASTA set /p "PASTA=Pasta do jogo: "
if not defined PASTA (
 echo Pasta nao informada.
 pause
 exit /b 1
)
if exist "%~dp0Traduzir_F22.exe" (
 "%~dp0Traduzir_F22.exe" "%PASTA%"
) else (
 where python >nul 2>&1
 if errorlevel 1 (
  echo Traduzir_F22.exe nao encontrado. Baixe o ZIP em Releases.
  pause
  exit /b 1
 )
 python "%~dp0aplicar.py" "%PASTA%"
)
if errorlevel 1 echo Falha na instalacao; confira o erro acima.
pause
