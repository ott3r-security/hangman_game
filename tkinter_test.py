import tkinter as tk
from word_dicts import easy_dict, hard_dict, master_dict
import random

height = 800
width = 600


def press(letter):
    return letter


def keys():
    keyboard_frame = tk.Frame(root, height=150, width=300, bg='white', bd=10)
    keyboard_frame.place(relx=0.5, y=650, width=440, height=140, anchor='n')

    button1 = tk.Button(keyboard_frame, text=' Q ', fg='black', bg='gray', 
                     command=lambda: press('Q'), height=2, width=4)
    button1.grid(row=1, column=0) 

    button2 = tk.Button(keyboard_frame, text=' W ', fg='black', bg='gray', 
                     command=lambda: press('W'), height=2, width=4)
    button2.grid(row=1, column=1)

    button3 = tk.Button(keyboard_frame, text=' E ', fg='black', bg='gray', 
                     command=lambda: press('E'), height=2, width=4)
    button3.grid(row=1, column=2)

    button4 = tk.Button(keyboard_frame, text=' R ', fg='black', bg='gray', 
                     command=lambda: press('R'), height=2, width=4)
    button4.grid(row=1, column=3)

    button5 = tk.Button(keyboard_frame, text=' T ', fg='black', bg='gray', 
                     command=lambda: press('T'), height=2, width=4)
    button5.grid(row=1, column=4)

    button6 = tk.Button(keyboard_frame, text=' Y ', fg='black', bg='gray', 
                     command=lambda: press('Y'), height=2, width=4)
    button6.grid(row=1, column=5)

    button7 = tk.Button(keyboard_frame, text=' U ', fg='black', bg='gray', 
                     command=lambda: press('U'), height=2, width=4)
    button7.grid(row=1, column=6)

    button8 = tk.Button(keyboard_frame, text=' I ', fg='black', bg='gray', 
                     command=lambda: press('I'), height=2, width=4)
    button8.grid(row=1, column=7)

    button10 = tk.Button(keyboard_frame, text=' O ', fg='black', bg='gray', 
                     command=lambda: press('O'), height=2, width=4)
    button10.grid(row=1, column=8)

    button11 = tk.Button(keyboard_frame, text=' P ', fg='black', bg='gray', 
                     command=lambda: press('P'), height=2, width=4)
    button11.grid(row=1, column=9)

    button_hint = tk.Button(keyboard_frame, text='HINT', fg='black', bg='gray', 
                     command=lambda: hint(word), height=2, width=4)
    button_hint.grid(row=1, column=10)

    button12 = tk.Button(keyboard_frame, text=' A ', fg='black', bg='gray', 
                     command=lambda: press('A'), height=2, width=4)
    button12.grid(row=2, column=1)

    button13 = tk.Button(keyboard_frame, text=' S ', fg='black', bg='gray', 
                     command=lambda: press('S'), height=2, width=4)
    button13.grid(row=2, column=2)

    button14 = tk.Button(keyboard_frame, text=' D ', fg='black', bg='gray', 
                     command=lambda: press('D'), height=2, width=4)
    button14.grid(row=2, column=3)

    button15 = tk.Button(keyboard_frame, text=' D ', fg='black', bg='gray', 
                     command=lambda: press('F'), height=2, width=4)
    button15.grid(row=2, column=4)

    button15 = tk.Button(keyboard_frame, text=' G ', fg='black', bg='gray', 
                     command=lambda: press('G'), height=2, width=4)
    button15.grid(row=2, column=5)

    button16 = tk.Button(keyboard_frame, text=' H ', fg='black', bg='gray', 
                     command=lambda: press('H'), height=2, width=4)
    button16.grid(row=2, column=6)

    button17 = tk.Button(keyboard_frame, text=' J ', fg='black', bg='gray', 
                     command=lambda: press('J'), height=2, width=4)
    button17.grid(row=2, column=7)

    button18 = tk.Button(keyboard_frame, text=' K ', fg='black', bg='gray', 
                     command=lambda: press('K'), height=2, width=4)
    button18.grid(row=2, column=8)

    button19 = tk.Button(keyboard_frame, text=' L ', fg='black', bg='gray', 
                     command=lambda: press('L'), height=2, width=4)
    button19.grid(row=2, column=9)

    button20 = tk.Button(keyboard_frame, text=' Z ', fg='black', bg='gray', 
                     command=lambda: press('Z'), height=2, width=4)
    button20.grid(row=3, column=2)

    button21 = tk.Button(keyboard_frame, text=' X ', fg='black', bg='gray', 
                     command=lambda: press('X'), height=2, width=4)
    button21.grid(row=3, column=3)

    button22 = tk.Button(keyboard_frame, text=' C ', fg='black', bg='gray', 
                     command=lambda: press('C'), height=2, width=4)
    button22.grid(row=3, column=4)

    button23 = tk.Button(keyboard_frame, text=' V ', fg='black', bg='gray', 
                     command=lambda: press('V'), height=2, width=4)
    button23.grid(row=3, column=5)

    button24 = tk.Button(keyboard_frame, text=' B ', fg='black', bg='gray', 
                     command=lambda: press('B'), height=2, width=4)
    button24.grid(row=3, column=6)

    button25 = tk.Button(keyboard_frame, text=' N ', fg='black', bg='gray', 
                     command=lambda: press('M'), height=2, width=4)
    button25.grid(row=3, column=7)

    button26 = tk.Button(keyboard_frame, text=' M ', fg='black', bg='gray', 
                     command=lambda: press('M'), height=2, width=4)
    button26.grid(row=3, column=8)


