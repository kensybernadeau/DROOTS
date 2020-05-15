from config.dbconfig import pg_config
import psycopg2

from dao.payment import paymentDAO


class athmovilDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAthmovil(self):
        cursor = self.conn.cursor()
        query = "select payment_id, payment_date, payment_amount, customer_id, supplier_id, resource_id, resource_name, athmovil_id, athmovil_transaction_num, athmovil_phone_number     " \
                "from athmovil natural inner join payment natural inner join supplies natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAthmovilById(self, athmovil_id):
        cursor = self.conn.cursor()
        query = "select payment_id, payment_date, payment_amount, customer_id, supplier_id, resource_id, resource_name, athmovil_id, athmovil_transaction_num, athmovil_phone_number   " \
                "from athmovil natural inner join payment natural inner join supplies natural inner join resources where payment_id = %s;"
        cursor.execute(query, (athmovil_id,))
        result = cursor.fetchone()
        return result

    def insertAthmovil(self, athmovil_transaction_num, athmovil_phone_number, payment_date, payment_amount, customer_id, resource_id,
                   supplier_id):
        payment_id = paymentDAO().insertPayment(payment_date, payment_amount, resource_id, supplier_id, customer_id)
        cursor = self.conn.cursor()
        query = "insert into athmovil(athmovil_transaction_num, athmovil_phone_number, payment_id) values (%s, %s, %s) returning athmovil_id;"
        cursor.execute(query, ( athmovil_transaction_num, athmovil_phone_number, payment_id,))
        athmovil_id = cursor.fetchone()[0]
        self.conn.commit()
        return athmovil_id, payment_id


