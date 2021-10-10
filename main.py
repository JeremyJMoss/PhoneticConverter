import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter: row.code for (key, row) in data.iterrows()}

print("Welcome to the Phonetic Alphabet Converter")
user_input = input("Write a word you would like to convert to phonetic alphabet.\n")
phonetic_list = []
for single_letter in user_input:
    phonetic_list.append(phonetic_alphabet[single_letter.upper()])

print(phonetic_list)
