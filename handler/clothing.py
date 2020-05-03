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
        return result

    def build_clothe_attributes(self, clothe_id, clothe_type, clothe_size, clothe_description):
        result = {}
        result['clothe_id'] = clothe_id
        result['clothe_type'] = clothe_type
        result['clothe_size'] = clothe_size
        result['clothe_description'] = clothe_description
        return result

    def getAllclothes(self):
        dao = ClothingDAO()
        clothing_list = dao.getAllClothing()
        result_list = []
        for row in clothing_list:
            result = self.build_clothe_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClotheById(self, clothe_id):
        dao = ClothingDAO()
        row = dao.getClothingById(clothe_id)
        if not row:
            return jsonify(Error="Clothe not found"), 404
        else:
            food = self.build_clothe_dict(row)
            return jsonify(Clothing=food)

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

    def insertClotheJson(self, form):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            clothe_type = form['clothe_type']
            clothe_size = form['clothe_size']
            clothe_description = form['clothe_description']
            if clothe_type and clothe_size and clothe_description:
                clothe_id = self.insert_clothe(clothe_type, clothe_size, clothe_description)
                result = self.build_clothe_attributes(clothe_id, clothe_type, clothe_size, clothe_description)
                return jsonify(Clothe=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateClothe(self, clothe_id, form):
        if not self.getClotheById(clothe_id):
            return jsonify(Error = "Clothe not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                clothe_type = form['clothe_type']
                clothe_size = form['clothe_size']
                clothe_description = form['clothe_description']
                if clothe_type and clothe_size and clothe_description:
                    self.update_clothe(clothe_id, clothe_type, clothe_size, clothe_description)
                    result = self.build_clothe_attributes(clothe_id, clothe_size, clothe_description)
                    return jsonify(Cloth=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteClothe(self, clothe_id):
        if not self.getClotheById(clothe_id):
            return jsonify(Error="Clothe not found."), 404
        else:
            # dao.delete(pid)
            self.delete_clothe(clothe_id)
            return jsonify(DeleteStatus="OK"), 200