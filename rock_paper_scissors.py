import random
x = random.randint(0, 2)
c = ""
b = 0
print("Rock-Paper-Scissors")
print("-------------------")
print()

while b == 0:
    a = input("user: ")

    if a == "rock" or a == "paper" or a == "scissors":
        if x == 0:
            c = "rock"
        elif x == 1:
            c = "paper"
        else:
            c = "scissors"

        print("computer:", c)

        if (c == "rock" and a == "paper") or (c == "paper" and a == "scissors") or (c == "scissors" and a == "rock"):
            print("user wins")
        elif (c == "paper" and a == "rock") or (c == "scissors" and a == "paper") or (c == "rock" and a == "scissors"):
            print("computer wins")
        else:
            print("its a draw")

        g = input("Do you want to continue? y/n: ")
        print()
        if g == "y":
            b = 0
        else:
            b = 1
    else:
        print("invalid input, please enter either rock, paper or scissors")
        b = 0
        print()
