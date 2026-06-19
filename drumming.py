import os
import random
import mido
from midiutil import MIDIFile
from utilities.mappings import get_mapping

# Словарь для смещения тональности
KEY_OFFSETS = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}

def add_note_with_feel(midi, track, channel, note, time, duration, base_velocity):
    velocity = max(20, min(127, base_velocity + random.randint(-5, 5)))
    midi.addNote(track, channel, note, time, duration, velocity)

def add_marker(midi, text, time):
    midi.addTrackName(0, time, text)

def parse_and_add_midi_fill(midi, track, channel, start_bar, fill_file):
    try:
        mid = mido.MidiFile(fill_file)
        start_time = start_bar * 4
        for msg in mid:
            if not msg.is_meta and msg.type == 'note_on' and msg.velocity > 0:
                midi.addNote(track, channel, msg.note, start_time + (msg.time / 480), 0.25, msg.velocity)
    except Exception as e:
        print(f"Ошибка при парсинге перехода {fill_file}: {e}")

def add_fill(midi, track, channel, start_bar, mapping, genre):
    path = os.path.join("fills_library", genre)
    fill_file = None
    if os.path.exists(path):
        files = [f for f in os.listdir(path) if f.endswith('.mid')]
        if files:
            fill_file = os.path.join(path, random.choice(files))
    
    if fill_file:
        parse_and_add_midi_fill(midi, track, channel, start_bar, fill_file)
    else:
        add_note_with_feel(midi, track, channel, mapping.get('crash_1', 49), start_bar * 4, 1, 120)
        toms = [mapping.get('tom_high', 48), mapping.get('tom_mid', 45), mapping.get('tom_low', 43)]
        for i, tom in enumerate(toms):
            add_note_with_feel(midi, track, channel, tom, start_bar * 4 + i*0.5, 0.5, 110)

def add_standard_beat(midi, track, channel, start_bar, mapping, energy=1):
    for beat in range(4):
        time = start_bar * 4 + beat
        if beat == 0 or beat == 2:
            add_note_with_feel(midi, track, channel, mapping['kick'], time, 1, 100)
        if beat == 1 or beat == 3:
            add_note_with_feel(midi, track, channel, mapping['snare_center'], time, 1, 105)
        steps = 4 if energy > 1 else 2
        for i in range(steps):
            add_note_with_feel(midi, track, channel, mapping['hat_closed_tip'], time + i*(1/steps), 0.25, 80)

def generate_full_track(filename, instrument, genre, intro, verses, chorus, bridge, outro, add_bass=False, bass_instrument="", selected_key="C"):
    mapping, drum_channel = get_mapping(instrument)
    midi = MIDIFile(2)
    midi.addTempo(0, 0, 160)
    midi.addTempo(1, 0, 160)
    current_bar = 0

    # --- Барабаны ---
    def process_drums(bar_count, is_chorus=False):
        nonlocal current_bar
        for b in range(bar_count):
            if not is_chorus and isinstance(verses, tuple) and verses[2] and b == (verses[1] // 2) - 1:
                add_fill(midi, 0, drum_channel, current_bar + b, mapping, genre)
            else:
                add_standard_beat(midi, 0, drum_channel, current_bar + b, mapping, energy=2 if is_chorus else 1)
        current_bar += bar_count

    if intro > 0: process_drums(intro)
    num_v, len_v, _ = verses
    for v in range(num_v):
        process_drums(len_v)
        process_drums(chorus, is_chorus=True)
    if bridge > 0: process_drums(bridge)
    if outro > 0: process_drums(outro)

    # --- Бас ---
    if add_bass and bass_instrument:
        from utilities.bass_mappings import get_bass_mapping
        b_map, b_chan = get_bass_mapping(bass_instrument)
        root_note = 36 + KEY_OFFSETS[selected_key]
        midi.addTrackName(1, 0, "Bass Line")
        
        for b in range(current_bar):
            # Ритмичный рисунок: Root на 1-ю долю, Октава на 3-ю
            if "Ample Bass" in bass_instrument:
                midi.addNote(1, b_chan, 24, b * 4, 0.1, 100) # Keyswitch
            midi.addNote(1, b_chan, root_note, b * 4, 2, 110)
            midi.addNote(1, b_chan, root_note + 12, b * 4 + 2, 2, 100)

    with open(filename, "wb") as f:
        midi.writeFile(f)