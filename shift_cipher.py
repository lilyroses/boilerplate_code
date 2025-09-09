# shift_ciper.py
from string import ascii_lowercase


def shift_cipher(letters, s, shift_val):
    LETTERS = list(letters)
    NUMS = list(range(0, len(LETTERS)))
    LETTER_MAP = dict(zip(LETTERS, NUMS))
    MAP_LETTER = dict(zip(NUMS, LETTERS))

    new_letters = ""
    
    for char in s:
        if char not in LETTERS:
            new_letters += char
        else:
            original_val = LETTER_MAP[char]
            new_val = original_val + shift_val
            new_val = new_val % len(LETTERS)
            new_char = MAP_LETTER[new_val]
            print(char, original_val, new_char, new_val)
            new_letters += new_char
    
    return new_letters


letters = ascii_lowercase
s = "qzmt-zixmtkozy-ivhz"
shift_val = 343
print(shift_cipher(letters, s, shift_val))