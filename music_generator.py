import random
from lcg import LCG


class MusicGenerator:
    def __init__(self, pitches, chords):
        self.pitches = pitches
        self.chords = chords
        self.lcg = LCG(len(pitches), 1103515245, 12345)

    def generate_melody(self, num_notes):
        """
        Generates a random melody by selecting random notes from the list of pitches.
        """
        melody = []
        for _ in range(num_notes):
            pitch_index = self.lcg.generate(
                random.randint(0, len(self.pitches)))
            pitch = self.pitches[pitch_index]
            melody.append(pitch)
        return melody
