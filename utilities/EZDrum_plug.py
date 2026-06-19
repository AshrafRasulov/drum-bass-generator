# Маппинг для EZDrummer (на основе официальной раскладки E-Drum / Piano Roll)
# Каждая нота подобрана так, чтобы соответствовать стандартным пресетам EZDrummer
MAP = {
    # КИК (Kick)
    "kick": 36,             # C1 - Kick
    
    # МАЛЫЙ БАРАБАН (Snare)
    "snare_center": 38,     # D1 - Snare Center
    "snare_rimshot": 40,    # E1 - Snare Rimshot
    "snare_sidestick": 37,  # C#1 - Side Stick
    
    # ХАЙ-ХЭТЫ (Hi-Hats)
    "hat_closed_tip": 42,   # F#1 - Closed Hat Tip
    "hat_closed_shaft": 44, # G#1 - Closed Hat Shaft
    "hat_open": 46,         # A#1 - Open Hat
    "hat_foot": 43,         # G1 - Foot Close
    
    # ТОМЫ (Toms) - настроены по высоте
    "tom_high": 50,         # D2 - High Tom
    "tom_mid": 47,          # B1 - Mid Tom
    "tom_low": 45,          # A1 - Low Tom
    
    # ТАРЕЛКИ (Cymbals)
    "crash_1": 49,          # C#2 - Crash 1
    "crash_2": 57,          # A2 - Crash 2
    "ride_tip": 51,         # D#2 - Ride Tip
    "ride_bell": 53,        # F2 - Ride Bell
    
    # ПЕРКУССИЯ
    "cowbell": 56,          # G#2 - Cowbell
    "tambourine": 54        # F#2 - Tambourine
}

# В EZDrummer стандартно используется 1-й MIDI канал (индекс 0)
CHANNEL = 0