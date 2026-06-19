@echo off
echo Установка зависимостей...
call venv\Scripts\activate
pip install -r requirements.txt
echo Все библиотеки установлены!
pause