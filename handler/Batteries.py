from flask import jsonify


class BatteriesHandler:
    batteries = [(1, 'AA', '1.5', '4'), (2, 'AAA', '1.5', '8'), (3, 'D', '9', '12')]

    # ----------------utils-------------------
    def give_me_batteries(self):
        return self.batteries

    def getById(self, batteries_id):
        for f in self.batteries:
            if batteries_id == f[0]:
                return f

    def insert_batteries(self, batteries_type, batteries_voltage, batteries_quantity):
        self.batteries.append((len(self.batteries) + 1, batteries_type, batteries_voltage, batteries_quantity))
        return len(self.batteries)

    def update_batteries(self, batteries_id, batteries_type, batteries_voltage, batteries_quantity):
        self.batteries.pop(batteries_id - 1)
        self.batteries.insert(batteries_id - 1, (batteries_id, batteries_type, batteries_voltage, batteries_quantity))

    def delete_batteries(self, batteries_id):
        self.batteries.pop(batteries_id - 1)

    # --------------end utils-----------------

    def build_batteries_dict(self, list):
        result = {}
        result['batteries_id'] = list[0]
        result['batteries_type'] = list[1]
        result['batteries_voltage'] = list[2]
        result['batteries_quantity'] = list[3]
        return result

    def build_batteries_attributes(self, batteries_id, batteries_type, batteries_voltage, batteries_quantity):
        result = {}
        result['batteries_id'] = batteries_id
        result['batteries_type'] = batteries_type
        result['batteries_voltage'] = batteries_voltage
        result['batteries_quantity'] = batteries_quantity
        return result

    def getAllBatteries(self):
        list = self.give_me_batteries()
        result_list = []
        for row in list:
            result = self.build_batteries_dict(row)
            result_list.append(result)
        return jsonify(Batteries=result_list)

    def getBatteriesById(self, batteries_id):
        row = self.getById(batteries_id)
        if not row:
            return jsonify(Error="Batteries Not Found"), 404
        else:
            batteries = self.build_batteries_dict(row)
            return jsonify(Batteries=batteries)

    def insertBatteriesJson(self, form):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            batteries_type = form['batteries_type']
            batteries_voltage = form['batteries_voltage']
            batteries_quantity = form['batteries_quantity']
            if batteries_type and batteries_voltage and batteries_quantity:
                batteries_id = self.insert_batteries(batteries_type, batteries_voltage, batteries_quantity)
                result = self.build_batteries_attributes(batteries_id, batteries_type, batteries_voltage,
                                                         batteries_quantity)
                return jsonify(Batteries=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateBatteries(self, batteries_id, form):
        if not self.getBatteriesById(batteries_id):
            return jsonify(Error="Batteries not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                batteries_type = form['batteries_type']
                batteries_voltage = form['batteries_voltage']
                batteries_quantity = form['batteries_quantity']
                if batteries_type and batteries_voltage and batteries_quantity:
                    self.update_batteries(batteries_id, batteries_type, batteries_voltage, batteries_quantity)
                    result = self.build_batteries_attributes(batteries_id, batteries_type, batteries_voltage,
                                                             batteries_quantity)
                    return jsonify(Batteries=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteBatteries(self, batteries_id):
        if not self.getBatteriesById(batteries_id):
            return jsonify(Error="Batteries not found."), 404
        else:
            self.delete_batteries(batteries_id)
            return jsonify(DeleteStatus="OK"), 200
