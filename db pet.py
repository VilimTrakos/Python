from sqlite3 import *


class DB:
    def __init__(self):
        self.connection = connect('todo.db')
        self.cursor = self.connection.cursor()

        self.createTable()

    # https://pastebin.com/i7uLp7dB

    def createTable(self):
        try:
            self.update('''
                CREATE TABLE Tasks (
                    id INTEGER UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    desc TEXT NOT NULL,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            ''')
        except OperationalError:
            print('Database exists')

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.fetchall()


class Task:
    def __init__(self, name, desc, id=None):
        self.name = name
        self.desc = desc
        self.id = id

    def __str__(self):
        if not (self.desc is None) and len(self.desc) > 0:
            return '{} ({})'.format(self.name, self.desc)
        else:
            return self.name

    def __repr__(self):
        return self.__str__()

    def save(self):
        db.update('''
            INSERT INTO Tasks
            ("task", "desc")
            VALUES("{}", "{}")'''.format(self.name, self.desc)
                  )
        return self

    def delete(self):
        db.update('DELETE FROM Tasks Where id = {}'.format(self.id))

    @staticmethod
    def all():
        tasks = db.query('SELECT * FROM Tasks')
        output = []
        for task in tasks:
            output.append(Task(task[1], task[2], task[0]))
        return output


db = DB()