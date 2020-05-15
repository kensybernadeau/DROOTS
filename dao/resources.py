import psycopg2
from config.dbconfig import pg_config


class ResourcesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def insert_resource(self, resource_name, resource_category, resource_date):
        cursor = self.conn.cursor()
        query = "insert into resources(resource_name, resource_category, resource_date) values (%s, %s, %s) returning resource_id;"
        cursor.execute(query, (resource_name, resource_category, resource_date))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def get_resource_daily_statistics(self, resource_date):
        cursor = self.conn.cursor()
        query = "select count(*) " \
                "from resources where resource_date = %s;"
        cursor.execute(query, (resource_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resource_weekly_statistics(self, resource_date):
        cursor = self.conn.cursor()
        query = "select count(*) " \
                "from resources " \
                "where resource_date >= %s and resource_date <= %s::date + interval '6 days';"
        cursor.execute(query, (resource_date, resource_date))
        result = []
        for row in cursor:
            result.append(row)
        return result

