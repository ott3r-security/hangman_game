

import tkinter as tk
from word_dicts import easy_list, hard_list, master_dict
from tkinter import ttk
import random
from keyboard import Keyboard
import PIL
from PIL import ImageTk, Image



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
        master.geometry("900x550")
        master.resizable(False, False)

        self.word = master.word # get the value from the first screen
        self.chosen_list = []
        self.score = 7
        self.display = list(len(self.word) * '_')
        self.image = f'images/hangman{self.score}.png'
    
        # Place the hangman
        hangman_draw = tk.Frame(master, height=580, width=600)
        self.photo = tk.PhotoImage(file=self.image)
        photo_label = tk.Label(hangman_draw, image=self.photo)
        photo_label.pack()

        hangman_draw.place(relx=0.5, y=100, anchor='n')

        # Display the keyboard
        keyboard = Keyboard(self)
        keyboard.pack()

        # Place box for keeping track of word and sample word below
        word_box = tk.Frame(master, height=80, width=600, bd=5)
        self.label = tk.Label(word_box, text=self.display)
        self.label.config(font=(None, 25))
        self.label.pack()
        self.lbl_txt = tk.Label(word_box, text=self.chosen_list)
        self.lbl_txt.pack()
        word_box.place(relx=0.5, y=425, anchor='n')

    def method(self, value):
 
        value = value.lower() # convert incoming value to lowercase to match word dict

        for i, char in enumerate(self.word):
            if char == value:
                self.display[i] = char.upper()

        self.chosen_list.append(value)
 
        if self.word.upper() == ''.join(self.display):
            SecondFrame.winner()

        if value not in self.word and self.chosen_list.count(value) < 2:
            self.score -= 1
            self.image = (f'images/hangman{self.score}.png')

            if self.score == 1:
                SecondFrame.game_over()
     
        self.label.config(text=self.display)
        self.photo.config(file=self.image)
        # Take list of choices in lowercase, delete duplicates, and return upper case choices
        self.lbl_txt.config(text=' '.join(set(x.upper() for x in self.chosen_list)))
     
    #TODO 
    # Reset game. Current command kills app and doesn't play.
    
    def game_over():
        # Once score is 0 or word is guessed game needs to option to restart or quit
        x = app.winfo_x()
        y = app.winfo_y()
        
        popup = tk.Toplevel()
        popup.geometry("+%d+%d" % (x + 100, y + 50))
        popup.grab_set()
        popup.wm_title('Hangman')
        label = tk.Label(popup, text='You lose. Bill has died')
        label.pack(side=tk.TOP, pady=5, padx=5)
        button_close = tk.Button(popup, text="Quit", command=app.destroy, 
                                bg='red', activebackground='orange red', width=50)
        button_close.pack(side=tk.LEFT, pady=5, padx=5)
        button_play_again = tk.Button(popup, text="Play Again", command=lambda: [popup.destroy(), app.destroy(), MainApp()], 
                                    bg='green', activebackground='light green', width=50)
        button_play_again.pack(side=tk.LEFT, pady=5, padx=5)


    def winner():
        x = app.winfo_x()
        y = app.winfo_y()
        
        popup = tk.Toplevel()
        popup.geometry("+%d+%d" % (x + 100, y + 50))
        popup.grab_set()
        popup.wm_title('Hangman')
        label = tk.Label(popup, text='You win. Bill has returned to his family')
        label.pack(side=tk.TOP, pady=5, padx=5)
        button_close = tk.Button(popup, text="Quit", command=app.destroy, 
                                bg='red', activebackground='orange red', width=50)
        button_close.pack(side=tk.LEFT, pady=5, padx=5)
        button_play_again = tk.Button(popup, text="Play Again", command=lambda: [popup.destroy(), app.destroy(), MainApp(),],
                                    bg='green', activebackground='light green', width=50)
        button_play_again.pack(side=tk.LEFT, pady=5, padx=5)

    #TODO 
    # Reset game. Current command kills app and doesn't play.



if __name__=="__main__":
    app=MainApp()
    app.mainloop()




