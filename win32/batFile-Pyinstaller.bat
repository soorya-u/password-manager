pyinstaller  ^
    -w ^
    --onefile ^
    --add-data "./Assets/wonderwords;wonderwords" ^
    --add-data "./Images;Images" ^
    "main.py"