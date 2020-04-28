from tkinter import *

y = ""
x = 2
player_1 = []
player_2 = []
playerX = NONE
playerO = NONE




root = Tk()

l1 = Label(root, text="Player 1 : X", font="ALGERIAN")
l1.grid(row=0, column=0)

l2 = Label(root, text="Player 2 : O", font="ALGERIAN")
l2.grid(row=0, column=1)

b1 = Button(root, width=20, height=10, command=lambda: define_sign(1))
b1.grid(row=1, column=0)

b2 = Button(root, width=20, height=10, command=lambda: define_sign(2))
b2.grid(row=1, column=1)


b3 = Button(root, width=20, height=10, command=lambda: define_sign(3))
b3.grid(row=1, column=2)

b4 = Button(root, width=20, height=10, command=lambda: define_sign(4))
b4.grid(row=2, column=0)

b5 = Button(root, width=20, height=10, command=lambda: define_sign(5))
b5.grid(row=2, column=1)

b6 = Button(root, width=20, height=10, command=lambda: define_sign(6))
b6.grid(row=2, column=2)

b7 = Button(root, width=20, height=10, command=lambda: define_sign(7))
b7.grid(row=3, column=0)

b8 = Button(root, width=20, height=10, command=lambda: define_sign(8))
b8.grid(row=3, column=1)

b9 = Button(root, width=20, height=10, command=lambda: define_sign(9))
b9.grid(row=3, column=2)

def switchAndGetUser():
    global playerX
    global playerY

    if playerX:
        playerX=FALSE
        playerO=TRUE
        return "O"
    else:
        playerX=TRUE
        playerO=FALSE
        return "X"

def define_sign(number):
    y = ""
    x = 2
    player_1 = []
    player_2 = []


    if number == 1:
        if x % 2 == 0:
            y = "X"
            b1.configure(text=y)
            player_1.append(number)
            print(player_1)

        elif (x % 2) != 0:
            y = "Y"
            player_2.append(number)
            print(player_2)
            b1.configure(text=switchAndGetUser())
            x = x + 1````````````````````````

        if number == 2:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                print(player_1)

            elif x % 2 != 0:
                y = "Y"
                player_2.append(number)
                print(player_2)
                b2.configure(text=switchAndGetUser())
                x = x + 1

        if number == 3:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                print(player_1)

            elif x % 2 != 0:
                y = "Y"
                player_2.append(number)
                print(player_2)
                b3.configure(text=switchAndGetUser())
                x = x + 1

        if number == 4:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                print(player_1)

            elif x % 2 != 0:
                y = "Y"
                player_2.append(number)
                print(player_2)
                b4.configure(text=switchAndGetUser())
                x = x + 1

        if number == 5:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                print(player_1)

            elif x % 2 != 0:
                y = "Y"
                player_2.append(number)
                print(player_2)
                b5.configure(text=switchAndGetUser())
                x = x + 1

        if number == 6:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                print(player_1)

            elif x % 2 != 0:
                y = "Y"
                player_2.append(number)
                print(player_2)
                b6.configure(text=switchAndGetUser())
                x = x + 1

        if number == 7:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                print(player_1)

            elif x % 2 != 0:
                y = "Y"
                player_2.append(number)
                print(player_2)
                b7.configure(text=switchAndGetUser())

                x = x + 1

        if number == 8:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                print(player_1)

            elif x % 2 != 0:
                y = "Y"
                player_2.append(number)
                print(player_2)
                b8.configure(text=switchAndGetUser())
                x = x + 1

        if number == 9:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                print(player_1)

            elif x % 2 != 0:
                y = "Y"
                player_2.append(number)
                print(player_2)
                b9.configure(text=switchAndGetUser())
                x = x + 1


root.mainloop()
