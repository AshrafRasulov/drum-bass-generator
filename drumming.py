from midiutil import MIDIFile

def create_pop_punk_midi(filename="drum_beat.mid", length_bars=4):
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, "Pop Punk Drums")
    midi.addTempo(track, time, 160)

    # Стандартный GM маппинг
    kick, snare, hat = 36, 38, 42

    for bar in range(length_bars):
        for beat in range(4):
            if beat == 0 or beat == 2:
                midi.addNote(track, 0, kick, bar*4 + beat, 1, 100)
            if beat == 1 or beat == 3:
                midi.addNote(track, 0, snare, bar*4 + beat, 1, 100)
            for i in range(2):
                midi.addNote(track, 0, hat, bar*4 + beat + i*0.5, 0.5, 80)

    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)
    print(f"Файл {filename} создан!")

if __name__ == "__main__":
    create_pop_punk_midi()