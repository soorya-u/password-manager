pyinstaller  ^
    -w ^
    --onefile ^
    --add-data "./Assets/wonderwords;wonderwords" ^
    --add-data "./Images;Images" ^
    --add-data "./SQL;SQL" ^
    --name "win32_app" ^
    --distpath "./win32" ^
    'main.py'

