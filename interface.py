from tkinter import * 
from math import pi

win = Tk()

#configuration Menubar
def alert():
    print("alert")

menubar = Menu(win)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Réinitialiser", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=win.quit)
menubar.add_cascade(label="Option", menu=menu1)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

# configuration de la fenêtre
win.minsize(400, 400)
win.title("Solides")
win.iconbitmap("C:/Users/timol/Projets Visual Sudio Code/PythonEx/P3_solids_py/Cube.ico")
win.config(bg="gray")
win.config(menu=menubar)

# configuration des Frames
Frame1 = Frame(win, relief=GROOVE, bg="gray")
Frame1.pack(expand=1, padx=30, pady=30)

Frame2 = Frame(win, relief=GROOVE, bg="gray")
Frame2.pack(expand=1, padx=30, pady=30)

# MyString
mystring =IntVar(win)

# question
ask_type_solid = Label(Frame1, text="Quel est le type du solide dont vous voulez calculer le volume ?", bg="gray", font="white, 18", fg="white")
ask_type_solid.pack()

# creation des commandes des boutons
def cmd_B1():
    print("cmd_B1")
    Label(Frame2, text="Longeur de l'arête :                    ", bg="gray", font="white, 10", fg="white", anchor="nw").pack()
    value1 = Entry(Frame2, textvariable = mystring, bg="white", font=40).pack()
    def cmd_Br():
        print("cmd_Br")
        print(int(mystring.get()))
        print(type(mystring))
    Br = Button(Frame2, text ='Calculer', command = cmd_Br, font="gray, 15").pack(expand=1, padx=5, pady=5)

def cmd_B2():
    print("cmd_B2")
    Label(Frame2, text="Entrez les valeur nécessaires :", bg="gray", font="white, 15", fg="white").pack(side=TOP)
    Label(Frame2, text="Largeur :                                  ", bg="gray", font="white, 10", fg="white", anchor="nw").pack()
    value1 = Entry(Frame2, text="largeur", textvariable = mystring, bg="white", font=40).pack()
    Label(Frame2, text="Longeur :                                 ", bg="gray", font="white, 10", fg="white").pack()
    value2 = Entry(Frame2, text="longeur", textvariable = mystring, bg="white", font=40).pack()
    Label(Frame2, text="Profondeur :                             ", bg="gray", font="white, 10", fg="white").pack()
    value3 = Entry(Frame2, text="hauteur", textvariable = mystring, bg="white", font=40).pack()
    def cmd_Br():
        print("cmd_Br")
        result = value1 * value1 * value1
        Label(Frame2, text=result, padx=10, pady=10)
    Br = Button(Frame2, text ='Calculer', command = cmd_Br, font="gray, 15").pack(expand=1, padx=5, pady=5)

def cmd_B3():
    print("cmd_B3")
    value1 = Entry(Frame2, text="largeur", textvariable = mystring, bg="white", font=40).pack()
    value2 = Entry(Frame2, text="longeur", textvariable = mystring, bg="white", font=40).pack()
    def cmd_Br():
        print("cmd_Br")
        result = value1 * value1 * value1
        Label(Frame2, text=result, padx=10, pady=10)
    Br = Button(Frame2, text ='Calculer', command = cmd_Br, font="red, 15").pack(expand=1, padx=5, pady=5)

def cmd_B4():
    print("cmd_B4")
    value1 = Entry(Frame2, text="largeur", textvariable = mystring, bg="white", font=40).pack()
    value2 = Entry(Frame2, text="longeur", textvariable = mystring, bg="white", font=40).pack()
    value3 = Entry(Frame2, text="hauteur", textvariable = mystring, bg="white", font=40).pack()
    def cmd_Br():
        print("cmd_Br")
        result = value1 * value1 * value1
        Label(Frame2, text=result, padx=10, pady=10)
    Br = Button(Frame2, text ='Calculer', command = cmd_Br, font="red, 15").pack(expand=1, padx=5, pady=5)

def cmd_B5():
    print("cmd_B5")
    value1 = Entry(Frame2, text="largeur", textvariable = mystring, bg="white", font=40).pack()
    value2 = Entry(Frame2, text="longeur", textvariable = mystring, bg="white", font=40).pack()
    def cmd_Br():
        print("cmd_Br")
        result = value1 * value1 * value1
        Label(Frame2, text=result, padx=10, pady=10)
    Br = Button(Frame2, text ='Calculer', command = cmd_Br, font="gray, 15").pack(expand=1, padx=5, pady=5)

# creation des boutons
B1 = Button(Frame1, text ='Bouton 1', command = cmd_B1, font="gray, 18").pack(expand=1, padx=5, pady=5)
B2 = Button(Frame1, text ='Bouton 2', command = cmd_B2, font="gray, 18").pack(expand=1, padx=5, pady=5)
B3 = Button(Frame1, text ='Bouton 3', command = cmd_B3, font="gray, 18").pack(expand=1, padx=5, pady=5)
B4 = Button(Frame1, text ='Bouton 4', command = cmd_B4, font="gray, 18").pack(expand=1, padx=5, pady=5)
B5 = Button(Frame1, text ='Bouton 5', command = cmd_B5, font="gray, 18").pack(expand=1, padx=5, pady=5)

win.mainloop()