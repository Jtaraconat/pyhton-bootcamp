import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dictionary = {row.letter:row.code for (index,row) in df.iterrows()}

user_input = input("Type a word: ").upper()
phonetic_code = [code_dictionary[letter] for letter in user_input]
print(phonetic_code)