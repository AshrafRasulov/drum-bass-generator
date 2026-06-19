import importlib

def get_mapping(vst_name):
    mapping_name = {
        "Addictive Drum": "AD2",
        "HyperCanvas": "HyperCanvas",
        "HyperQuarter": "HyperCanvas",
        "SRX Orchestra": "HyperCanvas",
        "Dummzz": "EZDrum",
        "EZDrummer": "EZDrum"
    }.get(vst_name, "AD2")

    try:
        plug = importlib.import_module(f"utilities.{mapping_name}_plug")
        return plug.MAP, plug.CHANNEL
    except Exception as e:
        print(f"Ошибка загрузки плагина: {e}")
        return {}, 0