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
    bookWindow = tk.Toplevel(root)
    bookWindow.title("Books")

    # header bar
    header = tk.Frame(bookWindow)
    header.pack(fill=tk.X, padx=10, pady=5)

    tk.Label(header, text="Books", font=("Arial", 16)).pack(side=tk.LEFT)
    
    addButton = tk.Button(header, text="Add", command=lambda: openBookList(bookWindow))
    addButton.pack(side=tk.RIGHT, padx=5)

    sortVar = tk.StringVar(value="Sort")
    sortMenu = ttk.OptionMenu(header, sortVar, "Sort", "Title", "Author", "Genre", command=lambda x: showTable(tree, x))
    sortMenu.pack(side=tk.RIGHT)

    # table of books
    columns = ("Title", "Author", "Genre")
    global tree
    tree = ttk.Treeview(bookWindow, columns=columns, show="heading")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Genre", text="Genre")
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # displays window when opened
    showTable(tree)

def openAddBook(parentWindow):
    pass

    def addBook():
        pass

def showTable(tree, sort_by=None):
    # clear existing table
    for row in tree.get_children():
        tree.delete(row)
    
    # get sorted data from DB
    if sort_by:
        query = f'SELECT title, author, genre FROM books ORDER BY {sort_by.lower()}'
    else:
        query = 'SELECT title, author, genre FROM books'
    cursor.execute(query)
    rows = cursor.fetchall()
    
    for row in rows:
        tree.insert("", tk.END, values=row)

root = tk.Tk()
root.title("Physical Media Manager")

welcomeLabel = tk.Label(root, text="Welcome to your Physical Media Manager!")
welcomeLabel.pack(pady=10)

root.mainloop()

# close database
conn.close()