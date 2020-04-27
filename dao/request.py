from config.dbconfig import pg_config
import psycopg2


class RequestDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequest(self):
        cursor = self.conn.cursor()
        query = "select * from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, request_id):
        cursor = self.conn.cursor()
        query = "select * from request where request_id = %s;"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def insert(self, customer_id, resource_id):
        cursor = self.conn.cursor()
        query = "insert into request(customer_id,resource_id) values(%s,%s) returning request_id;"
        cursor.execute(query, (customer_id,resource_id))
        request_id = cursor.fetchone()[0]
        self.conn.commit()
        return request_id

    def delete(self, request_id):
        cursor = self.conn.cursor()
        query = "delete from request where request_id = %s;"
        cursor.execute(query, (request_id,))
        self.conn.commit()
        return request_id

    # def update(self, user_id, user_first_name, user_last_name, user_location, user_name, user_password):
    # cursor = self.conn.cursor()
    # query = "update users set user_first_name = %s, user_last_name = %s, user_location = %s, user_name = %s, user_password = %s where user_id = %s;"
    # cursor.execute(query, (user_id, user_first_name, user_last_name, user_location, user_name, user_password,))
    # self.conn.commit()
    # return user_id
