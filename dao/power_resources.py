from config.dbconfig import pg_config
import psycopg2


class PowerResourcesDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPowerResources(self):
        cursor = self.conn.cursor()
        query = "select power_id, resource_name, power_type, power_description " \
                "from power_resources natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerResourcesById(self, power_id):
        cursor = self.conn.cursor()
        query = "select power_id, resource_name, power_type, power_description " \
                "from power_resources natural inner join resources where power_id = %s;"
        cursor.execute(query, (power_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = "select power_id, resource_name, power_type, power_description " \
                "from power_resources natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
