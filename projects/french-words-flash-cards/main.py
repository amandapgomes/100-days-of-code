from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
word = {}
to_learn = {}

try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words_data = pandas.read_csv("data/french_words.csv")
    to_learn = french_words_data.to_dict(orient="records")
else:
    to_learn = words_data.to_dict(orient="records")


def new_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=word["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")


def is_know():
    to_learn.remove(word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="")

card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="")

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=1)

new_card()

window.mainloop()
