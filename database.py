import random

import pymysql
from faker import Faker

from loadconfig import Config

# load configuration
config = Config()

# Quanti impiegati metto nel db?
HOW_MANY_EMPLOYEES = config.how_many_employees


class Database:
    def __init__(self):
        db = config.get_db_config()
        self.con = pymysql.connect(
            host=db["host"],
            port=db["port"],
            user=db["user"],
            password=db["password"],
            db=None,
            # db=db["db"],
            cursorclass=pymysql.cursors.DictCursor,
        )

        self.cur = self.con.cursor()

        # Crea il db e inserisce dei dati se necessario
        self.cur.execute(f"CREATE DATABASE IF NOT EXISTS {db['db']}")
        self.cur.execute(f"USE {db['db']}")
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS employees (
                id integer NOT NULL PRIMARY KEY,
                firstname VARCHAR(64) NOT NULL,
                lastname VARCHAR(64) NOT NULL,
                gender integer NOT NULL)"""
        )

        self.cur.execute("SELECT COUNT(1) FROM employees")
        result = self.cur.fetchone()
        how_many = result["COUNT(1)"]

        if how_many == HOW_MANY_EMPLOYEES:
            self.con.commit()
            return

        fake = Faker()
        for i in range(HOW_MANY_EMPLOYEES):
            is_male = random.randint(0, 1) == 0
            if is_male:
                fakename = fake.first_name_male()
                fakesurname = fake.last_name_male()
            else:
                fakename = fake.first_name_female()
                fakesurname = fake.last_name_female()
            self.cur.execute(
                f"""INSERT INTO employees VALUES
                    ({i}, '{fakename}', '{fakesurname}', {int(is_male)})"""
            )

        self.con.commit()

    def list_employees(self):
        self.cur.execute("SELECT firstname, lastname, gender FROM employees")
        result = self.cur.fetchall()

        return result
