@echo off
setlocal
set "PASTA=%~1"
if not defined PASTA set /p "PASTA=Pasta do jogo (exemplo G:\Jogos\F-22 Raptor): "
python "%~dp0aplicar.py" "%PASTA%"
pause
