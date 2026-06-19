# Маппинг для баса (GM для HyperCanvas/SQ и специфичный для Ample)
def get_bass_mapping(vst_name):
    if "Ample Bass" in vst_name:
        return {
            "root": 36,        # Базовая нота C1
            "slide_down": 24,  # Key-switch для слайда (пример)
            "palm_mute": 26    # Key-switch для приглушения
        }, 0 # Канал для Ample Bass
    else:
        # Стандартные MIDI басы (HyperCanvas/SQ)
        return {
            "root": 36,
            "octave_up": 48
        }, 1 # 2-й канал для баса, чтобы не мешать ударным (10-му каналу)