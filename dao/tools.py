from config.dbconfig import pg_config
import psycopg2

from dao.resources import ResourcesDAO


class ToolsDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
        self.select_statement = "select tool_id, resource_name, tool_description, resource_id " \

    def getAllTools(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from tools natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolsById(self, tool_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from tools natural inner join resources where tool_id = %s;"
        cursor.execute(query, (tool_id,))
        result = cursor.fetchone()
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from tools natural inner join resources where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from tools natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_supplied(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from suppliers natural inner join supplies natural inner join resources natural inner join tools;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_by_name(self, resource_name):
        cursor = self.conn.cursor()
        query = self.select_statement + "from tools natural inner join resources where resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert_tools(self, resource_name, tool_description, resource_date):
        resource_id = ResourcesDAO().insert_resource(resource_name, 'tools', resource_date)
        cursor = self.conn.cursor()
        query = "insert into tools(tool_description, resource_id) values (%s, %s) returning tool_id;"
        cursor.execute(query, (tool_description, resource_id))
        tool_id = cursor.fetchone()[0]
        self.conn.commit()
        return tool_id, resource_id
