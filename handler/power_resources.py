from flask import jsonify

from dao.power_resources import PowerResourcesDAO


class PowerResourcesHandler:

    def build_power_resources_dict(self, row):
        result = {}
        result['power_resource_id'] = row[0]
        result['power_resource_name'] = row[1]
        result['power_resource_type'] = row[2]
        result['power_resource_description'] = row[3]
        result['resource_id'] = row[4]
        return result

    def build_power_resources_attributes(self, power_resource_id, power_resource_name, power_resource_type,
                                         power_resource_description, resource_id, resource_date):
        result = {}
        result['power_resource_id'] = power_resource_id
        result['power_resource_name'] = power_resource_name
        result['power_resource_type'] = power_resource_type
        result['power_resource_description'] = power_resource_description
        result['resource_id'] = resource_id
        result['resource_date'] = resource_date
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

    def getResourceById(self, resource_id):
        dao = PowerResourcesDAO()
        row = dao.getResourceById(resource_id)
        if row:
            result = self.build_power_resources_dict(row)
        # jsonify(Food=food)
            return result

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
        if len(json) != 4:
            return jsonify(Error="Malformed post request"), 400
        power_resource_name = json['power_resource_name']
        power_resource_type = json['power_resource_type']
        power_resource_description = json['power_resource_description']
        power_resource_date = json['power_resource_date']
        if power_resource_name and power_resource_type and power_resource_description and power_resource_date:
            dao = PowerResourcesDAO()
            power_resource_id_and_resource_id = dao.insert_power_resource(power_resource_name, power_resource_type,
                                                                          power_resource_description,
                                                                          power_resource_date)
            result = self.build_power_resources_attributes(power_resource_id_and_resource_id[0], power_resource_name,
                                                           power_resource_type, power_resource_description,
                                                           power_resource_id_and_resource_id[1], power_resource_date)
            return jsonify(Power_Resource=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

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
