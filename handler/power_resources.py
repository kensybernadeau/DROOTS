from flask import jsonify


class PowerResourcesHandler:
    power_resources = [(1, "fuel", 20), (2, "diesel", 40), (3, "electric panels", 10)]

    # ----------------utils-------------------
    def give_me_power_resources(self):
        return self.power_resources

    def getById(self, user_id):
        for f in self.power_resources:
            if user_id == f[0]:
                return f

    def insert_power_resource(self, power_category, power_quantity):
        self.power_resources.append((len(self.power_resources) + 1, power_category, power_quantity))
        return len(self.power_resources)

    def update_power_resource(self, power_resource_id, power_category, power_quantity):
        self.power_resources.pop(power_resource_id - 1)
        self.power_resources.insert(power_resource_id - 1, (power_resource_id, power_category, power_quantity))

    def delete_power_resource(self, power_resource_id):
        self.power_resources.pop(power_resource_id - 1)

        # --------------end utils-----------------

    def build_power_resources_dict(self, row):
        result = {}
        result['power_resource_id'] = row[0]
        result['power_resource_category'] = row[1]
        result['power_resource_quantity'] = row[2]

        return result

    def build_power_resources_attributes(self, power_resource_id, power_resource_category, power_resource_quantity):
        result = {}
        result['power_resource_id'] = power_resource_id
        result['power_resource_category'] = power_resource_category
        result['power_resource_quantity'] = power_resource_quantity
        return result

    def getAllPowerResources(self):
        prlist = self.give_me_power_resources()
        result_list = []
        for row in prlist:
            result = self.build_power_resources_dict(row)
            result_list.append(result)
        return jsonify(Power_Resources=result_list)

    def getPowerResourceById(self, power_resource_id):
        row = self.getById(power_resource_id)
        if not row:
            return jsonify(Error="Power Resource Not Found"), 404
        else:
            power_resource = self.build_power_resources_dict(row)
            return jsonify(Power_Resource=power_resource)

    def insertPowerResourceJson(self, json):
        print("json ", json)
        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400
        power_resource_category = json['power_resource_category']
        power_resource_quantity = json['power_resource_quantity']

        if power_resource_category and power_resource_quantity:
            power_resource_id = self.insert_power_resource(power_resource_category, power_resource_quantity)
            result = self.build_power_resources_attributes(power_resource_id, power_resource_category, power_resource_quantity)
            return jsonify(Power_Resource=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updatePowerResource(self, power_resource_id, form):
        if not self.getById(power_resource_id):
            return jsonify(Error="Power Resource not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                power_resource_category = form['power_resource_category']
                power_resource_quantity = form['power_resource_quantity']
                if power_resource_category and power_resource_quantity:
                    self.update_power_resource(power_resource_id, power_resource_category, power_resource_quantity)
                    result = self.build_power_resources_attributes(1, power_resource_category, power_resource_quantity)
                    return jsonify(Power_Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deletePowerResource(self, power_resource_id):
        if not self.getById(power_resource_id):
            return jsonify(Error="Power Resource not found."), 404
        else:
            self.delete_power_resource(power_resource_id)
            return jsonify(DeleteStatus="OK"), 200
