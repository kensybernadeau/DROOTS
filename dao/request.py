from config.dbconfig import pg_config
import psycopg2


class requestDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequest(self):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, resource_id, resource_name  " \
                "from  customer natural inner join request natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, request_id):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, resource_id, resource_name  " \
                "from request natural inner join customer natural inner join resources where request_id = %s;"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def get_request_by_resource_name(self, resource_name):
        cursor = self.conn.cursor()
        query =  "select request_id, customer_id, resource_id, resource_name   " \
                "from customer natural inner join request natural inner join resources where resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

# CREATE TABLE child_table(
#   c1 INTEGER PRIMARY KEY,
#   c2 INTEGER,
#   c3 INTEGER,
#   FOREIGN KEY (c2, c3) REFERENCES parent_table (p1, p2)
# );