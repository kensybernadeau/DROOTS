from flask import jsonify

from dao.tools import ToolsDAO


class ToolsHandler:

    def build_tool_dict(self, row):
        result = {}
        result['tool_id'] = row[0]
        result['tool_name'] = row[1]
        result['tool_description'] = row[2]
        result['resource_id'] = row[3]
        return result

    def build_tool_attributes(self, tool_id, tool_name, tool_description, resource_id, resource_date):
        result = {}
        result['tool_id'] = tool_id
        result['tool_name'] = tool_name
        result['tool_description'] = tool_description
        result['resource_id'] = resource_id
        result['resource_date'] = resource_date
        return result

    def getAllTools(self):
        dao = ToolsDAO()
        tools_list = dao.getAllTools()
        result_list = []
        for row in tools_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)

    def getToolsById(self, tools_id):
        dao = ToolsDAO()
        row = dao.getToolsById(tools_id)
        if not row:
            return jsonify(Error="Tool Not Found"), 404
        else:
            tools = self.build_tool_dict(row)
            return jsonify(Tools=tools)

    def getResourceById(self, resource_id):
        dao = ToolsDAO()
        row = dao.getResourceById(resource_id)
        if row:
            result = self.build_tool_dict(row)
            # jsonify(Food=food)
            return result

    def get_resources_supplied(self):
        dao = ToolsDAO()
        resources_list = dao.get_resources_supplied()
        result_list = []
        for row in resources_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return result_list

    def get_available_resources(self):
        dao = ToolsDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list

    def get_resources_by_name(self, resource_name):
        dao = ToolsDAO()
        tool_list = []
        tool_list = dao.get_resources_by_name(resource_name)
        result_list = []
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return result_list

    def insertToolJson(self, json):
        print("json ", json)
        if len(json) != 3:
            return jsonify(Error="Malformed post request"), 400
        tool_name = json['tool_name']
        tool_description = json['tool_description']
        tool_date = json['tool_date']
        if tool_name and tool_description and tool_date:
            dao = ToolsDAO()
            tool_id_and_resource_id = dao.insert_tools(tool_name,tool_description,tool_date)
            result = self.build_tool_attributes(tool_id_and_resource_id[0], tool_name, tool_description,
                                                           tool_id_and_resource_id[1], tool_date)
            return jsonify(Power_Resource=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

