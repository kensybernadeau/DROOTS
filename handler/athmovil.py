from flask import jsonify

from dao.athmovil import athmovilDAO


class athmovilHandler:


    def build_athmovil_dict(self, list):
        result = {}
        result['payment_id'] = list[0]
        result['payment_date'] = list[1]
        result['payment_amount'] = list[2]
        result['customer_id'] = list[3]
        result['supplier_id'] = list[4]
        result['resource_id'] = list[5]
        result['resource_name'] = list[6]
        result['athmovil_id'] = list[7]
        result['athmovil_transaction_num'] = list[8]
        result['athmovil_phone_number'] = list[9]
        return result
    # athmovil(athmovil_transaction_num, athmovil_phone_number, payment_id


    def build_athmovil_attributes(self, payment_id, payment_date, payment_amount, customer_id, supplier_id, resource_id,
                              athmovil_id, athmovil_transaction_num, athmovil_phone_number):
        result = {}
        result['payment_id'] = payment_id
        result['payment_date'] = payment_date
        result['payment_amount'] = payment_amount
        result['customer_id'] = customer_id
        result['supplier_id'] = supplier_id
        result['resource_id'] = resource_id
        result['athmovil_id'] = athmovil_id
        result['athmovil_transaction_num'] = athmovil_transaction_num
        result['athmovil_phone_number'] = athmovil_phone_number
        return result

    def getAllPayment(self):
        dao = athmovilDAO()
        athmovil_list = dao.getAllAthmovil()
        result_list = []
        for row in athmovil_list:
            result = self.build_athmovil_dict(row)
            result_list.append(result)
        return result_list
        # return jsonify(Athmovil=result_list)

    def getAllById(self, athmovil_id):
        dao = athmovilDAO()
        row = dao.getAthmovilById(athmovil_id)
        if row:
            result = self.build_athmovil_dict(row)
            return result

    def insertAthmovilJson(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error="Malformed post request"), 400
        else:
            athmovil_transaction_num = form['athmovil_transaction_num']
            athmovil_phone_number = form['athmovil_phone_number']
            payment_date = form['payment_date']
            payment_amount = form['payment_amount']
            resource_id = form['resource_id']
            supplier_id = form['supplier_id']
            customer_id = form['customer_id']
            if athmovil_transaction_num and athmovil_phone_number and payment_date and payment_amount and resource_id and supplier_id and customer_id:
                dao = athmovilDAO()
                athmovil_and_payment_id = dao.insertAthmovil(athmovil_transaction_num, athmovil_phone_number, payment_date, payment_amount, customer_id, resource_id, supplier_id)
                result = self.build_athmovil_attributes(athmovil_and_payment_id[1], payment_date, payment_amount, customer_id, supplier_id, resource_id, athmovil_and_payment_id[0], athmovil_transaction_num, athmovil_phone_number)
                return jsonify(Payment=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    # athmovil(athmovil_transaction_num, athmovil_phone_number, payment_id

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
