from flask import jsonify


class ToolsHandler:

    tools = [(1, "destornillador", "de estrias"),
            (2, "destornillador", "de estrias"),]

    #----------------utils-------------------
    def give_me_tool(self):
        return self.tools

    def getById(self, tool_id):
        for f in self.tools:
            if tool_id == f[0]:
                return f

    def insert_food(self, tool_name, tool_description):
        self.tools.append((len(self.tools) + 1, tool_name, tool_description))
        return len(self.tools)

    def update_tool(self, tool_id, tool_name, tool_description):
        self.tools.pop(tool_id-1)
        self.tools.insert(tool_id-1, (tool_id, tool_name, tool_description))

    def delete_tool(self, tool_id):
        self.tools.pop(tool_id - 1)
    #--------------end utils-----------------

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
        # dao = SupplierDAO()
        # suppliers_list = dao.getAllSuppliers()
        flist = self.give_me_tool()
        result_list = []
        for row in flist:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)

    def getToolById(self, tool_id):
        # dao = PartsDAO()
        # row = dao.getPartById(pid)
        row = self.getById(tool_id)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            tool = self.build_tool_dict(row)
            return jsonify(Tool=tool)

    def insertToolJson(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            tool_name = form['tool_name']
            tool_description = form['tool_description']
            if tool_name and tool_description:
                # dao = PartsDAO()
                # pid = dao.insert(pname, pcolor, pmaterial, pprice)
                tool_id = self.insert_food(tool_name, tool_description)
                result = self.build_part_attributes(tool_id, tool_name, tool_description)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateTool(self, tool_id, form):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getToolById(tool_id):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                tool_name = form['tool_name']
                tool_type = form['tool_type']
                tool_description = form['tool_description']
                if tool_name and tool_type and tool_description:
                    # dao.update(pid, pname, pcolor, pmaterial, pprice)
                    self.update_tool(tool_id, tool_name, tool_type, tool_description)
                    result = self.build_tool_attributes(tool_id, tool_name, tool_type, tool_description)
                    return jsonify(Tool=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteTool(self, tool_id):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getToolById(tool_id):
            return jsonify(Error="Part not found."), 404
        else:
            # dao.delete(pid)
            self.delete_tool(tool_id)
            return jsonify(DeleteStatus="OK"), 200