from config.dbconfig import pg_config
import psycopg2


class UsersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result


    def insert(self, user_first_name, user_last_name, user_location, user_name, user_password):
        cursor = self.conn.cursor()
        query = "insert into users(user_first_name, user_last_name, user_location, user_name, user_password) values (%s, %s, %s, %s, %s) returning user_id;"
        cursor.execute(query, (user_first_name, user_last_name, user_location, user_name, user_password,))
        user_id = cursor.fetchone()[0]
        self.conn.commit()
        return user_id

    def delete(self, user_id):
        cursor = self.conn.cursor()
        query = "delete from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        self.conn.commit()
        return user_id

    def update(self, user_id, user_first_name, user_last_name, user_location, user_name, user_password):
        cursor = self.conn.cursor()
        query = "update users set user_first_name = %s, user_last_name = %s, user_location = %s, user_name = %s, user_password = %s where user_id = %s;"
        cursor.execute(query, (user_first_name, user_last_name, user_location, user_name, user_password, user_id,))
        self.conn.commit()
        return user_id

