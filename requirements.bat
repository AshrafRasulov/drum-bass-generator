@echo off
echo Сканирование проекта и создание requirements.txt...
pip install pipreqs
:: Команда --force перезапишет файл
pipreqs . --force --encoding=utf-8
echo Файл requirements.txt успешно создан!
pause