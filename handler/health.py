from flask import jsonify


class HealthHandler:
    health = [(1, "panadol", 20, "05/30/2020", "pm", "for people"),
              (2, "tylenol", 30, "05/30/2020", "jiji", "for babies")]

    # ----------------utils-------------------
    def give_me_health(self):
        return self.health

    def getById(self, health_id):
        for f in self.health:
            if health_id == f[0]:
                return f

    def insert_health(self, health_name, health_quantity, health_exp_date, health_type, health_description):
        self.health.append(
            (len(self.health) + 1, health_name, health_quantity, health_exp_date, health_type, health_description))
        return len(self.health)

    def update_health(self, health_id, health_name, health_quantity, health_exp_date, health_type, health_description):
        self.health.remove(self.getById(health_id))
        self.health.insert(health_id - 1,
                           (health_id, health_name, health_quantity, health_exp_date, health_type, health_description))

    def delete_health(self, health_id):
        h = self.getById(health_id)
        self.health.remove(h)

    # --------------end utils-----------------

    def build_health_dict(self, row):
        result = {}
        result['health_id'] = row[0]
        result['health_name'] = row[1]
        result['health_quantity'] = row[2]
        result['health_exp_date'] = row[3]
        result['health_type'] = row[4]
        result['health_description'] = row[5]
        return result

    def build_health_attributes(self, health_id, health_name, health_quantity, health_exp_date, health_type,
                                health_description):
        result = {}
        result['health_id'] = health_id
        result['health_name'] = health_name
        result['health_quantity'] = health_quantity
        result['health_exp_date'] = health_exp_date
        result['health_type'] = health_type
        result['health_description'] = health_description
        return result

    def getAllHealth(self):
        hlist = self.give_me_health()
        result_list = []
        for row in hlist:
            result = self.build_health_dict(row)
            result_list.append(result)
        return jsonify(Health=result_list)

    def getHealthById(self, health_id):
        row = self.getById(health_id)
        if not row:
            return jsonify(Error="Health Not Found"), 404
        else:
            health = self.build_health_dict(row)
            return jsonify(Health=health)

    def insertHealthJson(self, json):
        print("json: ", json)
        if len(json) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            health_name = json['health_name']
            health_quantity = json['health_quantity']
            health_exp_date = json['health_exp_date']
            health_type = json['health_type']
            health_description = json['health_description']
            if health_name and health_quantity and health_exp_date and health_type and health_description:
                health_id = self.insert_health(health_name, health_quantity, health_exp_date, health_type,
                                               health_description)
                result = self.build_health_attributes(health_id, health_name, health_quantity, health_exp_date,
                                                      health_type, health_description)
                return jsonify(Health=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateHealth(self, health_id, form):
        if not self.getHealthById(health_id):
            return jsonify(Error="Health not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                health_name = form['health_name']
                health_quantity = form['health_quantity']
                health_exp_date = form['health_exp_date']
                health_type = form['health_type']
                health_description = form['health_description']
                if health_name and health_quantity and health_exp_date and health_type and health_description:
                    self.update_health(health_id, health_name, health_quantity, health_exp_date, health_type,
                                       health_description)
                    result = self.build_health_attributes(health_id, health_name, health_quantity, health_exp_date,
                                                          health_type, health_description)
                    return jsonify(Health=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteHealth(self, health_id):
        if not self.getHealthById(health_id):
            return jsonify(Error="Health not found."), 404
        else:
            self.delete_health(health_id)
            return jsonify(DeleteStatus="OK"), 200
