from flask import jsonify

from dao.power_resources import PowerResourcesDAO


class PowerResourcesHandler:
    power_resources = [(1, "batteries", "AA", "5v batteries"), (2, "fuel", "diesel", ""),
                       (3, "solar", "panels", "Tesla")]

    # ----------------utils-------------------
    def give_me_power_resources(self):
        return self.power_resources

    def getById(self, power_resource_id):
        for f in self.power_resources:
            if power_resource_id == f[0]:
                return f

    def getByCategory(self, pr_category):
        result = []
        for row in self.power_resources:
            if row[1] == pr_category:
                result.append(row)
        return result

    def getByCategoryAndType(self, pr_category, pr_type):
        result = []
        for row in self.power_resources:
            if row[1] == pr_category and row[2] == pr_type:
                result.append(row)
        return result

    def insert_power_resource(self, power_resource_category, power_resource_type, power_resource_description):
        self.power_resources.append(
            (len(self.power_resources) + 1, power_resource_category, power_resource_type, power_resource_description))
        return len(self.power_resources)

    def update_power_resource(self, power_resource_id, power_resource_category, power_resource_type,
                              power_resource_description):
        self.power_resources.remove(self.getById(power_resource_id))
        self.power_resources.insert(power_resource_id - 1, (
        power_resource_id, power_resource_category, power_resource_type, power_resource_description))

    def delete_power_resource(self, power_resource_id):
        result = self.getById(power_resource_id)
        self.power_resources.remove(result)

        # --------------end utils-----------------

    def build_power_resources_dict(self, row):
        result = {}
        result['power_resource_id'] = row[0]
        result['power_resource_name'] = row[1]
        result['power_resource_type'] = row[2]
        result['power_resource_description'] = row[3]
        return result

    def build_power_resources_attributes(self, power_resource_id, power_resource_category, power_resource_type,
                                         power_resource_description):
        result = {}
        result['power_resource_id'] = power_resource_id
        result['power_resource_category'] = power_resource_category
        result['power_resource_quantity'] = power_resource_type
        result['power_resource_description'] = power_resource_description
        return result

    def getAllPowerResources(self):
        dao = PowerResourcesDAO()
        power_resources_list = dao.getAllPowerResources()
        result_list = []
        for row in power_resources_list:
            result = self.build_power_resources_dict(row)
            result_list.append(result)
        return jsonify(PowerResources=result_list)

    def getPowerResourcesById(self, power_resources_id):
        dao = PowerResourcesDAO()
        row = dao.getPowerResourcesById(power_resources_id)
        if not row:
            return jsonify(Error="Power Resource Not Found"), 404
        else:
            power_resources = self.build_power_resources_dict(row)
            return jsonify(PowerResources=power_resources)

    def get_available_resources(self):
        dao = PowerResourcesDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_power_resources_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list

    def get_resources_supplied(self):
        dao = PowerResourcesDAO()
        resources_list = dao.get_resources_supplied()
        result_list = []
        for row in resources_list:
            result = self.build_power_resources_dict(row)
            result_list.append(result)
        return result_list

    def get_resources_by_name(self, resource_name):
        dao = PowerResourcesDAO()
        power_resources_list = []
        power_resources_list = dao.get_resources_by_name(resource_name)
        result_list = []
        for row in power_resources_list:
            result = self.build_power_resources_dict(row)
            result_list.append(result)
        return result_list

    def insertPowerResourceJson(self, json):
        print("json ", json)
        if len(json) != 3:
            return jsonify(Error="Malformed post request"), 400
        power_resource_category = json['power_resource_category']
        power_resource_type = json['power_resource_type']
        power_resource_description = json['power_resource_description']

        if power_resource_category and power_resource_type and power_resource_description:
            power_resource_id = self.insert_power_resource(power_resource_category, power_resource_type,
                                                           power_resource_description)
            result = self.build_power_resources_attributes(power_resource_id, power_resource_category,
                                                           power_resource_type, power_resource_description)
            return jsonify(Power_Resource=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updatePowerResource(self, power_resource_id, form):
        if not self.getById(power_resource_id):
            return jsonify(Error="Power Resource not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                power_resource_category = form['power_resource_category']
                power_resource_type = form['power_resource_type']
                power_resource_description = form['power_resource_description']
                if power_resource_category and power_resource_type and power_resource_description:
                    self.update_power_resource(power_resource_id, power_resource_category, power_resource_type,
                                               power_resource_description)
                    result = self.build_power_resources_attributes(1, power_resource_category, power_resource_type,
                                                                   power_resource_description)
                    return jsonify(Power_Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deletePowerResource(self, power_resource_id):
        if not self.getById(power_resource_id):
            return jsonify(Error="Power Resource not found."), 404
        else:
            self.delete_power_resource(power_resource_id)
            return jsonify(DeleteStatus="OK"), 200

    def searchPowerResources(self, args):
        pr_category = args.get("power_resource_category")
        pr_type = args.get("power_resource_type")
        pr_list = []
        if (len(args) == 1) and pr_category:
            pr_list = self.getByCategory(pr_category)

        elif len(args) == 2 and pr_category and pr_type:
            pr_list = self.getByCategoryAndType(pr_category,pr_type)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in pr_list:
            result = self.build_power_resources_dict(row)
            result_list.append(result)
        return jsonify(Power_Resources=result_list)
