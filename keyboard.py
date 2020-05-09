import tkinter as tk
from tkinter import ttk
from word_dicts import master_dict


class Keyboard(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.output_label = tk.Label(self)
        self.output_label.grid(row=0, columnspan=10)

        button1 = ttk.Button(self, text=' Q ', command=lambda: self.press('Q'))
        button1.grid(row=1, column=0)

        button2 = ttk.Button(self, text=' W ', command=lambda: self.press('W'))
        button2.grid(row=1, column=1)

        button3 = ttk.Button(self, text=' E ', command=lambda: self.press('E'))
        button3.grid(row=1, column=2)

        button4 = ttk.Button(self, text=' R ', command=lambda: self.press('R'))
        button4.grid(row=1, column=3)

        button5 = ttk.Button(self, text=' T ', command=lambda: self.press('T'))
        button5.grid(row=1, column=4)

        button6 = ttk.Button(self, text=' Y ', command=lambda: self.press('Y'))
        button6.grid(row=1, column=5)

        button7 = ttk.Button(self, text=' U ', command=lambda: self.press('U'))
        button7.grid(row=1, column=6)

        button8 = ttk.Button(self, text=' I ', command=lambda: self.press('I'))
        button8.grid(row=1, column=7)

        button10 = ttk.Button(self, text=' O ', command=lambda: self.press('O'))
        button10.grid(row=1, column=8)

        button11 = ttk.Button(self, text=' P ', command=lambda: self.press('P'))
        button11.grid(row=1, column=9)

        button_hint = ttk.Button(self, text='HINT', command=lambda: self.hint(master.word))
        button_hint.grid(row=1, column=10)

        button12 = ttk.Button(self, text=' A ', command=lambda: self.press('A'))
        button12.grid(row=2, column=1)

        button13 = ttk.Button(self, text=' S ', command=lambda: self.press('S'))
        button13.grid(row=2, column=2)

        button14 = ttk.Button(self, text=' D ', command=lambda: self.press('D'))
        button14.grid(row=2, column=3)

        button15 = ttk.Button(self, text=' F ', command=lambda: self.press('F'))
        button15.grid(row=2, column=4)

        button15 = ttk.Button(self, text=' G ', command=lambda: self.press('G'))
        button15.grid(row=2, column=5)

        button16 = ttk.Button(self, text=' H ', command=lambda: self.press('H'))
        button16.grid(row=2, column=6)

        button17 = ttk.Button(self, text=' J ', command=lambda: self.press('J'))
        button17.grid(row=2, column=7)

        button18 = ttk.Button(self, text=' K ', command=lambda: self.press('K'))
        button18.grid(row=2, column=8)

        button19 = ttk.Button(self, text=' L ', command=lambda: self.press('L'))
        button19.grid(row=2, column=9)

        button20 = ttk.Button(self, text=' Z ', command=lambda: self.press('Z'))
        button20.grid(row=3, column=2)

        button21 = ttk.Button(self, text=' X ', command=lambda: self.press('X'))
        button21.grid(row=3, column=3)

        button22 = ttk.Button(self, text=' C ', command=lambda: self.press('C'))
        button22.grid(row=3, column=4)

        button23 = ttk.Button(self, text=' V ', command=lambda: self.press('V'))
        button23.grid(row=3, column=5)

        button24 = ttk.Button(self, text=' B ', command=lambda: self.press('B'))
        button24.grid(row=3, column=6)

        button25 = ttk.Button(self, text=' N ', command=lambda: self.press('N'))
        button25.grid(row=3, column=7)

        button26 = ttk.Button(self, text=' M ', command=lambda: self.press('M'))
        button26.grid(row=3, column=8)

    def press(self, letter):
        #self.output_label.config(text="You pressed "+letter)
        self.master.method(letter) # send the data back to the master class


    def hint(self, word):
        # Hard code word in for testing
        msg = master_dict[word]
 
        popup = tk.Toplevel()
        popup.geometry("+%d+%d" % (500, 400))
        popup.geometry('400x300')
        #popup.resizable(False, False)
        popup.wm_title('Word Hint')
        label = tk.Text(popup, wrap='word')
        label.config(height=15, width=100)
        label.pack(pady=5, padx=5)
        label.insert(tk.END, msg)
        label.configure(state='disabled')
        button_close = ttk.Button(popup, text="Close",command=popup.destroy)
        # ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
        button_close.pack()

