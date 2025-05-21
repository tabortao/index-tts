@echo off
pushd %~dp0
echo Current directory is: %cd%
echo The program is starting, please wait...
set PYTHON_PATH=.\py312\python.exe
echo The project is large and starts slowly, please wait patiently...
timeout /t 3 /nobreak > nul 
"%PYTHON_PATH%" webui.py --model_dir checkpoints\IndexTTS-1.5
pause