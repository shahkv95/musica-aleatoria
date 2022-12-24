from src.music_generator import MusicGenerator


def test_lcg_class_exists():
    from src.music_generator import LCG
    lcg = LCG(123, 456, 789)
    assert isinstance(lcg, LCG)


def test_generate_melody_returns_list_of_pitches():
    mg = MusicGenerator(pitches=['C', 'D', 'E'], chords=[])
    melody = mg.generate_melody(num_notes=3)
    assert all(pitch in ['C', 'D', 'E'] for pitch in melody)


def test_generate_chord_progression_returns_list_of_chords():
    mg = MusicGenerator(pitches=[], chords=['C', 'F', 'G'])
    progression = mg.generate_chord_progression(num_chords=3)
    assert len(progression) == 3
    assert all(chord in ['C', 'F', 'G'] for chord in progression)


def test_generate_chord_progression_returns_correct_length():
    mg = MusicGenerator(pitches=[], chords=['C', 'F', 'G'])
    progression = mg.generate_chord_progression(num_chords=3)
    assert len(progression) == 3


def test_generate_song_returns_list_of_measures():
    # Create a MusicGenerator object with some pitches and chords
    mg = MusicGenerator(pitches=['C', 'D', 'E', 'F'], chords=['C', 'F', 'G'])

    # Call the generate_song method with a given number of repeats
    song = mg.generate_song(num_repeats=3)

    # Assert that the returned value is a list
    assert isinstance(song, list)

    # Assert that the length of the list is equal to the number of repeats * number of measures per repeat
    assert len(song) == 3 * (16 + 4)


def test_generate_melody():
    pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    generator = MusicGenerator(pitches, [])
    melody = generator.generate_melody(16)
    assert len(melody) == 16
    assert all(pitch in pitches for pitch in melody)


def test_generate_chord_progression():
    chords = ['C', 'F', 'G', 'Am']
    generator = MusicGenerator([], chords)
    progression = generator.generate_chord_progression(4)
    assert len(progression) == 4
    assert all(chord in chords for chord in progression)


def test_generate_song():
    pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    chords = ['C', 'F', 'G', 'Am']
    generator = MusicGenerator(pitches, chords)
    song = generator.generate_song(4)
    assert len(song) == 4 * (16 + 4)
    # assert all(pitch in pitches or chord in chords for pitch, chord in song)

# def test_generate_song_returns_list_of_expected_length():
#     mg = MusicGenerator(pitches=[], chords=['C', 'F', 'G'])
#     melody = ['A', 'B', 'C']
#     progression = ['C', 'F', 'G']
#     num_repeats = 2

#     song = mg.generate_song(num_repeats=num_repeats,
#                             melody=melody, progression=progression)

#     expected_length = len(melody) + len(progression)
#     assert len(song) == expected_length
