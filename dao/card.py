from config.dbconfig import pg_config
import psycopg2


class cardDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCard(self):
        cursor = self.conn.cursor()
        query = "select card_id, card_type, card_number, card_security_code, payment_id " \
                "from card natural inner join payment;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardById(self, card_id):
        cursor = self.conn.cursor()
        query = "select card_id, card_type, card_number, card_security_code, payment_id " \
                "from card natural inner join payment where card_id = %s;"
        cursor.execute(query, (card_id,))
        result = cursor.fetchone()
        return result

