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
            self.master.word = random.choice(easy_list)
        elif diff == 'hard':
            self.master.word = random.choice(hard_list)

        self.master.change(SecondFrame) # switch window



class SecondFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title("Hangman")
        master.geometry("1000x800")
        master.resizable(False, False)

        self.word = master.word # get the value from the first screen

        self.score = 7
        self.display = list(len(self.word) * '_')


        # Place the hangman
        # TODO

        # Display the keyboard
        keyboard = Keyboard(self)
        keyboard.pack()

        # Place box for keeping track of word and sample word below
        word_box = tk.Frame(master, height=80, width=600, bd=5, bg='white')
        self.label = tk.Label(word_box, text=self.display)
        self.label.config(font=(None, 25))
        self.label.pack()
        lbl_txt = tk.Label(word_box, text=self.word)
        lbl_txt.pack()
        word_box.place(relx=0.5, y=700, anchor='n')

    def method(self, value):
        value = value.lower() # convert incoming value to lowercase to match word dict
        for i, char in enumerate(self.word):
            if char == value:
                self.display[i] = char

        self.label.config(text=self.display)

if __name__=="__main__":
    app=MainApp()
    app.mainloop()




