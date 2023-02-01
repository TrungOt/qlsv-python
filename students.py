#define PY_SSIZE_T_CLEAN
#include <Python.h>
import mysql.connector 
from mysql.connector import MySQLConnection, Error

# mydb = mysql.connector.connect(host='localhost',
# 							   	database='qlsv',
# 							   		user='test',
# 							password='123@123aA')

# def connect():
# 		mydb = {'host':'localhost',
# 				'database':'qlsv',
# 				'user':'root',
# 				'password':'123@123aA'}

# 		conn = None
		
# 		try:
# 			conn = MySQLConnection(**mydb)
# 			if conn.is_connected():
# 				return conn

# 		except Exception as err:
# 			print(err)
			
# 		return conn

# conn=connect()
# print(conn)

class Student:
	
	conn = None

	#Hàm khởi tạo 
	def __init__(self):
		self.connect()

	def __del__(self):
		if self.conn != None:
			self.conn.close()
	
	""" Kết nối MySQL """
	def connect(self):
		mydb = {'host':'localhost',
				'database':'qlsv',
				'user':'root',
				'password':'123@123aA'}

		conn = None
		
		try:
			conn = MySQLConnection(**mydb)
			if conn.is_connected() == False:
				raise Error
		except Error as error:
			print(error)
			
		self.conn = conn
		return self.conn

	""" Hàm hiển thị danh sách sinh viên """
	def show(self):
		cursor = self.conn.cursor()
		try:
			cursor = self.conn.cursor()
			cursor.execute("SELECT * FROM students")
			row = cursor.fetchone()

			while row is not None:
				print(row)
				row = cursor.fetchone()

		except Exception as err:
			print (err)
		finally:
			cursor.close()

	""" Hàm thêm sinh viên """
	def insert(self, fullname):
		cursor = self.conn.cursor()
		query = "INSERT INTO students(fullname) VALUES(%s)"
		args = (fullname,)
		try:
			cursor = self.conn.cursor()
			cursor.execute(query, args)
			if cursor.lastrowid:
				print("Success")
			else:
				print("False")

			self.conn.commit()
			self.show()

		except Exception as err:
			print(err)
		finally:
			cursor.close()
	
	""" Hàm update sinh viên """
	def update(self, id, name):
		cursor = self.conn.cursor()
		query = "UPDATE students SET fullname = %s WHERE id = %s"
		data = (name, id)
		try:
			cursor = self.conn.cursor()
			cursor.execute(query, data)
			
			self.conn.commit()
			self.show()

		except Exception as err:
			print(err)
		finally:
			cursor.close()
	
	""" Hàm xóa sinh viên """
	def delete(self, id):
		cursor = self.conn.cursor()
		query = "DELETE FROM students WHERE id = %s"
		data = (id,) #tuple 1 giá trị thì có dấu phẩy ở cuối 
		try:
			curson = self.conn.cursor()
			# curson.execute(query, (id,))
			curson.execute(query, data)
			print(curson)

			self.conn.commit()
			self.show()
			print(cursor.rowcount, "record(s) deleted")
		except Exception as err:
			print(err)
		finally:
			cursor.close()