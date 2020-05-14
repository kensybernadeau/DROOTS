from config.dbconfig import pg_config
import psycopg2

from dao.resources import ResourcesDAO


class ClothingDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
        self.select_statement = "select clothe_id, resource_name, clothe_size, clothe_type, clothe_description, resource_id "

    def getAllClothing(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from clothing natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingById(self, clothe_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from clothing natural inner join resources where clothe_id = %s;"
        cursor.execute(query, (clothe_id,))
        result = cursor.fetchone()
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from clothing natural inner join resources where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from clothing natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_supplied(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from suppliers natural inner join supplies natural inner join resources natural inner join clothing;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_by_name(self, resource_name):
        cursor = self.conn.cursor()
        query = self.select_statement + "from clothing natural inner join resources where resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert_clothing(self, resource_name, clothe_type, clothe_size, clothe_description, resource_date):
        resource_id = ResourcesDAO().insert_resource(resource_name, 'clothing', resource_date)
        cursor = self.conn.cursor()
        query = "insert into clothing(clothe_type, clothe_size, clothe_description, resource_id) " \
                "values (%s, %s, %s, %s) returning clothe_id;"
        cursor.execute(query, (clothe_type, clothe_size, clothe_description, resource_id))
        clothe_id = cursor.fetchone()[0]
        self.conn.commit()
        return clothe_id, resource_id
