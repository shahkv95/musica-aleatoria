import pygame


def generate_sound(notes: str) -> str:
    frequency = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
    duration = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    sound_data = []
    for note in notes:
        index = ord(note.lower()) - ord("a")
        sound_data.append((frequency[index], duration[index]))

    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_data)
    return sound
