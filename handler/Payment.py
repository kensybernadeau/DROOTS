from flask import jsonify

from dao.payment import paymentDAO
from handler.athmovil import athmovilHandler
from handler.card import cardHandler


class PaymentHandler:

    def build_payment_dict(self, list):
        result = {}
        result['payment_id'] = list[0]
        result['customer_id'] = list[1]
        result['payment_date'] = list[2]
        result['payment_amount'] = list[3]
        result['resource_id'] = list[4]
        result['supplier_id'] = list[5]
        return result

    def build_payment_attributes(self, payment_id, payment_method):
        result = {}
        result['payment_id'] = payment_id
        result['payment_method'] = payment_method

        return result

    def getAllPaymentMethods(self):
        handler_list = [athmovilHandler(), cardHandler()]
        payment_list = []
        for handler in handler_list:
            payment_list.extend(handler.getAllPayment())
        return jsonify(Payments=payment_list)

    def getAllPaymentById(self, payment_id):
        handler_list = [athmovilHandler(), cardHandler()]
        for handler in handler_list:
            row = handler.getAllById(payment_id)
            if row:
                return jsonify(Resource=row)
        return jsonify(Error="Payment Not Found"), 404

    def insertPaymentJson(self, form):
        print("form: ", form)
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            payment_method = form['payment_method']
            if payment_method:
                payment_id = self.insert_payment(payment_method)
                result = self.build_payment_attributes(payment_id, payment_method)
                return jsonify(Payment=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400