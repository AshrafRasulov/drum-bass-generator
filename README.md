🥁 Drum MIDI Generator Pro
Универсальный инструмент для автоматической генерации барабанных MIDI-партий с поддержкой различных VST-инструментов, системы маркеров и библиотеки пользовательских переходов (Fills).

📁 Структура проекта
Plaintext
drum_generator/
├── app.py                  # Главный UI (Streamlit)
├── drumming.py             # Движок: сборка трека и генерация MIDI
├── fills_library/          # Библиотека переходов (Personality)
│   ├── Pop-Punk/           # MIDI-файлы переходов по жанрам
│   ├── Rock/
│   └── Metal/
└── utilities/              # Модули маппинга инструментов
    ├── __init__.py         # Инициализация пакета
    ├── mappings.py         # Диспетчер выбора VST
    ├── AD2_plug.py         # Маппинг для Addictive Drums 2
    ├── EZDrum_plug.py      # Маппинг для EZDrummer
    └── HyperCanvas_plug.py # Маппинг для Roland/Edirol/General MIDI
🛠 Как это работает
Диспетчеризация (mappings.py): При выборе VST в интерфейсе, программа автоматически подгружает соответствующий маппинг нот и MIDI-канал.

Генерация (drumming.py):

Создает структуру трека с автоматической расстановкой MIDI-маркеров (Intro, Verse, Chorus, Bridge).

Учитывает динамику (add_note_with_feel — рандомизация Velocity).

Personality (Fills Library):

Программа ищет случайный MIDI-переход в папке fills_library/{жанр}/.

Если папка пуста, автоматически генерирует классический переход по томам.

Поддерживает загрузку собственных MIDI-файлов через вкладку "Personality".

🚀 Поддерживаемые инструменты
Addictive Drums 2: Канал 0 (артикуляции: Rimshot, Sidestick, Bell и др.).

EZDrummer: Канал 0 (стандартная раскладка Toontrack).

HyperCanvas / SRX Orchestra / Super Quartet: Канал 9 (General MIDI стандарт).
