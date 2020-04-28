import tkinter.messagebox
from tkinter import *


root=Tk()
root.geometry("1350x750+0+0")
root.title("Avinav's KATA KUTI")
root.configure(background='Cadet Blue')

tops = Frame(root, bg='Lavender Blush', pady=2, width=1350, height=100, relief=SUNKEN)
tops.grid(row=0, column=0)
label_title = Label(tops, font=('ALGERIAN', 50 , 'bold'), text="Avinav's KATA KUTI", bd=21, bg='Cadet Blue', fg= 'Cornsilk', justify=CENTER)
label_title.grid(row=0, column=0)

mainframe = Frame(root, bg='Powder Blue', bd=10, pady=2, width=1350, height=600, relief=SUNKEN)
mainframe.grid(row=1, column=0)

leftframe = Frame(mainframe, bg='Green', bd=10, pady=2, padx=10, width=750, height=500, relief=SUNKEN)
leftframe.pack(side=LEFT)

rightframe = Frame(mainframe, bg='Yellow',bd=10, pady=2, padx=10, width=800, height=700, relief=SUNKEN)
rightframe.pack(side=RIGHT)

rightframe1 = Frame(rightframe, bg='Yellow',bd=10, pady=2, padx=10, width=500, height=200, relief=SUNKEN)
rightframe1.grid(row=0, column=0)

rightframe2 = Frame(rightframe, bg='Yellow',bd=10, pady=2, padx=10, width=500, height=200, relief=SUNKEN)
rightframe2.grid(row=1, column=0)







playerX = IntVar()
playerO = IntVar()

playerX.set(0)
playerO.set(0)

button = StringVar()
click=True

def checkbutton(button):
    global click
    if button["text"] == " " and click==True :
        button.config(text="X")
        click=False
    elif button["text"] == " " and click==False :
        button.config(text="O")
        click=True
    rules()


def reset():
    button1.config(text=" ")
    button2.config(text=" ")
    button3.config(text=" ")
    button4.config(text=" ")
    button5.config(text=" ")
    button6.config(text=" ")
    button7.config(text=" ")
    button8.config(text=" ")
    button9.config(text=" ")

    button1.config(bg="gainsboro")
    button2.config(bg="gainsboro")
    button3.config(bg="gainsboro")
    button4.config(bg="gainsboro")
    button5.config(bg="gainsboro")
    button6.config(bg="gainsboro")
    button7.config(bg="gainsboro")
    button8.config(bg="gainsboro")
    button9.config(bg="gainsboro")




def rules():
    if button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X":
        button1.config(bg='cadet blue')
        button2.config(bg='cadet blue')
        button3.config(bg='cadet blue')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congrats,you have just won the game!")


    if button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X":
        button4.config(bg='blue')
        button5.config(bg='blue')
        button6.config(bg='blue')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congrats,you have just won the game!")


    if button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X":
        button7.config(bg='green')
        button8.config(bg='green')
        button9.config(bg='green')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congrats,you have just won the game!")

    if button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X":
        button1.config(bg='lavender blush')
        button5.config(bg='lavender blush')
        button9.config(bg='lavender blush')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congrats,you have just won the game!")

    if button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X":
        button3.config(bg='orange')
        button5.config(bg='orange')
        button7.config(bg='orange')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congrats,you have just won the game!")

    if button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X":
        button1.config(bg='yellow')
        button4.config(bg='yellow')
        button7.config(bg='yellow')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congrats,you have just won the game!")

    if button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X":
        button2.config(bg='yellow')
        button5.config(bg='yellow')
        button8.config(bg='yellow')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congrats,you have just won the game!")

    if button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X":
        button3.config(bg='yellow')
        button6.config(bg='yellow')
        button9.config(bg='yellow')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Congrats,you have just won the game!")



    if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg='cadet blue')
        button2.config(bg='cadet blue')
        button3.config(bg='cadet blue')
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congrats,you have just won the game!")

    if button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.config(bg='blue')
        button5.config(bg='blue')
        button6.config(bg='blue')
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congrats,you have just won the game!")

    if button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg='green')
        button8.config(bg='green')
        button9.config(bg='green')
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congrats,you have just won the game!")

    if button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg='powder blue')
        button5.config(bg='powder blue')
        button9.config(bg='powder blue')
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congrats,you have just won the game!")

    if button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.config(bg='orange')
        button5.config(bg='orange')
        button7.config(bg='orange')
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congrats,you have just won the game!")

    if button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.config(bg='yellow')
        button4.config(bg='yellow')
        button7.config(bg='yellow')
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congrats,you have just won the game!")

    if button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.config(bg='yellow')
        button5.config(bg='yellow')
        button8.config(bg='yellow')
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congrats,you have just won the game!")

    if button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.config(bg='yellow')
        button6.config(bg='yellow')
        button9.config(bg='yellow')
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congrats,you have just won the game!")

    if (button1["text"]!=" " and button2["text"]!=" " and button3["text"]!=" " and button4["text"]!=" " and button5["text"]!=" " and button6["text"]!=" " and button7["text"]!=" " and button8["text"]!=" " and button9["text"]!=" ") :
        button1.config(bg="powder blue")
        button2.config(bg="powder blue")
        button3.config(bg="powder blue")
        button4.config(bg="powder blue")
        button5.config(bg="powder blue")
        button6.config(bg="powder blue")
        button7.config(bg="powder blue")
        button8.config(bg="powder blue")
        button9.config(bg="powder blue")

        scoreX= float((playerX.get())+ 0.5)
        playerX.set(scoreX)
        scoreY = float((playerO.get())+0.5)
        playerO.set(scoreY)
        tkinter.messagebox.showinfo("You both take 0.5 credits.","Game has tied!")