# button_hint = tk.Button(keyboard_frame, text='HINT', fg='black', bg='gray', 
#                 command=lambda: hint(word), height=2, width=4)
# button_hint.grid(row=1, column=10)

# button12 = tk.Button(keyboard_frame, text=' A ', fg='black', bg='gray', 
#                 command=lambda: press('A'), height=2, width=4)
# button12.grid(row=2, column=1) 

def hint(word):
    msg = master_dict[word]
    popup = tk.Toplevel()
    popup.wm_title('Word Hint')
    label = tk.Text(popup, wrap='word')
    label.pack(pady=5, padx=5)
    label.insert(tk.END, msg)
    button_close = tk.Button(popup, text="Close", command=popup.destroy, bg='red', activebackground='orange red', width=50)
    button_close.pack()


def word_box(display):
    # only for outline now
    word_box = tk.Frame(root, height=150, width=700, bd=10)
    label = tk.Label(word_box, text=display)
    label.config(font=(None, 25))
    label.pack()
    word_box.place(relx=0.5, y=570, height=80, anchor='n')
    # Once word is guessed fully change word box to green
    if '_' not in display:
        label.configure(bg='green')
        word_box.configure(bg='green')

def hangman():
    # only for outline now
    word_box = tk.Frame(root, height=150, width=700, bd=10)
    word_box.place(relx=0.5, y=10, height=550, anchor='n')



def update_txt(l, t):
    global score
    global display
    # l is letter to find
    # t is original text to guess
    # i is index list
    # d is display word with hidden letters
    # s is score which starts at 7
    i = [i for i, ltr in enumerate(t) if ltr == l]
    if i == []:
        score -= 1
        # print turle sections here
        print('wrong guess')
        return score
    elif l in display:
        print('You\'ve guesed that already')
    else:
        for nums in i:
            display[nums] = l
            print(display)
    return display


def choices(choice):
    global word
    print(choice)
    if choice == 'easy':
        # root.mainloop()
        word = random.choice(list(easy_dict.items()))
        return word


def choose_difficulty():
    popup = tk.Toplevel()
    popup.geometry('150x150')
    popup.wm_title('Choose Level')
    popup.attributes('-topmost', 'true')

    button_easy = tk.Button(popup, text='Easy Word', command = choices('easy'))
    button_easy.pack()
    button_hard = tk.Button(popup, text='Hard Word')
    button_hard.pack()
 

    # random.choice(list(easy_dict.items()))

    choice = input('choose difficulty level: ')
    if choice == 'easy': 
        return random.choice(list(easy_dict))
    elif choice == 'hard':
        return random.choice(list(hard_dict))


score = 7


if __name__ == '__main__':

    root = tk.Tk()
    root.configure(background="white")
    root.title('Simple Hangman Game') 
    root.resizable(False, False)
    root.geometry("800x800") 
    
    
    hangman()
    
    score = 7
    keys()
    word = choose_difficulty()
    display = list(len(word) * '_')
    word_box(display)

    while score > 0:
        l = input('Guess a letter: ')
        print(f'here are the keys {keys()}')
        #print(f'this is printing letter from while loop {letter}')
        update_txt(l, word)
        word_box(display)
        print(display)
        print(score)
        print(word)


    root.mainloop() 
