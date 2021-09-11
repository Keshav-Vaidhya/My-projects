import random
target = 0
sum1 = 0
sum2 = 0
c = 0
t = ""
t1 = " "
print("Hand Cricket")
print("------------")
print()
a = input("heads or tails: ")
b = random.randint(1, 2)
if b == 1:
    t1 = "heads"
else:
    t1 = "tails"
print("it's ", t1)

if a == "h":
    if b == 1:
        bb = input("bat or bowl: ")
        if bb == "bat":
            print("user chose to bat")
            while c == 0:
                print("your score: ", sum1)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum1 = sum1 + y
                    print("computer: ", x)
                    target = (sum1 - y) + 1

                    if x == y:
                        print("you are out")
                        print("user score: ", sum1 - y)
                        target = (sum1 - y) + 1
                        print("the target: ", target)
                        print()
                        c = 1
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 0
                    print()

            while c == 1:
                print("computer's score: ", sum2)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum2 = sum2 + x
                    print("computer: ", x)

                    if x == y:
                        print("the computer is out")
                        print("computer score: ", sum2 - x)
                        print("user wins")
                        c = 2
                    elif sum2 > target:
                        print("computer score: ", sum2)
                        print("computer wins")
                        c = 2
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 1
                    print()

        else:                               
            #if user chooses bowl
            print("user chose to bowl")
            while c == 0:
                print("computer score: ", sum2)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum2 = sum2 + x
                    print("computer: ", x)
                    target = (sum2 - x) + 1

                    if x == y:
                        print("the computer is out")
                        print("computer score: ", sum2 - x)
                        target = (sum2 - x) + 1
                        print("the target: ", target)
                        print()
                        c = 1
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 0
                    print()

            while c == 1:
                print("user score: ", sum1)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum1 = sum1 + y
                    print("computer: ", x)

                    if x == y:
                        print("you are out")
                        print("user score: ", sum1 - y)
                        print("computer wins")
                        c = 2
                    elif sum1 > target:
                        print("user score: ", sum1)
                        print("user wins")
                        c = 2
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 1
                    print()

    else:
        z = random.randint(0, 1)
        if z == 0:
            t = "bat"
        else:
            t = "bowl"

        if t == "bowl":
            print("computer chose to bowl")
            while c == 0:
                print("your score: ", sum1)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum1 = sum1 + y
                    print("computer: ", x)
                    target = (sum1 - y) + 1

                    if x == y:
                        print("you are out")
                        print("user score: ", sum1 - y)
                        target = (sum1 - y) + 1
                        print("the target: ", target)
                        print()
                        c = 1
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 0
                    print()

            while c == 1:
                print("computer's score: ", sum2)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum2 = sum2 + x
                    print("computer: ", x)

                    if x == y:
                        print("the computer is out")
                        print("computer score: ", sum2 - x)
                        print("user wins")
                        c = 2
                    elif sum2 > target:
                        print("computer score: ", sum2)
                        print("computer wins")
                        c = 2
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 1
                    print()

        else:                                   
            #if pc chooses to bowl
            print("computer chose to bat")
            while c == 0:
                print("computer score: ", sum2)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum2 = sum2 + x
                    print("computer: ", x)
                    target = (sum2 - x) + 1

                    if x == y:
                        print("the computer is out")
                        print("computer score: ", sum2 - x)
                        target = (sum2 - x) + 1
                        print("the target: ", target)
                        print()
                        c = 1
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 0
                    print()

            while c == 1:
                print("user score: ", sum1)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum1 = sum1 + y
                    print("computer: ", x)

                    if x == y:
                        print("you are out")
                        print("user score: ", sum1 - y)
                        print("computer wins")
                        c = 2
                    elif sum1 > target:
                        print("user score: ", sum1)
                        print("user wins")
                        c = 2
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 1
                    print()

else:
    if b == 2:
        bb = input("bat or bowl: ")
        if bb == "bat":
            print("user chose to bat")
            while c == 0:
                print("your score: ", sum1)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum1 = sum1 + y
                    print("computer: ", x)
                    target = (sum1 - y) + 1

                    if x == y:
                        print("you are out")
                        print("user score: ", sum1 - y)
                        target = (sum1 - y) + 1
                        print("the target: ", target)
                        print()
                        c = 1
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 0
                    print()

            while c == 1:
                print("computer's score: ", sum2)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum2 = sum2 + x
                    print("computer: ", x)

                    if x == y:
                        print("the computer is out")
                        print("computer score: ", sum2 - x)
                        print("user wins")
                        c = 2
                    elif sum2 > target:
                        print("computer score: ", sum2)
                        print("computer wins")
                        c = 2
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 1
                    print()

        else:  # if user chooses bowl
            print("user chose to bowl")
            while c == 0:
                print("computer score: ", sum2)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum2 = sum2 + x
                    print("computer: ", x)
                    target = (sum2 - x) + 1

                    if x == y:
                        print("the computer is out")
                        print("computer score: ", sum2 - x)
                        target = (sum2 - x) + 1
                        print("the target: ", target)
                        print()
                        c = 1
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 0
                    print()

            while c == 1:
                print("user score: ", sum1)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum1 = sum1 + y
                    print("computer: ", x)

                    if x == y:
                        print("you are out")
                        print("user score: ", sum1 - y)
                        print("computer wins")
                        c = 2
                    elif sum1 > target:
                        print("user score: ", sum1)
                        print("user wins")
                        c = 2
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 1
                    print()

    else:
        z = random.randint(0, 1)
        if z == 0:
            t = "bat"
        else:
            t = "bowl"

        if t == "bowl":
            print("computer chose to bowl")
            while c == 0:
                print("your score: ", sum1)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum1 = sum1 + y
                    print("computer: ", x)
                    target = (sum1 - y) + 1

                    if x == y:
                        print("you are out")
                        print("user score: ", sum1 - y)
                        target = (sum1 - y) + 1
                        print("the target: ", target)
                        print()
                        c = 1
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 0
                    print()

            while c == 1:
                print("computer's score: ", sum2)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum2 = sum2 + x
                    print("computer: ", x)

                    if x == y:
                        print("the computer is out")
                        print("computer score: ", sum2 - x)
                        print("user wins")
                        c = 2
                    elif sum2 > target:
                        print("computer score: ", sum2)
                        print("computer wins")
                        c = 2
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 1
                    print()

        else:  # if pc chooses to bat
            print("computer chose to bat")
            while c == 0:
                print("computer score: ", sum2)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum2 = sum2 + x
                    print("computer: ", x)
                    target = (sum2 - x) + 1

                    if x == y:
                        print("the computer is out")
                        print("computer score: ", sum2 - x)
                        target = (sum2 - x) + 1
                        print("the target: ", target)
                        print()
                        c = 1
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 0
                    print()

            while c == 1:
                print("user score: ", sum1)
                y = int(input("user: "))
                if 1 <= y <= 6:
                    x = random.randint(1, 6)
                    sum1 = sum1 + y
                    print("computer: ", x)

                    if x == y:
                        print("you are out")
                        print("user score: ", sum1 - y)
                        print("computer wins")
                        c = 2
                    elif sum1 > target:
                        print("user score: ", sum1)
                        print("user wins")
                        c = 2
                    else:
                        print()
                else:
                    print("number out of range, enter input between 1 and 6")
                    c = 1
                    print()
