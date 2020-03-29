#_[N_F]_
from tkinter import *
from random import randrange
from clipboard import copy


root = Tk()


Va, Vb, Vc, Vd, Ve = IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
alphaA = '0123456789'
alphaB = 'abcdefghijklmnopqrstuvwxyz'
alphaC = alphaB.upper()
alphaD = "'!@#$%¨&*()_+-=§ªº°`{^}:?></;.,]~´[\|"


def click():
    global password, final
    final, alphabet = '', []
    try:
        password = int(box.get())
    except:
        password = len(box.get())
    if Va.get() == 1:
        alphabet.insert(1, alphaA)
    if Vb.get() == 1:
        alphabet.insert(1, alphaB)
    if Vc.get() == 1:
        alphabet.insert(1, alphaC)
    if Vd.get() == 1:
        alphabet.insert(1, alphaD)
    if Ve.get() == 1:
        alphabet.insert(1, ' ')
    if alphabet == []:
        alphabet.insert(1, alphaA)
    for i in range(password):
        P1 = randrange(0, len(alphabet))
        L2 = alphabet[P1]
        P2 = randrange(0, len(L2))
        final += L2[P2]
    label['text'] = final


def Copy():
    global final
    copy(final)


def TXT():
    global final
    Tex = open('password.txt', 'w')
    Tex.write('password : ' + final)
    Tex.close()


text = Label(root, text='len message : ', )
text.place(x=10, y=20)

box = Entry(root, width=20, font='calabri 12')
box.place(x=100, y=20)


alphaA_b = Checkbutton(root, variable=Va, text='numbers')
alphaB_b = Checkbutton(root, variable=Vb, text='letters')
alphaC_b = Checkbutton(root, variable=Vc, text='capital letters')
alphaD_b = Checkbutton(root, variable=Vd, text='symbols')
alphaE_b = Checkbutton(root, variable=Ve, text='spaces')
alphaA_b.place(x=10, y=60)
alphaB_b.place(x=10, y=80)
alphaC_b.place(x=10, y=100)
alphaD_b.place(x=150, y=60)
alphaE_b.place(x=150, y=80)


button = Button(root, width=25, font='calabri 12', text='GO!', command=click)
button.place(x=10, y=140)


label = Label(root, width=25, font='calabri 12', text='', background='white')
label.place(x=10, y=180)


copyButton = Button(root, width=5, font='calabri 12', text='copy', command=Copy)
copyButton.place(x=10, y=220)


buttonTXT = Button(root, width=10, font='calabri 12', text='create a .txt', command=TXT)
buttonTXT.place(x=100, y=220)


root.title('passwords')
root.geometry('300x300')
root.resizable(width=False, height=False)
root.mainloop()
