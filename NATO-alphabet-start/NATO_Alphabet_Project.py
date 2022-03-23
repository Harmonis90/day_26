import pandas

# TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Convert a word to NATOs' phonetic alphabet.\n\t Word: ").upper()
natoify = [nato_dict[letter] for letter in user_input]
print(natoify)
