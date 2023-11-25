# MUSICA ALEATORIA

<img src="https://github.com/shahkv95/musica-aleatoria/blob/main/assets/musica.png">

<hr>

Code generates random music using linear congruential generator (LCG) to select pitches & chords from predefined lists. LCG generates random integers based on modulus, multiplier, increment. Integers used to index lists and select pitches/chords. Pitches/chords combined to create melody/chord progression, repeated to form song structure. Code also defines functions for LCG, melody, chord progression, song structure.

## Setting up the project

### Pre-requisites

Python 3.6 or above

### Steps

- Clone the repository using the following command:
  `git clone https://github.com/shahkv95/lcg-music-gen.git`
- Change the current working directory to the project directory:
  `cd lcg-music-gen`
- Setup virtual environment: `PIPENV_VENV_IN_PROJECT=true pipenv shell`
- Install the dependencies using the following command:
  `pip install -r requirements.txt`
- Run the main file using the following command:
  `python3 main.py`

### Testing

Run the tests using the following command:
`pytest`
