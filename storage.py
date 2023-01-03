import sqlite3
import pandas as pd


class DBStorage():
    def __init__(self):
        self.con = sqlite3.connect("recommendations.db")
        self.setup_tables()

    def Setup_tables(self):
        cur = self.con.cursor()
        trainingData_table = r"""
            CREATE TABLE IF NOT EXISTS recommendations (
                #id INTEGER PRIMARY KEY,
                userid INTEGER,
                movieId INTEGER,
                timestamp LONG INTEGER,
                rating REAL,
            );
            """

        cur.execute(trainingData_table)
        self.con.commit()
        cur.close()

    def GetTrainingData(self):
        # get training data from database
        df = pd.read_sql(f"select * from trainingData_table", self.con)
        return df

    def ClearTrainingData(self):
        # clear training data
        c = self.con.cursor()
        c.execute("DELETE FROM trainingData_table")

    def insert_row(self, values):
        cur = self.con.cursor()
        try:
            cur.execute(
                'INSERT INTO trainingData_table (userid, movieId, timestamp, rating,) VALUES(?, ?, ?, ?,)', values)
            self.con.commit()
        except sqlite3.IntegrityError:
            pass
        cur.close()
