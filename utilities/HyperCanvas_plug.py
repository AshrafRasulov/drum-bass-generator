# Маппинг для Hyper Canvas / Super Quartet / SRX / GM Standard
# Работает строго на 10-м MIDI канале (в коде это канал 9)
MAP = {
    # Основные компоненты
    "kick": 36,             # Bass Drum 1
    "snare_center": 38,     # Acoustic Snare
    "snare_rimshot": 40,    # Electric Snare / Rimshot
    "snare_sidestick": 37,  # Side Stick
    
    # Хай-хэты
    "hat_closed_tip": 42,   # Closed Hi-Hat
    "hat_closed_shaft": 44, # Pedal Hi-Hat
    "hat_open": 46,         # Open Hi-Hat
    
    # Томы
    "tom_low": 41,          # Low Floor Tom
    "tom_mid": 45,          # Low-Mid Tom
    "tom_high": 48,         # Hi Mid Tom
    
    # Тарелки
    "crash_1": 49,          # Crash Cymbal 1
    "crash_2": 57,          # Crash Cymbal 2
    "ride_tip": 51,         # Ride Cymbal 1
    "ride_bell": 53,        # Ride Bell
    
    # Перкуссия
    "cowbell": 56,          # Cowbell
    "tambourine": 54        # Tambourine
}

CHANNEL = 9 # Стандартный 10-й канал MIDI для ударных GM