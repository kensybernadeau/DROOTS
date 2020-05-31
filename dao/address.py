from config.dbconfig import pg_config
import psycopg2


class AddressDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self, user_country, user_city, user_street_address, user_zipcode, user_id):
        cursor = self.conn.cursor()
        query = "insert into address(user_country, user_city, user_street_address, user_zipcode, user_id) values (%s, %s, %s, %s, %s) returning address_id;"
        cursor.execute(query, (user_country, user_city, user_street_address, user_zipcode, user_id,))
        address_id = cursor.fetchone()[0]
        self.conn.commit()
        return address_id

