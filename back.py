import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self) -> None:
        self.connect()

    def connect(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'Apteka'
        )

    def get_role(self, user: dict):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT role FROM Users
                    WHERE login LIKE %s AND password LIKE %s
                """
                cursor.execute(query,(user['login'],user['password']))
                role = cursor.fetchone()
                cursor.close()
                if role:
                    return role[0]
                return ''
        except Error as err:
            return err

    def insert_user(self, user: dict):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    INSERT INTO Users (login, password) VALUES (%s, %s)
                """
                cursor.execute(query,(user['login'],user['password']))
                self.connection.commit()
                cursor.close()
                return ''
        except Error as err:
            return err
        
    def get_all_info(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT login, id, phone_number FROM users
                    WHERE role like 'user'
                """
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                if data:
                    return data
        except Error as err:
            return Error

    def delete_employee(self, _id: str):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    DELETE FROM users
                    WHERE id like %s
                """
                cursor.execute(query,(_id,))
                self.connection.commit()
                cursor.close()
                return True
        except Error as err:
            return False
        
    def suppliers_info(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT name, phone_number FROM suppliers
                """
                cursor.execute(query)
                supp_data = cursor.fetchall()
                cursor.close()
                if supp_data:
                    return supp_data
                return 'empty'
        except Error as err:
            return ''
        
    def customers_info(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT name, date, amount FROM customer
                """
                cursor.execute(query)
                supp_data = cursor.fetchall()
                cursor.close()
                if supp_data:
                    return supp_data
                return 'empty'
        except Error as err:
            return ''
        
    def admins_info(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT login, level, phone_number FROM users
                    WHERE role like 'admin'
                """
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                if data:
                    return data
                return 'empty'
        except Error as err:
            return ''
        
    def get_midicine_category(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT category, image FROM medics
                """
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                if data:
                    return data
                return 'empty'
        except Error as err:
            return ''

    def get_all_medics_info(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT name, category, amount, output_price, image FROM medics
                """
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                if data:
                    return data
                return 'empty'
        except Error as err:
            return ''

    def medicine_info(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT name, amount, output_price FROM medics
                """
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                if data:
                    return data
                return 'empty'
        except Error as err:
            return ''

    def add_up_medics(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT COUNT(name) FROM medics
                """
                cursor.execute(query)
                data = cursor.fetchone()
                cursor.close()
                if data:
                    return data[0]
                return 'empty'
        except Error as err:
            return ''

    def remove_medics(self, request: list):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = """
                    SELECT name, amount FROM medics
                """
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()

            for values in request:
                for i in data:
                    if i[0] == values[1]:
                        if i[1] >= values[0]:
                            with self.connection.cursor() as cursor:
                                query = """
                                    UPDATE medics
                                    SET amount = amount - %s
                                    WHERE name = %s
                                """
                                cursor.execute(query,values)
                                self.connection.commit()
                                cursor.close()
                            with self.connection.cursor() as cursor:
                                query = """
                                    DELETE FROM medics
                                    WHERE amount < 1
                                """
                                cursor.execute(query)
                                self.connection.commit()
                                cursor.close()
                        else:
                            return f'{values[1]} dorisidan bu miqdorda mavjud emas\n{values[1]} - {i[1]} dona'
            return ''
        except Error as err:
            return str(err)