import streamlit as st
import drumming
import os

st.set_page_config(page_title="Drum MIDI Generator", page_icon="🥁", layout="wide")
st.title("🥁 Drum MIDI Generator Pro")

# --- ГЛОБАЛЬНЫЕ НАСТРОЙКИ ---
project_name = st.text_input("Введите имя проекта (обязательно):", value="")
disabled = not project_name

tab1, tab2 = st.tabs(["Генератор", "Personality (Fills Library)"])

# --- ВКЛАДКА 1: ГЕНЕРАТОР ---
with tab1:
    col_vst1, col_vst2 = st.columns(2)
    with col_vst1:
        instrument = st.selectbox("Выберите VST барабанов:", ["HyperCanvas", "HyperQuarter", "Dummzz", "Addictive Drum", "EZDrummer"], disabled=disabled)
    with col_vst2:
        add_bass = st.checkbox("Добавить басовую линию", value=False, disabled=disabled)
        bass_instrument = st.selectbox("Выберите VST баса:", ["HyperCanvas", "Ample Bass P"], disabled=not add_bass or disabled)

    # ВЫБОР ТОНАЛЬНОСТИ
    keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    selected_key = st.selectbox("Выберите тональность:", keys, index=0, disabled=not add_bass or disabled)

    genre = st.selectbox("Жанр:", ["Pop-Punk", "Rock", "Metal"], disabled=disabled)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Куплеты")
        num_verses = st.slider("Количество куплетов", 1, 5, 2, disabled=disabled)
        verse_bars = st.slider("Длина куплета (BARs)", 4, 32, 16, disabled=disabled)
        use_mid_fill = st.checkbox("Переход в середине куплета", value=True, disabled=disabled)

    with col2:
        st.subheader("Припевы и части")
        chorus_bars = st.slider("Длина припева (BARs)", 4, 32, 16, disabled=disabled)
        intro_bars = st.slider("Intro (BARs)", 0, 16, 4, disabled=disabled)
        has_bridge = st.checkbox("Добавить Bridge", disabled=disabled)
        bridge_bars = st.slider("Длина Bridge (BARs)", 0, 24, 8, disabled=not has_bridge or disabled)
        outro_bars = st.slider("Outro (BARs)", 0, 16, 0, disabled=disabled)

    if st.button("Сгенерировать MIDI", disabled=disabled):
        filename = f"{project_name}.mid"
        drumming.generate_full_track(
            filename=filename, instrument=instrument, genre=genre,
            intro=intro_bars, verses=(num_verses, verse_bars, use_mid_fill),
            chorus=chorus_bars, bridge=bridge_bars, outro=outro_bars,
            add_bass=add_bass, bass_instrument=bass_instrument, selected_key=selected_key
        )
        st.success(f"Файл {filename} создан!")
        with open(filename, "rb") as f:
            st.download_button("Скачать MIDI", f, file_name=filename)

# --- ВКЛАДКА 2: PERSONALITY ---
with tab2:
    st.header("Загрузка ваших MIDI-переходов")
    fill_genre = st.selectbox("Выберите жанр для перехода:", ["Pop-Punk", "Rock", "Metal"], key="fill_genre")
    uploaded_file = st.file_uploader("Выберите MIDI файл перехода", type=['mid'])
    
    if uploaded_file and st.button("Сохранить переход"):
        save_path = os.path.join("fills_library", fill_genre)
        os.makedirs(save_path, exist_ok=True)
        files = os.listdir(save_path)
        new_index = len(files) + 1
        save_file = os.path.join(save_path, f"fill_{new_index:03d}.mid")
        with open(save_file, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Переход сохранен как {save_file}")