from flask import jsonify

from dao.clothing import ClothingDAO


class ClothingHandler:

    def build_clothe_dict(self, row):
        result = {}
        result['clothe_id'] = row[0]
        result['clothe_name'] = row[1]
        result['clothe_size'] = row[2]
        result['clothe_type'] = row[3]
        result['clothe_description'] = row[4]
        result['resource_id'] = row[5]
        return result

    def build_clothe_attributes(self, clothe_id, clothe_name, clothe_type, clothe_size, clothe_description, resource_id,
                                resource_date):
        result = {}
        result['clothe_id'] = clothe_id
        result['clothe_name'] = clothe_name
        result['clothe_type'] = clothe_type
        result['clothe_size'] = clothe_size
        result['clothe_description'] = clothe_description
        result['resource_id'] = resource_id
        result['resource_date'] = resource_date
        return result

    def getAllclothes(self):
        dao = ClothingDAO()
        clothing_list = dao.getAllClothing()
        result_list = []
        for row in clothing_list:
            result = self.build_clothe_dict(row)
            result_list.append(result)
        return jsonify(Clothing=result_list)

    def getClotheById(self, clothe_id):
        dao = ClothingDAO()
        row = dao.getClothingById(clothe_id)
        if not row:
            return jsonify(Error="Clothe not found"), 404
        else:
            food = self.build_clothe_dict(row)
            return jsonify(Clothing=food)

    def getResourceById(self, resource_id):
        dao = ClothingDAO()
        row = dao.getResourceById(resource_id)
        if row:
            result = self.build_clothe_dict(row)
        # jsonify(Food=food)
            return result

    def get_available_resources(self):
        dao = ClothingDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_clothe_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list

    def get_resources_supplied(self):
        dao = ClothingDAO()
        resources_list = dao.get_resources_supplied()
        result_list = []
        for row in resources_list:
            result = self.build_clothe_dict(row)
            result_list.append(result)
        return result_list

    def get_resources_by_name(self, resource_name):
        dao = ClothingDAO()
        clothing_list = []
        clothing_list = dao.get_resources_by_name(resource_name)
        result_list = []
        for row in clothing_list:
            result = self.build_clothe_dict(row)
            result_list.append(result)
        return result_list

    def insertClotheJson(self, json):
        print("json: ", json)
        if len(json) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            clothe_name = json['clothe_name']
            clothe_type = json['clothe_type']
            clothe_size = json['clothe_size']
            clothe_description = json['clothe_description']
            clothe_date = json['clothe_date']
            if clothe_name and clothe_type and clothe_size and clothe_description and clothe_date:
                dao = ClothingDAO()
                clothe_and_resource_id = dao.insert_clothing(clothe_name, clothe_type, clothe_size, clothe_description,
                                                             clothe_date)
                result = self.build_clothe_attributes(clothe_and_resource_id[0], clothe_name, clothe_type, clothe_size,
                                                      clothe_description, clothe_and_resource_id[1], clothe_date)
                return jsonify(Clothing=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
