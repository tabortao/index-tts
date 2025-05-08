@echo off
pushd %~dp0
REM %~dp0
REM pushd
echo Current directory is: %cd%
echo The program is starting, please wait...
rem cd /d F:\Code\TTS\index-tts
set PYTHON_PATH=.\py312\python.exe
echo The project is large and starts slowly, please wait patiently...
timeout /t 3 /nobreak > nul 
"%PYTHON_PATH%" webui.py
pause