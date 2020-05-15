from config.dbconfig import pg_config
import psycopg2

from dao.resources import ResourcesDAO


class FoodDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)
        self.select_statement = "select food_id, resource_name, food_exp_date, food_type, food_description, resource_id "

    def getAllFood(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from food natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodById(self, food_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from food natural inner join resources where food_id = %s;"
        cursor.execute(query, (food_id,))
        result = cursor.fetchone()
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from food natural inner join resources where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from food natural inner join resources;"

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_supplied(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from suppliers natural inner join supplies natural inner join resources natural inner join food;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_by_name(self, resource_name):
        cursor = self.conn.cursor()
        query = self.select_statement + "from food natural inner join resources where resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_food_by_type(self, food_type):
        cursor = self.conn.cursor()
        query = self.select_statement + "from food natural inner join resources where food_type = %s;"
        cursor.execute(query, (food_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result


# ----------------------------------Inserts------------------------------------------------------------------------------

    def insert_food(self, resource_name, food_exp_date, food_type, food_description, resource_date):
        resource_id = ResourcesDAO().insert_resource(resource_name, 'food', resource_date)
        cursor = self.conn.cursor()
        query = "insert into food(food_exp_date, food_type, food_description, resource_id) values (%s, %s, %s, %s) returning food_id;"
        cursor.execute(query, (food_exp_date, food_type, food_description, resource_id))
        food_id = cursor.fetchone()[0]
        self.conn.commit()
        return food_id, resource_id


