from config.dbconfig import pg_config
import psycopg2


class SuppliesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2.connect(connection_url)

    def insert_supplies(self, resource_id, supplier_id, supplies_price, supplies_stock):
        cursor = self.conn.cursor()
        query = "insert into supplies(resource_id, supplier_id, supplies_price, supplies_stock) values (%s, %s, %s, %s);"
        cursor.execute(query, (resource_id, supplier_id, supplies_price, supplies_stock))
        self.conn.commit()
