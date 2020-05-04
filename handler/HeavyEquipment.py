from flask import jsonify

from dao.heavy_equipment import HeavyEquipmentDAO


class HeavyEquipmentHandler:

    hequipment =   [(1,'Carpa','30 metros'),(2,'Digger','1500Lbs'),(3,'Cama','Ortopedica')]

    #----------------utils-------------------
    def give_me_hequipment(self):
        return self.hequipment

    def getById(self, hequipment_id):
        for f in self.hequipment:
            if hequipment_id == f[0]:
                return f

    def insert_hequipment(self, hequipment_name, hequipment_description):
        self.hequipment.append((len(self.hequipment) + 1, hequipment_name, hequipment_description))
        return len(self.hequipment)

    def update_hequipment(self, hequipment_id, hequipment_name, hequipment_description):
        self.hequipment.remove(self.getById(hequipment_id))
        self.hequipment.insert(hequipment_id-1, (hequipment_name, hequipment_description))

    def delete_hequipment(self, hequipment_id):
        self.hequipment.remove(self.getById(hequipment_id))
    #--------------end utils-----------------

    def build_heavy_dict(self, list):
        result = {}
        result['hequipment_id'] = list[0]
        result['hequipment_name'] = list[1]
        result['hequipment_description'] = list[2]
        return result

    def build_heavy_attributes(self, hequipment_id, hequipment_name, hequipment_description):
        result = {}
        result['hequipment_id'] = hequipment_id
        result['hequipment_name'] = hequipment_name
        result['hequipment_description'] = hequipment_description
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

    def insertHEquipmentJson(self, form):
        print("form: ", form)
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            hequipment_name = form['hequipment_name']
            hequipment_description = form['hequipment_description']
            if hequipment_name and hequipment_description:
                hequipment_id = self.insert_hequipment(hequipment_name, hequipment_description)
                result = self.build_hequipment_attributes(hequipment_id, hequipment_name, hequipment_description)
                return jsonify(HeavyEquipment=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateHEquipment(self, hequipment_id, form):
        if not self.getHEquipmentById(hequipment_id):
            return jsonify(Error = "HeavyEquipment not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                hequipment_name = form['hequipment_name']
                hequipment_description = form['hequipment_description']
                if hequipment_name and hequipment_description:
                    self.update_hequipment(hequipment_id, hequipment_name, hequipment_description)
                    result = self.build_hequipment_attributes(hequipment_id, hequipment_name, hequipment_description)
                    return jsonify(HeavyEquipment=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteHEquipment(self, hequipment_id):
        if not self.getHEquipmentById(hequipment_id):
            return jsonify(Error="HeavyEquipment not found."), 404
        else:
            self.delete_hequipment(hequipment_id)
            return jsonify(DeleteStatus="OK"), 200