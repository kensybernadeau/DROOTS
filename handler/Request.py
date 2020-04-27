from flask import jsonify

from dao.request import RequestDAO


class RequestHandler:

    def build_request_dict(self, row):
        result = {}
        result['request_id'] = row[0]
        result['costumer_id'] = row[1]
        result['resource_id'] = row[2]
        return result

    def build_request_attributes(self, request_id, costumer_id, resource_id):
        result = {}
        result['request_id'] = request_id
        result['costumer_id'] = costumer_id
        result['resource_id'] = resource_id
        return result

    def getAllRequests(self):
        rdao = RequestDAO()
        result_list = []
        for row in rdao.getAllRequest():
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def getRequestById(self, request_id):
        rdao = RequestDAO()
        row = rdao.getRequestById(request_id)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            result = self.build_request_dict(row)
            return jsonify(Request=result)

    def insertRequestJson(self, json):
        print("form: ", json)
        if len(json) != 1:
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
