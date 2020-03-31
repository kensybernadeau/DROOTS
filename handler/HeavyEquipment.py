from flask import jsonify


class HeavyEquipmentHandler:

    hequipment = [(1,'Carpa','30 metros'),(2,'Digger','1500Lbs'),(3,'Cama','Ortopedica')]

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
        self.hequipment.pop(hequipment_id-1)
        self.hequipment.insert(hequipment_id-1, (hequipment_name, hequipment_description))

    def delete_hequipment(self, hequipment_id):
        self.hequipment.pop(hequipment_id - 1)
    #--------------end utils-----------------

    def build_hequipment_dict(self, list):
        result = {}
        result['hequipment_id'] = list[0]
        result['hequipment_name'] = list[1]
        result['hequipment_description'] = list[2]
        return result

    def build_hequipment_attributes(self, hequipment_id, hequipment_name, hequipment_description):
        result = {}
        result['hequipment_id'] = hequipment_id
        result['hequipment_name'] = hequipment_name
        result['hequipment_description'] = hequipment_description
        return result

    def getAllHEquipment(self):
        list = self.give_me_hequipment()
        result_list = []
        for row in list:
            result = self.build_hequipment_dict(row)
            result_list.append(result)
        return jsonify(HeavyEquipment=result_list)

    def getHEquipmentById(self, hequipment_id):
        row = self.getById(hequipment_id)
        if not row:
            return jsonify(Error="HeavyEquipment Not Found"), 404
        else:
            hequipment = self.build_hequipment_dict(row)
            return jsonify(HeavyEquipment=hequipment)

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