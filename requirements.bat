@echo off
echo Сканирование проекта и создание requirements.txt...
pip install pipreqs
:: Команда --force перезапишет файл, если он уже есть
pipreqs . --force
echo Файл requirements.txt успешно создан на основе твоего кода!
pause