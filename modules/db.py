import configparser

import psycopg2


class Database:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        self.__conn = psycopg2.connect(
            dbname='services',
            user='postgres',
            password='Programm',
        )
        self.__conn.autocommit = True
        self.__cur = self.__conn.cursor()

    def close(self):
        self.__conn.close()

    def execute(self, sql, params=None):
        self.__cur.execute(sql, params)
        self.__conn.commit()
        return self.__cur.rowcount

    def select(self, sql, params=None):
        self.__cur.execute(sql, params)
        return self.__cur.fetchall()
