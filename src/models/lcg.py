class LCG:
    def __init__(self, modulus, multiplier, increment):
        if modulus == 0:
            self.modulus = 1
        else:
            self.modulus = modulus
        self.multiplier = multiplier
        self.increment = increment

    def generate(self, seed):
        """
        Generates a random integer using a linear congruential generator (LCG).
        """
        seed = (self.multiplier * seed + self.increment) % self.modulus
        return seed
