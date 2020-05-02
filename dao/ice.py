from config.dbconfig import pg_config
import psycopg2


class IceDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllIce(self):
        cursor = self.conn.cursor()
        query = "select ice_id, resource_name, ice_description " \
                "from ice natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceById(self, ice_id):
        cursor = self.conn.cursor()
        query = "select ice_id, resource_name, ice_description " \
                "from ice natural inner join resources where ice_id = %s;"
        cursor.execute(query, (ice_id,))
        result = cursor.fetchone()
        return result
