from config.dbconfig import pg_config
import psycopg2


class ToolsDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllTools(self):
        cursor = self.conn.cursor()
        query = "select tool_id, resource_name, tool_description " \
                "from tools natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolsById(self, tool_id):
        cursor = self.conn.cursor()
        query = "select tool_id, resource_name, tool_description " \
                "from tools natural inner join resources where tool_id = %s;"
        cursor.execute(query, (tool_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = "select tool_id, resource_name, tool_description " \
                "from tools natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
