from tkinter import *
from Data import Record
import tkinter as tk


def main():
    m = tk.Tk()
    m.title = 'FRC Scouting Data'

    Label(m, text='Raw data CSV').grid(row=0, column=0)
    e1 = Entry(m).grid(row=0, column=1)
    get_data_button = tk.Button(m, text='Import raw data', command=Record.import_raw_data(e1))
    get_data_button.pack()
    Teamlistbox = Listbox(m)

    m.mainloop()
