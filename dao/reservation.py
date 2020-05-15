from config.dbconfig import pg_config
import psycopg2


class reservationDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReservation(self):
        cursor = self.conn.cursor()
        query = "select reservation_id, customer_id, supplier_id, resource_id, resource_name   " \
                "from  customer natural inner join reservation natural inner join supplies natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationById(self, reservation_id):
        cursor = self.conn.cursor()
        query = "select reservation_id, customer_id, resource_id, supplier_id  " \
                "from reservation natural inner join customer natural inner join supplies where reservation_id = %s;"
        cursor.execute(query, (reservation_id,))
        result = cursor.fetchone()
        return result

    def insertReservation(self, customer_id, resource_id, supplier_id):
        cursor = self.conn.cursor()
        query = "insert into reservation(customer_id, resource_id, supplier_id) " \
                "values (%s, %s, %s) returning reservation_id;"
        cursor.execute(query, (customer_id, resource_id, supplier_id,))
        reservation_id = cursor.fetchone()[0]
        self.conn.commit()
        return reservation_id



# CREATE TABLE child_table(
#   c1 INTEGER PRIMARY KEY,
#   c2 INTEGER,
#   c3 INTEGER,
#   FOREIGN KEY (c2, c3) REFERENCES parent_table (p1, p2)
# );