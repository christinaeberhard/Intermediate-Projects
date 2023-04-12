# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
result = [phonetics[letter] for letter in word]
print(result)
