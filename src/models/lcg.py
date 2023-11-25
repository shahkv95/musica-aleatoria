class LCG:
    def __init__(self, modulus: int, multiplier: int, increment: int) -> None:
        if modulus == 0:
            self.modulus = 1
        else:
            self.modulus = modulus
        self.multiplier = multiplier
        self.increment = increment

    def generate(self, seed: int) -> int:
        """
        Generates a random integer using a linear congruential generator (LCG).
        """
        seed = (self.multiplier * seed + self.increment) % self.modulus
        return seed
