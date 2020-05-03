from config.dbconfig import pg_config
import psycopg2


class SupplierDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select supplier_id, user_id, user_first_name, user_last_name, user_uname, user_password, address_id, " \
                "user_country, user_city, user_street_address, user_zipcode " \
                "from suppliers natural inner join users natural inner join address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select supplier_id, user_id, user_first_name, user_last_name, user_uname, user_password, address_id, " \
                "user_country, user_city, user_street_address, user_zipcode " \
                "from suppliers natural inner join users natural inner join address where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self, user_id):
        cursor = self.conn.cursor()
        query = "insert into suppliers(user_id) values (%s) returning supplier_id;"
        cursor.execute(query, (user_id,))
        supplier_id = cursor.fetchone()[0]
        self.conn.commit()
        return supplier_id

    def delete(self, supplier_id):
        cursor = self.conn.cursor()
        query = "delete from suppliers where customer_id = %s returning user_id;"
        cursor.execute(query, (supplier_id,))
        user_id = cursor.fetchone()[0]
        self.conn.commit()
        return user_id

    # def update(self, user_id, user_first_name, user_last_name, user_location, user_name, user_password):
    # cursor = self.conn.cursor()
    # query = "update users set user_first_name = %s, user_last_name = %s, user_location = %s, user_name = %s, user_password = %s where user_id = %s;"
    # cursor.execute(query, (user_id, user_first_name, user_last_name, user_location, user_name, user_password,))
    # self.conn.commit()
    # return user_id
