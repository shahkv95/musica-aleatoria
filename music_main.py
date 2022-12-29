import pygame

from play_music import generate_sound


def main():
    notes = input("Enter a series of notes (A-G): ")
    sound = generate_sound(notes)
    sound.play()


if __name__ == "__main__":
    main()
