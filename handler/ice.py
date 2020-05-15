from flask import jsonify

from dao.ice import IceDAO


class IceHandler:

    def build_ice_dict(self, row):
        result = {}
        result['ice_id'] = row[0]
        result['ice_name'] = row[1]
        result['ice_description'] = row[2]
        result['resource_id'] = row[3]
        return result

    def build_ice_attributes(self, ice_id, ice_name, ice_description, resource_id, resource_date):
        result = {}
        result['ice_id'] = ice_id
        result['ice_name'] = ice_name
        result['ice_description'] = ice_description
        result['resource_id'] = resource_id
        result['resource_date'] = resource_date
        return result

    def getAllIce(self):
        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def getIceById(self, ice_id):
        dao = IceDAO()
        row = dao.getIceById(ice_id)
        if not row:
            return jsonify(Error="Ice Not Found"), 404
        else:
            ice = self.build_ice_dict(row)
            return jsonify(Ice=ice)

    def getResourceById(self, resource_id):
        dao = IceDAO()
        row = dao.getResourceById(resource_id)
        if row:
            result = self.build_ice_dict(row)
            # jsonify(Food=food)
            return result

    def get_available_resources(self):
        dao = IceDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_ice_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list

    def get_resources_supplied(self):
        dao = IceDAO()
        resources_list = dao.get_resources_supplied()
        result_list = []
        for row in resources_list:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return result_list

    def get_resources_by_name(self, resource_name):
        dao = IceDAO()
        ice_list = []
        ice_list = dao.get_resources_by_name(resource_name)
        result_list = []
        for row in ice_list:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return result_list

    def insertIceJson(self, json):
        print("json ", json)
        if len(json) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            ice_name = json['ice_name']
            ice_description = json['ice_description']
            ice_date = json['ice_date']
            if ice_name and ice_description and ice_date:
                dao = IceDAO()
                ice_and_resource_id = dao.insert_ice(ice_name, ice_description, ice_date)
                result = self.build_ice_attributes(ice_and_resource_id[0], ice_name, ice_description,
                                                   ice_and_resource_id[1], ice_date)
                return jsonify(Ice=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
