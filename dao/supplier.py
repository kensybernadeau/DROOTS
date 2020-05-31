from config.dbconfig import pg_config
import psycopg2


class SupplierDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select supplier_id, user_id, user_first_name, user_last_name, user_uname, user_password, " \
                "user_country, user_city, user_street_address, user_zipcode, phone_number, email_address " \
                "from suppliers natural inner join users natural inner join address natural inner join " \
                "phone natural inner join email;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select supplier_id, user_id, user_first_name, user_last_name, user_uname, user_password, " \
                "user_country, user_city, user_street_address, user_zipcode, phone_number, email_address " \
                "from suppliers natural inner join users natural inner join address natural inner join phone " \
                "natural inner join email where supplier_id = %s;"
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

