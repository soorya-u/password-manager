pyinstaller  ^
    -w ^
    --onefile ^
    --add-data "./Assets/wonderwords;wonderwords" ^
    --add-data "./Images;Images" ^
    --add-data "./Fonts;Fonts" ^
    --name "win32_app" ^
    --distpath "./win32" ^
    'main.py'

