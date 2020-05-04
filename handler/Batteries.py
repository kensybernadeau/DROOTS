from flask import jsonify

from dao.batteries import BatteriesDAO


class BatteriesHandler:
    batteries =  [(1, 'Lithium Ion', '1.5', '4'), (2, 'Acid', '1.5', '8'), (3, 'Lead Acid', '9', '12')]

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
        self.batteries.remove(self.getById(batteries_id))
        self.batteries.insert(batteries_id - 1, (batteries_id, batteries_type, batteries_voltage, batteries_quantity))

    def delete_batteries(self, batteries_id):
        self.batteries.remove(self.getById(batteries_id))

    # --------------end utils-----------------

    def build_battery_dict(self, list):
        result = {}
        result['battery_id'] = list[0]
        result['battery_name'] = list[1]
        result['battery'] = list[2]
        result['battery_type'] = list[3]
        result['battery_voltage'] = list[4]
        result['resource_id'] = list[5]
        return result

    def build_batteries_attributes(self, batteries_id, batteries_type, batteries_voltage, batteries_quantity):
        result = {}
        result['battery_id'] = batteries_id
        result['battery_type'] = batteries_type
        result['battery_voltage'] = batteries_voltage
        result['battery_quantity'] = batteries_quantity
        return result

    def getAllBatteries(self):
        dao = BatteriesDAO()
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Batteries=result_list)

    def getBatteriesById(self, battery_id):
        dao = BatteriesDAO()
        row = dao.getBatteriesById(battery_id)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            battery = self.build_battery_dict(row)
            return jsonify(Batteries=battery)

    def getResourceById(self, resource_id):
        dao = BatteriesDAO()
        row = dao.getResourceById(resource_id)
        if row:
            result = self.build_battery_dict(row)
        # jsonify(Food=food)
            return result

    def get_available_resources(self):
        dao = BatteriesDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list

    def get_resources_supplied(self):
        dao = BatteriesDAO()
        resources_list = dao.get_resources_supplied()
        result_list = []
        for row in resources_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return result_list

    def get_resources_by_name(self, resource_name):
        dao = BatteriesDAO()
        batteries_list = []
        batteries_list = dao.get_resources_by_name(resource_name)
        result_list = []
        for row in batteries_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return result_list

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
