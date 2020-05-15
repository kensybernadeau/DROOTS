from config.dbconfig import pg_config
import psycopg2


class EmailDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def insert(self, email_address, user_id):
        cursor = self.conn.cursor()
        query = "insert into email(email_address, user_id) values (%s, %s) returning email_id;"
        cursor.execute(query, (email_address, user_id))
        email_id = cursor.fetchone()[0]
        self.conn.commit()
        return email_id
