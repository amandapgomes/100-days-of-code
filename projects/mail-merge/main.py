with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

for i in range(len(names)):
    names[i] = names[i].strip("\n")
    striped_name = names[i]
    with open("./Input/Letters/starting_letter.txt") as starting_letter:
        letter_file = starting_letter.read()
        new_letter = letter_file.replace("[name]", striped_name)
    with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as edited_letter:
        edited_letter.write(new_letter)
