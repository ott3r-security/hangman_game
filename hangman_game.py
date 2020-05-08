#!/usr/bin/env python3

import tkinter as tk
from word_dicts import easy_list, hard_list, master_dict
from tkinter import ttk
import random
from keyboard import Keyboard


class MainApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = ChooseDifficulty(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack()



class ChooseDifficulty(tk.Frame):
    # First window. Choose easy or hard.
    def __init__(self, master=None, word='', *args, **kwargs):
        ChooseDifficulty.word = word
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Hangman")
        master.geometry("300x200")

        lbl = tk.Label(self, text='Choose Word Difficulty')
        lbl.pack()

        btn_easy = ttk.Button(self, text="Easy", command=lambda : self.check('easy'))
        btn_easy.pack()
        btn_hard = ttk.Button(self, text="Hard", command=lambda : self.check('hard'))
        btn_hard.pack()
        btn_quit = ttk.Button(self, text="Quit", command=self.quit)
        btn_quit.pack()

        lbl_g = tk.Label(self, text='Classic Hangman Game')
        lbl_g.pack()
        lbl_n = tk.Label(self, text='erok81 2020')
        lbl_n.pack()


    def check(self, diff):

        if diff == 'easy':
            ChooseDifficulty.word = random.choice(easy_list)
            return self.master.change(SecondFrame), ChooseDifficulty.word
        elif diff == 'hard':
            ChooseDifficulty.word = random.choice(hard_list)
            return self.master.change(SecondFrame), ChooseDifficulty.word




class SecondFrame(tk.Frame):

    def __init__(self, master=None, **kwargs):

        tk.Frame.__init__(self, master, **kwargs)

        master.title("Hangman")
        master.geometry("1000x800")
        # ~ master.resizable(False, False)

        self.score = 7
        self.display = list(len(ChooseDifficulty.word) * '_')


        # Place the hangman
        # TODO


        # Place box for keeping track of word and sample word below
        word_box = tk.Frame(master, height=80, width=600, bd=5, bg='white')
        label = tk.Label(word_box, text=self.display)
        label.config(font=(None, 25))
        label.pack()
        lbl_txt = tk.Label(word_box, text=ChooseDifficulty.word)
        lbl_txt.pack()
        word_box.place(relx=0.5, y=700, anchor='n')

        # Display the keyboard
        keyboard = Keyboard(self)
        keyboard.pack()

    def method(self, value):
        print("MainApp method called with value", value)

        return value



# Game play from tkinter test for later
# def update_txt(l, t):
#     global score
#     global display
#     # l is letter to find
#     # t is original text to guess
#     # i is index list
#     # d is display word with hidden letters
#     # s is score which starts at 7
#     i = [i for i, ltr in enumerate(t) if ltr == l]
#     if i == []:
#         score -= 1
#         # print turle sections here
#         print('wrong guess')
#         return score
#     elif l in display:
#         print('You\'ve guesed that already')
#     else:
#         for nums in i:
#             display[nums] = l
#             print(display)
#     return display



if __name__=="__main__":
    app=MainApp()
    app.mainloop()




