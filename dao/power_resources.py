from config.dbconfig import pg_config
import psycopg2

from dao.resources import ResourcesDAO


class PowerResourcesDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
        self.select_statement = "select power_id, resource_name, power_type, power_description, resource_id " \

    def getAllPowerResources(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from power_resources natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerResourcesById(self, power_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from power_resources natural inner join resources where power_id = %s;"
        cursor.execute(query, (power_id,))
        result = cursor.fetchone()
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from power_resources natural inner join resources where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from power_resources natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_supplied(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from suppliers natural inner join supplies natural inner join resources natural inner join power_resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_by_name(self, resource_name):
        cursor = self.conn.cursor()
        query = self.select_statement + "from power_resources natural inner join resources where resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert_power_resource(self, resource_name, power_type, power_description):
        resource_id = ResourcesDAO().insert_resource(resource_name, 'powerres')
        cursor = self.conn.cursor()
        query = "insert into power_resources(power_type, power_description, resource_id) values (%s, %s, %s) returning power_id;"
        cursor.execute(query, (power_type, power_description, resource_id))
        power_id = cursor.fetchone()[0]
        self.conn.commit()
        return power_id, resource_id
