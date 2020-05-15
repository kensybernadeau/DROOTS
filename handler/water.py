from flask import jsonify

from dao.water import WaterDAO


class WaterHandler:

    def build_water_dict(self, row):
        result = {}
        result['water_id'] = row[0]
        result['water_name'] = row[1]
        result['water_oz'] = row[2]
        result['water_type'] = row[3]
        result['resource_id'] = row[4]
        return result

    def build_water_attributes(self, water_id, water_name, water_oz, water_type, resource_id, resource_date):
        result = {}
        result['water_id'] = water_id
        result['water_name'] = water_name
        result['water_oz'] = water_oz
        result['water_type'] = water_type
        result['resource_id'] = resource_id
        result['resource_date'] = resource_date
        return result

    def getAllWater(self):
        dao = WaterDAO()
        water_list = dao.getAllWater()
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Water=result_list)

    def getWaterById(self, water_id):
        dao = WaterDAO()
        row = dao.getWaterById(water_id)
        if not row:
            return jsonify(Error="Water Not Found"), 404
        else:
            water = self.build_water_dict(row)
            return jsonify(Water=water)

    def getResourceById(self, resource_id):
        dao = WaterDAO()
        row = dao.getResourceById(resource_id)
        if row:
            result = self.build_water_dict(row)
            # jsonify(water=water)
            return result

    def get_available_resources(self):
        dao = WaterDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list

    def get_resources_supplied(self):
        dao = WaterDAO()
        resources_list = dao.get_resources_supplied()
        result_list = []
        for row in resources_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return result_list

    def get_resources_by_name(self, resource_name):
        dao = WaterDAO()
        water_list = []
        water_list = dao.get_resources_by_name(resource_name)
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return result_list

    def get_water_by_type(self, water_type):
        dao = WaterDAO()
        water_list = []
        water_list = dao.get_water_by_type(water_type)
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Water=result_list)

    def insertWaterJson(self, json):
        print("json ", json)
        if len(json) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            water_name = json['water_name']
            water_oz = json['water_oz']
            water_type = json['water_type']
            water_date = json['water_date']
            if water_name and water_oz and water_type and water_date:
                dao = WaterDAO()
                water_and_resource_id = dao.insert_water(water_name, water_oz, water_type, water_date)
                result = self.build_water_attributes(water_and_resource_id[0], water_name, water_oz, water_type,
                                                     water_and_resource_id[1], water_date)
                return jsonify(Water=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