def newgame():
    reset()
    playerX.set(0)
    playerO.set(0)


right_label1 = Label(rightframe1, font=("Monotype Corsiva",20), text="Player X: ",bd=10,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
right_label1.grid(row=0, column=0)
txtplayerX =Entry(rightframe1, textvariable =playerX,width=16,bd=5,fg='black').grid(row=0,column=1)


right_label2 = Label(rightframe1, font=("Monotype Corsiva",20), text="Player O: ",bd=10,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
right_label2.grid(row=1, column=0)
txtplayerO = Entry(rightframe1,textvariable= playerO,width=16,bd=5,fg='black').grid(row=1, column=1)


btnreset = Button(rightframe2, text= "Reset", font=('ALGERIAN', 20, 'bold'), width=10, height=1,bg='gainsboro',command=lambda :reset())
btnreset.pack(side=TOP)

btnnewgame = Button(rightframe2, text= "New Game ", font=('ALGERIAN', 20, 'bold'), width=10, height=1,bg='gainsboro',command=lambda :newgame())
btnnewgame.pack(side=BOTTOM)

button1 = Button(leftframe, text= " ", font=('ALGERIAN', 50 , 'bold'), width=4, height=1,bg='gainsboro',command=lambda :checkbutton(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(leftframe, text= " ", font=('ALGERIAN', 50 , 'bold'), width=4, height=1,bg='gainsboro',command=lambda :checkbutton(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(leftframe, text= " ", font=('ALGERIAN', 50 , 'bold'), width=4, height=1,bg='gainsboro',command=lambda :checkbutton(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(leftframe, text= " ", font=('ALGERIAN', 50 , 'bold'), width=4, height=1,bg='gainsboro',command=lambda :checkbutton(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(leftframe, text= " ", font=('ALGERIAN', 50 , 'bold'), width=4, height=1,bg='gainsboro',command=lambda :checkbutton(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(leftframe, text= " ", font=('ALGERIAN', 50 , 'bold'), width=4, height=1,bg='gainsboro',command=lambda :checkbutton(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(leftframe, text= " ", font=('ALGERIAN', 50 , 'bold'), width=4, height=1,bg='gainsboro',command=lambda :checkbutton(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(leftframe, text= " ", font=('ALGERIAN', 50 , 'bold'), width=4, height=1,bg='gainsboro',command=lambda :checkbutton(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(leftframe, text= " ", font=('ALGERIAN', 50 , 'bold'), width=4, height=1,bg='gainsboro',command=lambda :checkbutton(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)


root.mainloop()