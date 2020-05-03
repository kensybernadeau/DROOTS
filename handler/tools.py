from flask import jsonify

from dao.tools import ToolsDAO


class ToolsHandler:
    tools = [(1, "destornillador", "de estrias"),
             (2, "destornillador", "de estrias"), ]

    # ----------------utils-------------------
    def give_me_tool(self):
        return self.tools

    def getById(self, tool_id):
        for f in self.tools:
            if tool_id == f[0]:
                return f

    def insert_tool(self, tool_name, tool_description):
        self.tools.append((len(self.tools) + 1, tool_name, tool_description))
        return len(self.tools)

    def update_tool(self, tool_id, tool_name, tool_description):
        self.tools.reomove(self.getById(tool_id))
        self.tools.insert(tool_id - 1, (tool_id, tool_name, tool_description))

    def delete_tool(self, tool_id):
        self.tools.remove(self.getById(tool_id))

    # --------------end utils-----------------

    def build_tool_dict(self, row):
        result = {}
        result['tool_id'] = row[0]
        result['tool_name'] = row[1]
        result['tool_description'] = row[2]
        return result

    def build_tool_attributes(self, tool_id, tool_name, tool_description):
        result = {}
        result['tool_id'] = tool_id
        result['tool_name'] = tool_name
        result['tool_description'] = tool_description
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

    def get_available_resources(self):
        dao = ToolsDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list

    def insertToolJson(self, form):
        print("form: ", form)
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            tool_name = form['tool_name']
            tool_description = form['tool_description']
            if tool_name and tool_description:
                tool_id = self.insert_tool(tool_name, tool_description)
                result = self.build_tool_attributes(tool_id, tool_name, tool_description)
                return jsonify(Tool=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateTool(self, tool_id, form):
        if not self.getToolById(tool_id):
            return jsonify(Error="Tool not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                tool_name = form['tool_name']
                tool_description = form['tool_description']
                if tool_name  and tool_description:
                    self.update_tool(tool_id, tool_name, tool_description)
                    result = self.build_tool_attributes(tool_id, tool_name, tool_description)
                    return jsonify(Tool=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteTool(self, tool_id):
        if not self.getToolById(tool_id):
            return jsonify(Error="Tool not found."), 404
        else:
            self.delete_tool(tool_id)
            return jsonify(DeleteStatus="OK"), 200
