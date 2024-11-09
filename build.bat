@echo off
pyinstaller --icon=Icon\Icon.ico --onefile AbidosCalculator.py
python sub_data_build.py
pause