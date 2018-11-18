"""Database model"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class Datastore(object):
    def __init__(self):
        """constructor method for connecting to the database""" 
        if os.getenv("Testingenv") == "EnvTests":
            dbname = "testdb"
        else: 
            dbname = "storemanagerdb"
        self.conn = psycopg2.connect(dbname=dbname, user="postgres", host="localhost", password="alimanu", port="5432")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        self.create_user_table()
        self.create_products_table()
        self.create_sales_table()

        print (dbname)            

    def create_user_table(self):
        """method creates table in database for users"""
        user_table = "CREATE TABLE IF NOT EXISTS users(user_id serial PRIMARY KEY, \
        username varchar(50), password varchar(256), role varchar(15))"

        self.cur.execute(user_table)

    def create_products_table(self):
        """creates table to store products"""
        products_table = "CREATE TABLE IF NOT EXISTS products(product_id serial PRIMARY KEY, \
        product_name varchar(100), price integer, category varchar(80), quantity integer, \
        minimum_quantity integer)"

        self.cur.execute(products_table)

    def create_sales_table(self):
        """creates sales records tables"""
        sales_table = "CREATE TABLE IF NOT EXISTS sales(sale_id serial PRIMARY KEY, product_name varchar(100), \
        price integer, quantity integer)"
        
        self.cur.execute(sales_table)

    def drop_tables(self):
        """drops/ deletes tables"""
        drop_user_table = "DROP TABLE users cascade;"
        drop_products_table = "DROP TABLE products cascade;"
        drop_sales_table = "DROP TABLE sales order cascade;"
        self.cur.execute(drop_user_table)
        self.cur.execute(drop_products_table)
        self.cur.execute(drop_sales_table)
