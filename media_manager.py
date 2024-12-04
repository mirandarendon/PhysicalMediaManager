import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# connect to SQLite
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# create table if it doesnt exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    if INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL
)
''')
conn.commit()

def openBookList():
    pass

def openAddBook(parentWin):
    pass

    def addBook():
        pass

def showTable():
    pass

root = tk.Tk()
root.title("Physical Media Manager")

welcomeLabel = tk.Label(root, text="Welcome to your Physical Media Manager!")
welcomeLabel.pack(pady=10)

root.mainloop()

# close database
conn.close()