from config.dbconfig import pg_config
import psycopg2


class PhoneDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def insert(self, phone_number, user_id):
        cursor = self.conn.cursor()
        query = "insert into phone(phone_number, user_id) values (%s, %s) returning phone_id;"
        cursor.execute(query, (phone_number, user_id))
        phone_id = cursor.fetchone()[0]
        self.conn.commit()
        return phone_id
