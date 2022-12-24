# An overview of the project's main components and functionality

The lcg-music-gen project is a music generator that uses a linear congruential generator (LCG) to create melodies and chord progressions.
The project consists of three main components:

- MusicGenerator Class
- LCG Class
- music_generator module

## MusicGenerator class

The MusicGenerator class is the main interface for generating music. It has the following methods:

- **generate_melody(num_notes: int) -> List[str]:** generates a melody with the specified number of pitches
- **generate_chord_progression(num_chords: int) -> List[str]:** generates a chord progression with the specified number of chords
- **generate_song(num_repeats: int) -> List[Union[str, Tuple[str, str]]]:** generates a song by repeating the melody and chord progression a specified number of times

## LCG class

The LCG class is a helper class that generates random integers using a linear congruential generator (LCG) algorithm.
It has the following methods:

- **generate(seed: int) -> int:** generates a random integer using the LCG algorithm
  music_generator.py module

## music_generator module

It contains the implementation of the MusicGenerator class. It imports the LCG class and uses it to generate melodies and chord progressions.

## Functionality

The lcg-music-gen project allows users to generate melodies and chord progressions using a simple interface. The user can specify the pitches and chords to be used, as well as the number of notes and chords in the generated melodies and chord progressions. The user can also specify the number of times the melody and chord progression should be repeated to generate a complete song.

The project uses an LCG algorithm to randomly select pitches and chords from the provided list. This allows for a large variety of melodies and chord progressions to be generated without requiring a large amount of pre-generated content.
