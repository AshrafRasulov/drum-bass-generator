AD2_MAP = {
    "kick": 36,
    "snare_center": 38,
    "snare_rimshot": 40,
    "hat_closed_tip": 42,
    "hat_closed_shaft": 44,
    "hat_open": 46,
    "tom_high": 48,
    "tom_mid": 45,
    "tom_low": 43,
    "crash": 49,
    "ride_tip": 51
}

# Функция для получения маппинга по названию VST
def get_mapping(vst_name):
    if vst_name == "Addictive Drum":
        return AD2_MAP
    # Здесь можно добавить другие инструменты
    return AD2_MAP