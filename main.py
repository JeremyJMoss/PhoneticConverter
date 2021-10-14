import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter: row.code for (key, row) in data.iterrows()}

print("Welcome to the Phonetic Alphabet Converter")

not_a_word = True

while not_a_word:
    user_input = input("Write a word you would like to convert to phonetic alphabet.\n").upper()
    try:
        phonetic_list = [phonetic_alphabet[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        not_a_word = False

print(phonetic_list)
