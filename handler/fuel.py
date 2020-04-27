from flask import jsonify

from dao.fuel import FuelDAO


class FuelHandler:

    def build_fuel_dict(self, row):
        result = {}
        result['fuel_id'] = row[0]
        result['fuel_type'] = row[1]
        result['fuel_liters'] = row[2]

        return result

    def build_fuel_attributes(self, fuel_id, fuel_type, fuel_liters):
        result = {}
        result['fuel_id'] = fuel_id
        result['fuel_type'] = fuel_type
        result['fuel_liters'] = fuel_liters
        return result

    def getAllFuels(self):
        fdao = FuelDAO()
        result_list = []
        for row in fdao.getAllFuels():
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuels=result_list)

    def getFuelById(self, fuel_id):
        fdao = FuelDAO()
        row = fdao.getFuelById(fuel_id)
        if not row:
            return jsonify(Error="Fuel Not Found"), 404
        else:
            fuel = self.build_fuel_dict(row)
            return jsonify(Fuel=fuel)

    def insertFuelJson(self, json):
        print("json ", json)
        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400
        fuel_type = json['fuel_type']
        fuel_liters = json['fuel_liters']

        if fuel_type and fuel_liters:
            fuel_id = self.insert_fuel(fuel_type, fuel_liters)
            result = self.build_fuel_attributes(fuel_id, fuel_type, fuel_liters)
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
            fdao = FuelDAO()
            fuels_list = fdao.getFuelByType(f_type)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in fuels_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuels=result_list)
