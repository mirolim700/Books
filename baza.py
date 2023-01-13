import sqlite3 

class Database():
	def __init__(self):
		self.conn = sqlite3.connect("books.db")
		self.cur = self.conn.cursor()
	# Users
	def create_users(self):
		self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
			tel_id varchar(20),
			name varchar(50)
			)""")
	def select_users(self,id):
		self.cur.execute(f"SELECT * FROM users WHERE tel_id = '{id}'")
		data = self.cur.fetchone()
		if data is None:
			return False
		else:
			return True

	def insert_users(self,tel_id,name):
		self.cur.execute(f"INSERT into users values('{tel_id}',{name})")
		return self.cur.commit()

	# Books Category
	def create_category(self):
		self.cur.execute("""CREATE TABLE IF NOT EXISTS category(
			id integer PRIMARY KEY AUTOINCREMENT,
			name varchar(20)
			)""")
	def insert_category(self,name):
		self.cur.execute(f"INSERT into category(name) values('{name}')")
		return self.conn.commit()
	def select_category_id(self,id):
		self.cur.execute(f"SELECT * FROM category WHERE id = '{id}'")
		data = self.cur.fetchone()
		return data

	def select_category_all(self):
		self.cur.execute("SELECT * from category")
		data = self.cur.fetchall()
		return data 

	# Books Products
	def create_table_sub_products(self):
		self.cur.execute("""CREATE TABLE IF NOT EXISTS products(
			id integer PRIMARY KEY AUTOINCREMENT,
			category_id integer,
			file_text text NULL,
			file_name varchar(250),
			file_des text NULL,
			file_photo text NULL,
			file_price varchar(20),
			FOREIGN KEY(category_id) references category(id)
			)""")

	def select_products_for_category_id(self,id):
		self.cur.execute(f"""SELECT * FROM products WHERE category_id = '{id}'""")
		return self.cur.fetchall()

	def select_product_id(self,id):
		self.cur.execute(f"""SELECT * FROM products WHERE id = '{id}'""")
		return self.cur.fetchone()

	def insert_products(self,file_name,file_des,category_id,file_price):
		self.cur.execute(f"""INSERT into products(file_name,file_des,category_id,file_price) values("{file_name}","{file_des}","{category_id}","{file_price}")""" )
		return self.conn.commit()

	def search_product(self,suz):
		self.cur.execute(f"""SELECT * FROM products where file_name like "%(suz)%" """)
		return self.cur.fetchall()

