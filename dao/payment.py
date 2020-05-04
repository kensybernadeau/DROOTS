from config.dbconfig import pg_config
import psycopg2


class paymentDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPayment(self):
        cursor = self.conn.cursor()
        query = "select payment_id, customer_id, payment_date, payment_amount, supplier_id, resource_id   " \
                "from  customer natural inner join payment natural inner join supplies;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPaymentById(self, payment_id):
        cursor = self.conn.cursor()
        query = "select payment_id, customer_id, payment_date, payment_amount, resource_id, supplier_id  " \
                "from payment inner join customer inner join supplies where payment_id = %s;"
        cursor.execute(query, (payment_id,))
        result = cursor.fetchone()
        return result