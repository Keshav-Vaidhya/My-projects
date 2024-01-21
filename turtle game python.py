import turtle as tu
import random
import time

sc = tu.Screen()
sc.title("Turtle Race")
sc.bgcolor("light blue")

#player one
player1 = tu.Turtle()
#colour of p1
player1.color("red")
player1.shape("turtle")

#player two
player2 = player1.clone()
player2.color("blue")

player3 = player1.clone()
player3.color("green")

player4 = player1.clone()
player4.color("yellow")

#cursor for finish
finish = tu.Turtle()
finish.hideturtle()
finish.color("black")
finish.penup()

style = ["Arial", 14, "italic"]

#position the players
player1.penup()
player1.goto(-300, 100)
player1.write("P1", move=True, font=style, align="right")
player2.penup()
player2.goto(-300, 50)
player2.write("P2", font=style, align="right")
player3.penup()
player3.goto(-300, 0)
player3.write("P3", font=style, align="right")
player4.penup()
player4.goto(-300, -50)
player4.write("P4", font=style, align="right")

#finish line
finish.goto(250, -150)
finish.left(90)
finish.pendown()
finish.color("black")
finish.forward(300)
finish.write("Finish Line", font=style, align="right")

player1.pendown()
player2.pendown()
player3.pendown()
player4.pendown()

#values for the die
die = [1, 2, 3, 4, 5, 6]

#lesssgooo


def game():
    die_roll1 = random.choice(die)
    player1.forward(30 * die_roll1)
    player1.dot()
    time.sleep(1)
    die_roll2 = random.choice(die)
    player2.forward(30 * die_roll2)
    player2.dot()
    time.sleep(1)
    die_roll3 = random.choice(die)
    player3.forward(30 * die_roll3)
    player3.dot()
    time.sleep(1)
    die_roll4 = random.choice(die)
    player4.forward(30 * die_roll4)
    player4.dot()
    time.sleep(1)

    for i in range(30):
        if player1.pos() >= (250, 100):
            print("Player one wins")
            finish.penup()
            finish.left(90)
            finish.goto(250, 100)
            finish.pendown()
            finish.color("red")
            finish.write("Player one wins!", font=style, align="right")
            break
        elif player2.pos() >= (250, 50):
            print("Player two wins")
            finish.penup()
            finish.left(90)
            finish.goto(250, 50)
            finish.pendown()
            finish.color("blue")
            finish.write("Player two wins!", font=style, align="right")
            break
        elif player3.pos() >= (250, 0):
            print("Player three wins")
            finish.penup()
            finish.left(90)
            finish.goto(250, 0)
            finish.pendown()
            finish.color("green")
            finish.write("Player three wins!", font=style, align="right")
            break
        elif player4.pos() >= (250, -50):
            print("Player four wins")
            finish.penup()
            finish.left(90)
            finish.goto(250, -50)
            finish.pendown()
            finish.color("yellow")
            finish.write("Player four wins!", font=style, align="right")
            break
        else:
            game()            
def close():
    tu.Screen().bye()

sc.listen()
sc.onkeypress(game, "s")
sc.onkeypress(close, "x")

tu.done()
