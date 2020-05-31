from config.dbconfig import pg_config
import psycopg2


class CustomerDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllCustomers(self):
        cursor = self.conn.cursor()
        query = "select customer_id, user_id, user_first_name, user_last_name, user_uname, user_password, " \
                "user_country, user_city, user_street_address, user_zipcode, phone_number, email_address " \
                "from customer natural inner join users natural inner join address natural inner join " \
                "phone natural inner join email;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCustomerById(self, customer_id):
        cursor = self.conn.cursor()
        query = "select customer_id, user_id, user_first_name, user_last_name, user_uname, user_password, " \
                "user_country, user_city, user_street_address, user_zipcode, phone_number, email_address " \
                "from customer natural inner join users natural inner join address natural inner join " \
                "phone natural inner join email " \
                "where customer_id = %s;"
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()
        return result

    def insert(self, user_id):
        cursor = self.conn.cursor()
        query = "insert into customer(user_id) values (%s) returning customer_id;"
        cursor.execute(query, (user_id,))
        customer_id = cursor.fetchone()[0]
        self.conn.commit()
        return customer_id
