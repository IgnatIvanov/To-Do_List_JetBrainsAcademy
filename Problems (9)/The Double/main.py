# put your python code here
from string import ascii_lowercase

double_alphabet = {}

for letter in ascii_lowercase:
    double_alphabet[str(letter)] = str(letter + letter)