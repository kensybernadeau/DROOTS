from config.dbconfig import pg_config
import psycopg2


class FuelDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select fuel_id, resource_name, fuel_type, fuel_liters " \
                "from fuel natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelById(self, fuel_id):
        cursor = self.conn.cursor()
        query = "select fuel_id, resource_name, fuel_type, fuel_liters " \
                "from fuel natural inner join resources where fuel_id = %s;"
        cursor.execute(query, (fuel_id,))
        result = cursor.fetchone()
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = "select fuel_id, resource_name, fuel_type, fuel_liters " \
                "from fuel natural inner join resources where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = "select fuel_id, resource_name, fuel_type, fuel_liters " \
                "from fuel natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_supplied(self):
        cursor = self.conn.cursor()
        query = "select fuel_id, resource_name, fuel_type, fuel_liters " \
                "from suppliers natural inner join supplies natural inner join resources natural inner join fuel;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_by_name(self, resource_name):
        cursor = self.conn.cursor()
        query = "select fuel_id, resource_name, fuel_type, fuel_liters " \
                "from fuel natural inner join resources where resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result
