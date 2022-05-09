import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)


def generate_nato():
    word = input("Enter a word: ").upper()
    try:
        nato_for_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato()
    else:
        print(nato_for_word)


generate_nato()
