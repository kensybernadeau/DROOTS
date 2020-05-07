from flask import jsonify

from dao.request import requestDAO


class RequestHandler:
    def build_request_dict(self, list):
        result = {}
        result['request_id'] = list[0]
        result['customer_id'] = list[1]
        result['resource_id'] = list[2]
        result['resource_name'] = list[3]
        return result

    def build_request_attributes(self, request_id):
        result = {}
        result['request_id'] = request_id
        return result

    def getAllRequest(self):
        dao = requestDAO()
        request_list = dao.getAllRequest()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def getRequestById(self, request_id):
        dao = requestDAO()
        row = dao.getRequestById(request_id)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            request = self.build_request_dict(row)
            return jsonify(Request=request)

    def searchRequest(self, args):
        resource_name = args.get("resource_name")
        dao = requestDAO()
        request_list = []
        if (len(args) == 1) and resource_name:
            request_list = dao.get_request_by_resource_name(resource_name)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def insertRequestJson(self, form):
        print("form: ", form)
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            request_id = self.insert_request()
            result = self.build_request_attributes(request_id)
            return jsonify(Request=result), 201

    def updateRequest(self, request_id, form):
        if not self.getRequestById(request_id):
            return jsonify(Error="Request not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                self.update_request(request_id)
                result = self.build_request_attributes(request_id)
                return jsonify(Request=result), 200

    def deleteRequest(self, request_id):
        if not self.getRequestById(request_id):
            return jsonify(Error="Request not found."), 404
        else:
            self.delete_request(request_id)
            return jsonify(DeleteStatus="OK"), 200
