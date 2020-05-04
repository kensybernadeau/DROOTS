from flask import jsonify

from dao.athmovil import athmovilDAO


class athmovilHandler:


    def build_athmovil_dict(self, list):
        result = {}
        result['payment_id'] = list[0]
        result['payment_method'] = list[1]

        return result

    def build_athmovil_attributes(self, payment_id, payment_method):
        result = {}
        result['payment_id'] = payment_id
        result['payment_method'] = payment_method

        return result

    def getAllAthmovil(self):
        dao = athmovilDAO()
        athmovil_list = dao.getAllAthmovil()
        result_list = []
        for row in athmovil_list:
            result = self.build_athmovil_dict(row)
            result_list.append(result)
        return jsonify(Athmovil=result_list)

    def getAthmovilById(self, athmovil_id):
        dao = athmovilDAO()
        row = dao.getAthmovilById(athmovil_id)
        if not row:
            return jsonify(Error="Athmovil Not Found"), 404
        else:
            athmovil = self.build_athmovil_dict(row)
            return jsonify(Athmovil=athmovil)

    # def insertPaymentJson(self, form):
    #     print("form: ", form)
    #     if len(form) != 1:
    #         return jsonify(Error="Malformed post request"), 400
    #     else:
    #         payment_method = form['payment_method']
    #         if payment_method:
    #             payment_id = self.insert_payment(payment_method)
    #             result = self.build_payment_attributes(payment_id, payment_method)
    #             return jsonify(Payment=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def updatePayment(self, payment_id, payment_method, form):
    #     if not self.getPaymentById(payment_id):
    #         return jsonify(Error="Payment not found."), 404
    #     else:
    #         if len(form) != 1:
    #             return jsonify(Error="Malformed update request"), 400
    #         else:
    #             self.update_payment(payment_id, payment_method)
    #             result = self.build_payment_attributes(payment_id,payment_method)
    #             return jsonify(Payment=result), 200
    #
    # def deletePayment(self, payment_id):
    #     if not self.getPaymentById(payment_id):
    #         return jsonify(Error="Payment not found."), 404
    #     else:
    #         self.delete_payment(payment_id)
    #         return jsonify(DeleteStatus="OK"), 200