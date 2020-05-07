import tkinter as tk
from word_dicts import easy_list, hard_list, master_dict
from tkinter import ttk
import random


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


    def check(self, diff):

        if diff == 'easy':
            ChooseDifficulty.word = random.choice(easy_list)
            return self.master.change(SecondFrame), ChooseDifficulty.word
        elif diff == 'hard':
            ChooseDifficulty.word = random.choice(hard_list)
            return self.master.change(SecondFrame), ChooseDifficulty.word
  



class SecondFrame(ChooseDifficulty, tk.Frame):

    def __init__(self, master=None, **kwargs):

        tk.Frame.__init__(self, master, **kwargs)
        master.title("Hangman")
        master.geometry("800x800")
        master.resizable(False, False)
        
        # Display word at top for testing
        lbl = tk.Label(self, text=ChooseDifficulty.word)
        lbl.pack()

        self.score = 7
        self.display = list(len(ChooseDifficulty.word) * '_')
    

        # Place the hangman

        # Place box for keeping track of word
        word_box = tk.Frame(master, height=80, width=600, bd=5, bg='white')
        label = tk.Label(word_box, text=self.display)
        label.config(font=(None, 25))
        label.pack()
        word_box.place(relx=0.5, y=525, anchor='n')

        



if __name__=="__main__":
    app=MainApp()
    app.mainloop()