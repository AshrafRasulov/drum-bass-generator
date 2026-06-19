# Маппинг для Addictive Drums 2 (на основе официальной карты XLN Audio)
# Каждая нота соответствует реальным артикуляциям барабанщика
MAP = {
    # КИК (Kick)
    "kick": 36,             # Основной бас-барабан
    
    # МАЛЫЙ БАРАБАН (Snare)
    "snare_center": 38,     # Удар по центру (Center)
    "snare_rimshot": 40,    # Римшот (Rimshot)
    "snare_sidestick": 37,  # Римклик/Сайдстик (Sidestick)
    "snare_shallow": 41,    # Неглубокий удар (Shallow Rimshot)
    
    # ХАЙ-ХЭТЫ (Hi-Hats)
    "hat_closed_tip": 42,   # Закрытый, удар кончиком (Closed Tip)
    "hat_closed_shaft": 44, # Закрытый, удар плечом (Closed Shaft)
    "hat_open": 46,         # Открытый хай-хэт (Open)
    "hat_foot": 43,         # Удар педалью (Foot Close)
    
    # ТОМЫ (Toms) - настроены по высоте
    "tom_high": 48,         # Высокий том
    "tom_mid": 45,          # Средний том
    "tom_low": 43,          # Низкий том
    
    # ТАРЕЛКИ (Cymbals)
    "crash_1": 49,          # Crash 1
    "crash_2": 57,          # Crash 2
    "ride_tip": 51,         # Райд, удар кончиком (Ride Tip)
    "ride_bell": 53,        # Райд, удар в купол (Ride Bell)
    "ride_shaft": 55,       # Райд, удар плечом (Ride Shaft)
    
    # ПЕРКУССИЯ (Дополнительно)
    "cowbell": 56,          # Ковбел
    "tambourine": 54        # Тамбурин
}

# В AD2 стандартно используется 1-й MIDI канал (индекс 0)
CHANNEL = 0