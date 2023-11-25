import random
from typing import List, Tuple, Union
from src.models.lcg import LCG


class MusicGenerator:
    def __init__(self, pitches: List[str], chords: List[str]) -> None:
        self.pitches = pitches
        self.chords = chords
        self.lcg = LCG(len(pitches), 1103515245, 12345)

    def generate_melody(self, num_notes: int) -> List[str]:
        """
        Generates a random melody by selecting random notes
        from the list of pitches.
        """
        melody = []
        for _ in range(num_notes):
            pitches_length = len(self.pitches)
            pitch_index = self.lcg.generate(random.randint(0, pitches_length))
            pitch = self.pitches[pitch_index]
            melody.append(pitch)
        return melody

    def generate_chord_progression(self, num_chords: int) -> List[str]:
        """
        Generates a random chord progression by selecting
        random chords from the list of chord symbols.
        """
        progression = []
        for _ in range(num_chords):
            chord_len = len(self.chords)
            chord_index = self.lcg.generate(random.randint(0, chord_len)) % len(
                self.chords
            )
            chord = self.chords[chord_index]
            progression.append(chord)
        return progression

    def generate_song(self, num_repeats: int) -> List[Union[str, Tuple[str, str]]]:
        """
        Generates a song structure by repeating
        a melody and chord progression.
        """
        song = []
        for _ in range(num_repeats):
            melody = self.generate_melody(16)
            progression = self.generate_chord_progression(4)
            song.extend(melody)
            song.extend(progression)
        return song
