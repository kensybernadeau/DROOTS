from flask import jsonify


class RequestHandler:
    request = [(1), (2), (3)]

    # ----------------utils-------------------
    def give_me_request(self):
        return self.request

    def getById(self, request_id):
        for f in self.request:
            if request_id == f:
                return f

    def insert_request(self):
        self.request.append(len(self.request) + 1)
        return len(self.request)

    def update_request(self, request_id):
        self.request.remove(self.getById(request_id))
        self.request.insert(request_id - 1, request_id)

    def delete_request(self, request_id):
        self.request.remove(self.getById(request_id))

    # --------------end utils-----------------

    def build_request_dict(self, list):
        result = {}
        result['request_id'] = list
        return result

    def build_request_attributes(self, request_id):
        result = {}
        result['request_id'] = request_id
        return result

    def getAllRequest(self):
        list = self.give_me_request()
        result_list = []
        for row in list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def getRequestById(self, request_id):
        row = self.getById(request_id)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            batteries = self.build_request_dict(row)
            return jsonify(Request=batteries)

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
