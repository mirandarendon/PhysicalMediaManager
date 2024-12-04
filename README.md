# Physical Media Manager

A desktop application built with Python and Tkinter for managing books and DVDs. Users can add, view, and organize their collections with ease. The app uses SQLite for data persistence.

## Features
- Manage separate collections for books and DVDs.
- Add new items to your collection (title, author/director, genre).
- Sort items by title, author/director, or genre.
- Data is saved persistently using SQLite.

## Prerequisites
- Python 3.6 or later

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/physical-media-manager.git
   cd physical-media-manager
   ```

2. Run the application:
   ```bash
   python media_manager.py
   ```

## How to Use
1. Run the application:
   ```bash
   python media_manager.py
   ```

2. From the main menu:
   - Click the **Book** button to manage your book collection.
   - Click the **DVD** button to manage your DVD collection.

3. In the collection window:
   - Click **Add** to add a new item.
   - Use the dropdown menu to sort by title, author/director, or genre.
   - Your data will be saved automatically in the `media.db` file.
