from flask import jsonify

from dao.ice import IceDAO


class IceHandler:


    def build_ice_dict(self, row):
        result = {}
        result['ice_id'] = row[0]
        result['ice_name'] = row[1]
        result['ice_description'] = row[2]
        return result

    def build_ice_attributes(self, ice_id, ice_name, ice_oz, ice_description):
        result = {}
        result['ice_id'] = ice_id
        result['ice_name'] = ice_name
        result['ice_description'] = ice_description
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

    def get_available_resources(self):
        dao = IceDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_ice_dict(row)
            result_list.append(result)
        # return jsonify(Resource=result_list)
        return result_list