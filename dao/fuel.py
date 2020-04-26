from config.dbconfig import pg_config
import psycopg2


class FuelDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuels(self):
        cursor = self.conn.cursor()
        query = "select * from fuel;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelById(self, fuel_id):
        cursor = self.conn.cursor()
        query = "select * from fuel where fuel_id = %s;"
        cursor.execute(query, (fuel_id,))
        result = cursor.fetchone()
        return result


    def insert(self, fuel_type, fuel_liters):
        cursor = self.conn.cursor()
        query = "insert into fuel(fuel_type, fuel_liters) values (%s, %s) returning fuel_id;"
        cursor.execute(query, (fuel_type, fuel_liters,))
        fuel_id = cursor.fetchone()[0]
        self.conn.commit()
        return fuel_id

    def delete(self, fuel_id):
        cursor = self.conn.cursor()
        query = "delete from fuel where fuel_id = %s;"
        cursor.execute(query, (fuel_id,))
        self.conn.commit()
        return fuel_id

    def update(self, fuel_id, fuel_type, fuel_liters):
        cursor = self.conn.cursor()
        query = "update fuel set fuel_type = %s, fuel_liters = %s where fuel_id = %s;"
        cursor.execute(query, (fuel_type, fuel_liters, fuel_id,))
        self.conn.commit()
        return fuel_id

