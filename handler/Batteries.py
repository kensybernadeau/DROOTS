from flask import jsonify

from dao.batteries import BatteriesDAO


class BatteriesHandler:

    def build_battery_dict(self, list):
        result = {}
        result['battery_id'] = list[0]
        result['battery_name'] = list[1]
        result['battery_material'] = list[2]
        result['battery_voltage'] = list[3]
        result['battery_type'] = list[4]
        result['battery_description'] = list[5]
        result['resource_id'] = list[6]
        return result

    def build_battery_attributes(self, batteries_id, battery_name, battery_material, batteries_voltage, batteries_type, resource_description, resource_id, resource_date):
        result = {}
        result['battery_id'] = batteries_id
        result['battery_name'] = battery_name
        result['battery_material'] = battery_material
        result['battery_voltage'] = batteries_voltage
        result['battery_type'] = batteries_type
        result['battery_description'] = resource_description
        result['resource_id'] = resource_id
        result['resource_date'] = resource_date
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
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            battery_name = form['battery_name']
            battery_material = form['battery_material']
            battery_voltage = form['battery_voltage']
            battery_type = form['battery_type']
            battery_description = form['battery_description']
            battery_date = form['battery_date']
            if battery_name and battery_material and battery_voltage and battery_type and battery_description and battery_date:
                dao = BatteriesDAO()
                battery_id_and_resource_id = dao.insert_battery(battery_name, battery_material, battery_voltage, battery_type, battery_description, battery_date)
                result = self.build_battery_attributes(battery_id_and_resource_id[0], battery_name, battery_material,
                                                       battery_voltage, battery_type, battery_description,
                                                       battery_id_and_resource_id[1], battery_date)
                return jsonify(Batteries=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

