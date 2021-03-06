from flask import jsonify


class FuelHandler:
    fuels = [(1, "diesel", 20), (2, "gas", 40), (3, "biodiesel", 10),(4, "diesel", 50),(5, "diesel", 100),(6, "diesel", 40)]

    # ----------------utils-------------------
    def give_me_fuels(self):
        return self.fuels

    def getById(self, fuel_id):
        for f in self.fuels:
            if fuel_id == f[0]:
                return f

    def getByType(self, f_type):
        result = []
        for row in self.fuels:
            if row[1] == f_type:
                result.append(row)
        return result

    def insert_fuel(self, fuel_type, fuel_liters):
        self.fuels.append((len(self.fuels) + 1, fuel_type, fuel_liters))
        return len(self.fuels)

    def update_fuel(self, fuel_id, fuel_type, fuel_liters):
        self.fuels.remove(self.getById(fuel_id))
        self.fuels.insert(fuel_id - 1, (fuel_id, fuel_type, fuel_liters))

    def delete_fuel(self, fuel_id):
        result = self.getById(fuel_id)
        self.fuels.remove(result)

        # --------------end utils-----------------

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
        flist = self.give_me_fuels()
        result_list = []
        for row in flist:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuels=result_list)

    def getFuelById(self, fuel_id):
        row = self.getById(fuel_id)
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
            fuels_list = self.getByType(f_type)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in fuels_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuels=result_list)
