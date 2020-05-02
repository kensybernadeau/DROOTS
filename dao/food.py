from config.dbconfig import pg_config
import psycopg2


class FoodDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFood(self):
        cursor = self.conn.cursor()
        query = "select food_id, resource_name, food_exp_date, food_type, food_description " \
                "from food natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodById(self, food_id):
        cursor = self.conn.cursor()
        query = "select food_id, resource_name, food_exp_date, food_type, food_description " \
                "from food natural inner join resources where food_id = %s;"
        cursor.execute(query, (food_id,))
        result = cursor.fetchone()
        return result


#----------------------------------Inserts------------------------------------------------------------------------------
    def insert_resource(self, resource_name, resource_category, resource_availability):
        cursor = self.conn.cursor()
        query = "insert into resources(resource_name, resource_category) values (%s, %s) returning resource_id;"
        cursor.execute(query, (resource_category, resource_availability,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def insert_food(self, food_exp_date, food_type, food_description, resource_availability):
        resource_id = self.insert_resource("food", resource_availability)
        cursor = self.conn.cursor()
        query = "insert into food(food_exp_date, food_type, food_description, resource_id) values (%s, %s, %s, %s) returning food_id;"
        cursor.execute(query, (food_exp_date, food_type, food_description, resource_id))
        food_id = cursor.fetchone()[0]
        self.conn.commit()
        return food_id

    # def get_available_resources(self):
    #     cursor = self.conn.cursor()
    #     query = "select food_id, food_exp_date, food_type, food_description, resource_availability " \
    #             "from food natural inner join resources " \
    #             "where resource_availability > 0;"
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

