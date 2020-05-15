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
        query = "select request_id, customer_id, resource_id, resource_name, request_date  " \
                "from  customer natural inner join request natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, request_id):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, resource_id, resource_name, request_date  " \
                "from request natural inner join customer natural inner join resources where request_id = %s;"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def get_request_by_resource_name(self, resource_name):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, resource_id, resource_name, request_date " \
                "from customer natural inner join request natural inner join resources where resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_request_daily_statistics(self, request_date):
        cursor = self.conn.cursor()
        query = "select count(*) " \
                "from customer natural inner join request natural inner join resources where request_date = %s;"
        cursor.execute(query, (request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_request_weekly_statistics(self, request_date):
        cursor = self.conn.cursor()
        query = "select count(*) " \
                "from customer natural inner join request natural inner join resources " \
                "where request_date >= %s and request_date <= %s::date + interval '6 days';"
        cursor.execute(query, (request_date, request_date))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert_request(self, customer_id, resource_id, request_date):
        cursor = self.conn.cursor()
        query = "insert into request(customer_id, resource_id, request_date) values (%s, %s, %s) returning request_id;"
        cursor.execute(query, (customer_id, resource_id, request_date))
        request_id = cursor.fetchone()[0]
        self.conn.commit()
        return request_id

# CREATE TABLE child_table(
#   c1 INTEGER PRIMARY KEY,
#   c2 INTEGER,
#   c3 INTEGER,
#   FOREIGN KEY (c2, c3) REFERENCES parent_table (p1, p2)
# );