•	import tkinter as tk
from tkinter import messagebox
from random import randrange


wnd = tk.Tk()
wnd.title("TicTacToe")


# Write your code here.
def gameover(ch):
    if ch == 'O':
        messagebox.showinfo('Game over!', 'You win!')
    else:
        messagebox.showinfo('Game over!', 'PC win!')
    return 1

def check(ch):
    ic = 0
    r = 0
    for j in range(3):
        ic = 0
        for i in range(3):
            if c[i][j]['text'] == ch:
                ic += 1
            if ic ==3:
                r = gameover(ch)
    for i in range(3):
        ic = 0
        for j in range(3):
            if c[i][j]['text'] == ch:
                ic += 1
            if ic ==3:
                r = gameover(ch)
    ic = 0
    for i in range(3):
        if c[i][i]['text'] == ch:
            ic += 1
    if ic == 3:
        r = gameover(ch)
    ic = 0
    for i in range(2, -1, -1):
        if c[i][i]['text'] == ch:
            ic += 1
    if ic == 3:
        r = gameover(ch)
    return r

def opp(event):
    if event.widget['text'] == '':
        event.widget.config(text='O', fg='green')
        if check('O') == 1:
            wnd.destroy()
            return
        i = randrange(3)
        j = randrange(3)
        while c[i][j]['text'] != '':
            i = randrange(3)
            j = randrange(3)
        c[i][j].config(text='X', fg='red')
        if check('X') == 1:
            wnd.destroy()

wnd.bind_all('<Button-1>', opp)
c =[[0 for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        c[i][j] = tk.Label(wnd, width=10, height=5, bd=2, relief='raised')
        c[i][j].grid(row=j, column=i)
c[1][1].config(text='X', fg='red')
wnd.mainloop()
