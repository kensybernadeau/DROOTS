from config.dbconfig import pg_config
import psycopg2


class PowerResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPowerResources(self):
        cursor = self.conn.cursor()
        query = "select * from power_resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerResourceById(self, power_id):
        cursor = self.conn.cursor()
        query = "select * from power_resources where power_id = %s;"
        cursor.execute(query, (power_id,))
        result = cursor.fetchone()
        return result


    def insert(self, power_category, power_type, power_description):
        cursor = self.conn.cursor()
        query = "insert into power_resources(power_category, power_type, power_description) values (%s, %s, %s) returning power_id;"
        cursor.execute(query, (power_category, power_type, power_description,))
        power_id = cursor.fetchone()[0]
        self.conn.commit()
        return power_id

    def delete(self, power_id):
        cursor = self.conn.cursor()
        query = "delete from power_resources where power_id = %s;"
        cursor.execute(query, (power_id,))
        self.conn.commit()
        return power_id

    def update(self, power_id, power_category, power_type, power_description):
        cursor = self.conn.cursor()
        query = "update power_resources set power_category = %s, power_type = %s, power_description = %s where power_id = %s;"
        cursor.execute(query, (power_category, power_type, power_description, power_id,))
        self.conn.commit()
        return power_id

