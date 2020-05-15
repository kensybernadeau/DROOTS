from flask import jsonify

from dao.heavy_equipment import HeavyEquipmentDAO


class HeavyEquipmentHandler:

    def build_heavy_dict(self, list):
        result = {}
        result['hequipment_id'] = list[0]
        result['hequipment_name'] = list[1]
        result['hequipment_description'] = list[2]
        result['resource_id'] = list[3]
        return result

    def build_heavy_attributes(self, hequipment_id, hequipment_name, hequipment_description, resource_date):
        result = {}
        result['hequipment_id'] = hequipment_id
        result['hequipment_name'] = hequipment_name
        result['hequipment_description'] = hequipment_description
        result['resource_date'] = resource_date
        return result

    def getAllHeavyEquipment(self):
        dao = HeavyEquipmentDAO()
        heavy_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in heavy_list:
            result = self.build_heavy_dict(row)
            result_list.append(result)
        return jsonify(HeavyEquipment=result_list)

    def getHeavyEquipmentById(self, heavy_id):
        dao = HeavyEquipmentDAO()
        row = dao.getHeavyEquipmentById(heavy_id)
        if not row:
            return jsonify(Error="Equipment Not Found"), 404
        else:
            heavy = self.build_heavy_dict(row)
            return jsonify(HeavyEquipment=heavy)

    def getResourceById(self, resource_id):
        dao = HeavyEquipmentDAO()
        row = dao.getResourceById(resource_id)
        if row:
            result = self.build_heavy_dict(row)
        # jsonify(Food=food)
            return result

    def get_available_resources(self):
        dao = HeavyEquipmentDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_heavy_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list

    def get_resources_supplied(self):
        dao = HeavyEquipmentDAO()
        resources_list = dao.get_resources_supplied()
        result_list = []
        for row in resources_list:
            result = self.build_heavy_dict(row)
            result_list.append(result)
        return result_list

    def get_resources_by_name(self, resource_name):
        dao = HeavyEquipmentDAO()
        heavy_list = []
        heavy_list = dao.get_resources_by_name(resource_name)
        result_list = []
        for row in heavy_list:
            result = self.build_heavy_dict(row)
            result_list.append(result)
        return result_list

    def insertHeavyEquipmentJson(self, json):
        print("json ", json)
        if len(json) != 3:
            return jsonify(Error="Malformed post request"), 400
        heavy_name = json['heavy_name']
        heavy_description = json['heavy_description']
        heavy_date = json['heavy_date']
        if heavy_name  and heavy_description and heavy_date:
            dao = HeavyEquipmentDAO()
            heavy_and_resource_id = dao.insert_heavy_equipment(heavy_name, heavy_description, heavy_date)
            result = self.build_heavy_attributes(heavy_and_resource_id [0], heavy_name, heavy_description,
                                                heavy_and_resource_id[1], heavy_date)
            return jsonify(Fuel=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    # def updateHEquipment(self, hequipment_id, form):
    #     if not self.getHEquipmentById(hequipment_id):
    #         return jsonify(Error = "HeavyEquipment not found."), 404
    #     else:
    #         if len(form) != 2:
    #             return jsonify(Error="Malformed update request"), 400
    #         else:
    #             hequipment_name = form['hequipment_name']
    #             hequipment_description = form['hequipment_description']
    #             if hequipment_name and hequipment_description:
    #                 self.update_hequipment(hequipment_id, hequipment_name, hequipment_description)
    #                 result = self.build_heavy_attributes(hequipment_id, hequipment_name, hequipment_description)
    #                 return jsonify(HeavyEquipment=result), 200
    #             else:
    #                 return jsonify(Error="Unexpected attributes in update request"), 400
    #
    # def deleteHEquipment(self, hequipment_id):
    #     if not self.getHEquipmentById(hequipment_id):
    #         return jsonify(Error="HeavyEquipment not found."), 404
    #     else:
    #         self.delete_hequipment(hequipment_id)
    #         return jsonify(DeleteStatus="OK"), 200