from config.dbconfig import pg_config
import psycopg2


class WaterDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllWater(self):
        cursor = self.conn.cursor()
        query = "select water_id, resource_name, water_oz, water_type " \
                "from water natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterById(self, water_id):
        cursor = self.conn.cursor()
        query = "select water_id, resource_name, water_oz, water_type " \
                "from water natural inner join resources where water_id = %s;"
        cursor.execute(query, (water_id,))
        result = cursor.fetchone()
        return result