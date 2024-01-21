m = []
x = 0
c = 0
y = 0
z = 0
a = 0
b = 0
pr1 = 0
pc1 = 0
pr2 = 0
pc2 = 0
print("Tic Tac Toe")
print("-----------")
print()
print("player 1 -> X")
print("player 2 -> O")
print()
for i in range(3):
    a = []
    for j in range(3):
        a.append(".")
    m.append(a)
for i in range(3):
    for j in range(3):
        print(m[i][j], end=" ")
    print()
print()
while x == 0:
    while c == 0:
        print("player 1:")
        pr1 = int(input("row: "))
        pc1 = int(input("col: "))
        print()
        if (0 < pr1 <= 3) and (0 < pc1 <= 3):
            for e in range(1):
                for f in range(1):
                    if m[pr1 - 1][pc1 - 1] == ".":
                        m[pr1 - 1][pc1 - 1] = "X"
                        for i in range(3):
                            for j in range(3):
                                print(m[i][j], end=" ")
                            print()
                        print()
                        a = 0
                        while a == 0:
                            if (m[0][0] == m[0][1] == m[0][2] == "X") or (m[0][2] == m[1][2] == m[2][2] == "X") or (
                                    m[2][2] == m[2][1] == m[2][0] == "X") or (m[2][0] == m[1][0] == m[0][0] == "X") or (
                                    m[0][0] == m[1][1] == m[2][2] == "X") or (m[0][2] == m[1][1] == m[2][0] == "X") or (
                                    m[0][1] == m[1][1] == m[2][1] == "X") or (m[1][0] == m[0][1] == m[1][2] == "X"):
                                print("player 1 wins")
                                x = 1
                                c = 2
                                a = 1
                            elif (m[0][0] != "." and m[0][1] != "." and m[0][2] != "." and m[1][0] != "."
                                  and m[1][1] != "." and m[1][2] != "." and m[2][0] != "." and m[2][1] != "."
                                  and m[2][2] != "."):
                                print("its a draw")
                                x = 1
                                c = 2
                                a = 1
                            else:
                                c = 1
                                a = 1
                                print()
                    else:
                        print("already taken, choose another spot")
                        c = 0
                        y = 0
                        print()
        else:
            print("invalid input")
            print("enter input between 1 and 3")
            print()
            y = 0
            c = 0
    while c == 1:
        print("player 2:")
        pr2 = int(input("row: "))
        pc2 = int(input("col: "))
        print()
        if (0 < pr2 <= 3) and (0 < pc2 <= 3):
            for e in range(1):
                for f in range(1):
                    if m[pr2 - 1][pc2 - 1] == ".":
                        m[pr2 - 1][pc2 - 1] = "O"
                        for i in range(3):
                            for j in range(3):
                                print(m[i][j], end=" ")
                            print()
                        print()
                        b = 0
                        while b == 0:
                            if (m[0][0] == m[0][1] == m[0][2] == "O") or (m[0][2] == m[1][2] == m[2][2] == "O") or (
                                    m[2][2] == m[2][1] == m[2][0] == "O") or (m[2][0] == m[1][0] == m[0][0] == "O") or (
                                    m[0][0] == m[1][1] == m[2][2] == "O") or (m[0][2] == m[1][1] == m[2][0] == "O") or (
                                    m[0][1] == m[1][1] == m[2][1] == "O") or (m[1][0] == m[0][1] == m[1][2] == "O"):
                                print("player 2 wins")
                                x = 1
                                c = 2
                                b = 1
                            elif (m[0][0] != "." and m[0][1] != "." and m[0][2] != "." and m[1][0] != "." and
                                  m[1][1] != "." and m[1][2] != "." and m[2][0] != "." and m[2][1] != "." and
                                  m[2][2] != "."):
                                print("its a draw")
                                x = 1
                                c = 2
                                a = 1
                            else:
                                c = 0
                                b = 1
                                print()
                    else:
                        print("already taken, choose another spot")
                        c = 1
                        z = 0
                        print()
        else:
            print("invalid input")
            print("enter input between 1 and 3")
            print()
            z = 0
            c = 1
