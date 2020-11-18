@ECHO OFF
:: This batch will run main.py in this directory

TITLE main.py

if exist main.py (
	python main.py
) else (
	echo main.py not found in this directory
)

PAUSE

EXIT /B
