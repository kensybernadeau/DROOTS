from config.dbconfig import pg_config
import psycopg2

from dao.payment import paymentDAO


class cardDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCard(self):
        cursor = self.conn.cursor()
        query = "select payment_id, payment_date, payment_amount, customer_id, supplier_id, resource_id, resource_name, card_id, card_type, card_number, card_security_code  " \
                "from card natural inner join payment natural inner join supplies natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardById(self, card_id):
        cursor = self.conn.cursor()
        query = "select payment_id, payment_date, payment_amount, customer_id, supplier_id, resource_id, resource_name, card_id, card_type, card_number, card_security_code  " \
                "from card natural inner join payment natural inner join supplies natural inner join resources where payment_id = %s;"
        cursor.execute(query, (card_id,))
        result = cursor.fetchone()
        return result

    def insertCard(self, card_type, card_number, card_security_code, payment_date, payment_amount, resource_id,
                   supplier_id, customer_id):
        payment_id = paymentDAO().insertPayment(payment_date, payment_amount, resource_id, supplier_id, customer_id)
        cursor = self.conn.cursor()
        query = "insert into Card(card_type, card_number, card_security_code, payment_id) values (%s, %s, %s, %s) returning card_id;"
        cursor.execute(query, (card_type, card_number, card_security_code, payment_id,))
        card_id = cursor.fetchone()[0]
        self.conn.commit()
        return card_id, payment_id

