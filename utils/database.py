import sqlite3 as sql


class Database():
    def __init__(self, database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_users_id(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS users_id ('
                         'id INTEGER PRIMARY KEY,'
                         'id_user TEXT UNIQUE,'
                         'datetime TEXT)')

    def insert_user_id(self, user_id, datetime):
        self.cur.execute('INSERT OR IGNORE INTO users_id (id_user, datetime) VALUES (?, ?)',
                         (user_id, datetime)),
        self.con.commit()

    def select_user_id(self):
        self.cur.execute('SELECT id_user FROM users_id')
        return self.cur.fetchall()

    def close(self):
        self.con.close()


db1 = Database('users_id.db')
