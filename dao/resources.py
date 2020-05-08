import psycopg2
from config.dbconfig import pg_config


class ResourcesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def insert_resource(self, resource_name, resource_category):
        cursor = self.conn.cursor()
        query = "insert into resources(resource_name, resource_category) values (%s, %s) returning resource_id;"
        cursor.execute(query, (resource_name, resource_category,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

