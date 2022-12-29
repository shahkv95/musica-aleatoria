from src.music_generator.music_generator import MusicGenerator


def test_lcg_class_exists():
    """Test that the LCG class can be imported from the music_generator module and that an instance of the LCG class can be created."""
    from src.models.lcg import LCG

    lcg = LCG(123, 456, 789)
    assert isinstance(lcg, LCG)


def test_generate_melody_returns_list_of_pitches():
    """Test that the generate_melody method returns a list of pitches that are contained in the pitches provided to the MusicGenerator object."""
    mg = MusicGenerator(pitches=["C", "D", "E"], chords=[])
    melody = mg.generate_melody(num_notes=3)
    assert all(pitch in ["C", "D", "E"] for pitch in melody)


def test_generate_chord_progression_returns_list_of_chords():
    """Test that the generate_chord_progression method returns a list of chords with the correct length and containing only valid chords."""
    mg = MusicGenerator(pitches=[], chords=["C", "F", "G"])
    progression = mg.generate_chord_progression(num_chords=3)
    assert len(progression) == 3
    assert all(chord in ["C", "F", "G"] for chord in progression)


def test_generate_chord_progression_returns_correct_length():
    """Test that checks that the generate_chord_progression method returns a list of the correct length."""
    mg = MusicGenerator(pitches=[], chords=["C", "F", "G"])
    progression = mg.generate_chord_progression(num_chords=3)
    assert len(progression) == 3


def test_generate_song_returns_list_of_measures():
    """Test that the generate_song function in the MusicGenerator class returns a list of measures. It also checks that the length of the returned list is correct."""
    mg = MusicGenerator(pitches=["C", "D", "E", "F"], chords=["C", "F", "G"])
    song = mg.generate_song(num_repeats=3)
    assert isinstance(song, list)
    assert len(song) == 3 * (16 + 4)


def test_generate_melody():
    """Test that the generate_melody function in the MusicGenerator class returns a list of pitches of the correct length. It also checks that all the pitches in the returned list are in the list of pitches that were passed to the MusicGenerator constructor."""
    pitches = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    generator = MusicGenerator(pitches, [])
    melody = generator.generate_melody(16)
    assert len(melody) == 16
    assert all(pitch in pitches for pitch in melody)


def test_generate_chord_progression():
    """Test that the generate_chord_progression function in the MusicGenerator class returns a list of chords of the correct length. It also checks that all the chords in the returned list are in the list of chords that were passed to the MusicGenerator constructor."""
    chords = ["C", "F", "G", "Am"]
    generator = MusicGenerator([], chords)
    progression = generator.generate_chord_progression(4)
    assert len(progression) == 4
    assert all(chord in chords for chord in progression)


def test_generate_song():
    """that the generate_song function in the MusicGenerator class returns a list of measures of the correct length."""
    pitches = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    chords = ["C", "F", "G", "Am"]
    generator = MusicGenerator(pitches, chords)
    song = generator.generate_song(4)
    assert len(song) == 4 * (16 + 4)
    # assert all(pitch in pitches or chord in chords for pitch, chord in song)
