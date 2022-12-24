import src.music_generator.music_generator as music_generator


def main():
    pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    chords = ['C', 'F', 'G', 'Am']
    num_repeats = 4

    generator = music_generator.MusicGenerator(pitches, chords)
    melody = generator.generate_melody(16)
    progression = generator.generate_chord_progression(4)
    song = generator.generate_song(num_repeats)

    print("Melody:", melody)
    print("Chord progression:", progression)
    print("Song:", song)


if __name__ == '__main__':
    main()
