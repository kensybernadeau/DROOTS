from flask import jsonify


class AdministratorsHandler:
    administrators = [(1, "Tito", "Trinidad"), (2, "Benito", "Martinez"), (3, "Javier", "Perez")]

    # ----------------utils-------------------
    def give_me_administrators(self):
        return self.administrators

    def getById(self, administrator_id):
        for f in self.administrators:
            if administrator_id == f[0]:
                return f

    def insert_administrator(self, administrator_fname, administrator_lname):
        self.administrators.append((len(self.administrators) + 1, administrator_fname, administrator_lname))
        return len(self.administrators)

    def update_administrator(self, administrator_id, administrator_fname, administrator_lname):
        self.administrators.pop(administrator_id - 1)
        self.administrators.insert(administrator_id - 1, (administrator_id, administrator_fname, administrator_lname))

    def delete_administrator(self, administrator_id):
        self.administrators.remove(self.getById(administrator_id))

        # --------------end utils-----------------

    def build_administrator_dict(self, row):
        result = {}
        result['administrator_id'] = row[0]
        result['administrator_fname'] = row[1]
        result['administrator_lname'] = row[2]

        return result

    def build_administrator_attributes(self, administrator_id, administrator_fname, administrator_lname):
        result = {}
        result['administrator_id'] = administrator_id
        result['administrator_fname'] = administrator_fname
        result['administrator_lname'] = administrator_lname
        return result

    def getAllAdministrators(self):
        ulist = self.give_me_administrators()
        result_list = []
        for row in ulist:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators=result_list)

    def getAdministratorById(self, administrator_id):
        row = self.getById(administrator_id)
        if not row:
            return jsonify(Error="Administrator Not Found"), 404
        else:
            admin = self.build_administrator_dict(row)
            return jsonify(Administrator=admin)

    def insertAdministratorJson(self, json):
        print("json ", json)
        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400
        administrator_fname = json['administrator_fname']
        administrator_lname = json['administrator_lname']

        if administrator_fname and administrator_lname:
            administrator_id = self.insert_administrator(administrator_fname, administrator_lname)
            result = self.build_administrator_attributes(administrator_id, administrator_fname, administrator_lname)
            return jsonify(Administrator=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateAdministrator(self, administrator_id, form):
        if not self.getById(administrator_id):
            return jsonify(Error="Administrator not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                administrator_fname = form['administrator_fname']
                administrator_lname = form['administrator_lname']
                if administrator_fname and administrator_lname:
                    self.update_administrator(administrator_id, administrator_fname, administrator_lname)
                    result = self.build_administrator_attributes(administrator_id, administrator_fname,
                                                                 administrator_lname)
                    return jsonify(Administrator=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteAdministrator(self, administrator_id):
        if not self.getById(administrator_id):
            return jsonify(Error="Administrator not found."), 404
        else:
            self.delete_administrator(administrator_id)
            return jsonify(DeleteStatus="OK"), 200
