import sqlite3
from lib.config import CONN, CURSOR

class Song:
    def __init__(self, name, album, id=None):
        self.id = id
        self.name = name
        self.album = album

    def save(self):
        with CONN:
            CURSOR.execute('INSERT INTO songs (name, album) VALUES (?, ?)', (self.name, self.album))
            # Update the 'id' attribute with the last inserted row's ID
            self.id = CURSOR.lastrowid

    @classmethod
    def create_table(cls):
        with CONN:
            CURSOR.execute('''
                CREATE TABLE IF NOT EXISTS songs (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    album TEXT NOT NULL
                )
            ''')

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
