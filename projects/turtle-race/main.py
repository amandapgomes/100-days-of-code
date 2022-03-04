import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color (blue, "
                                                            "yellow, green, red, purple, orange):")
turtles = []
start = False

x = -150
for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.speed(0)
    turtle.goto(-230, x)
    x += 50
    turtles.append(turtle)

if user_bet:
    start = True

while start:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.color()[0]
            start = False
            if user_bet == winner:
                print(f"You win. The {winner} is the winner.")
            else:
                print(f"You lose. The {winner} is the winner.")

screen.exitonclick()