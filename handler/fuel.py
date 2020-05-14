from flask import jsonify

from dao.fuel import FuelDAO


class FuelHandler:

    def build_fuel_dict(self, row):
        result = {}
        result['fuel_id'] = row[0]
        result['fuel_name'] = row[1]
        result['fuel_type'] = row[2]
        result['fuel_liters'] = row[3]
        result['resource_id'] = row[4]
        return result

    def build_fuel_attributes(self, fuel_id, fuel_name, fuel_type, fuel_liters, resource_id, resource_date):
        result = {}
        result['fuel_id'] = fuel_id
        result['fuel_name'] = fuel_name
        result['fuel_type'] = fuel_type
        result['fuel_liters'] = fuel_liters
        result['resource_id'] = resource_id
        result['resource_date'] = resource_date
        return result

    def getAllFuel(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def getFuelById(self, fuel_id):
        dao = FuelDAO()
        row = dao.getFuelById(fuel_id)
        if not row:
            return jsonify(Error="Power Resource Not Found"), 404
        else:
            fuel = self.build_fuel_dict(row)
            return jsonify(Fuel=fuel)

    def getResourceById(self, resource_id):
        dao = FuelDAO()
        row = dao.getResourceById(resource_id)
        if row:
            result = self.build_fuel_dict(row)
            # jsonify(Food=food)
            return result

    def get_available_resources(self):
        dao = FuelDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list

    def get_resources_supplied(self):
        dao = FuelDAO()
        resources_list = dao.get_resources_supplied()
        result_list = []
        for row in resources_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return result_list

    def get_resources_by_name(self, resource_name):
        dao = FuelDAO()
        fuel_list = []
        fuel_list = dao.get_resources_by_name(resource_name)
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return result_list

    def insertFuelJson(self, json):
        print("json ", json)
        if len(json) != 4:
            return jsonify(Error="Malformed post request"), 400
        fuel_name = json['fuel_name']
        fuel_type = json['fuel_type']
        fuel_liters = json['fuel_liters']
        fuel_date = json['fuel_date']
        if fuel_name and fuel_type and fuel_liters and fuel_date:
            dao = FuelDAO()
            fuel_and_resource_id = dao.insert_fuel(fuel_name, fuel_type, fuel_liters, fuel_date)
            result = self.build_fuel_attributes(fuel_and_resource_id[0], fuel_name, fuel_type, fuel_liters,
                                                fuel_and_resource_id[1], fuel_date)
            return jsonify(Fuel=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateFuel(self, fuel_id, form):
        if not self.getById(fuel_id):
            return jsonify(Error="Fuel not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                fuel_type = form['fuel_type']
                fuel_liters = form['fuel_liters']
                if fuel_type and fuel_liters:
                    self.update_fuel(fuel_id, fuel_type, fuel_liters)
                    result = self.build_fuel_attributes(fuel_id, fuel_type, fuel_liters)
                    return jsonify(Fuel=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteFuel(self, fuel_id):
        if not self.getById(fuel_id):
            return jsonify(Error="Fuel not found."), 404
        else:
            self.delete_fuel(fuel_id)
            return jsonify(DeleteStatus="OK"), 200

    def searchFuels(self, args):
        f_type = args.get("fuel_type")
        fuels_list = []
        if (len(args) == 1) and f_type:
            fuels_list = self.getByType(f_type)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in fuels_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuels=result_list)
