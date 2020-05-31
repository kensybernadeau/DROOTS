from flask import jsonify

from dao.card import cardDAO
from dao.payment import paymentDAO


class cardHandler:


    def build_card_dict(self, list):
        result = {}
        result['payment_id'] = list[0]
        result['payment_date'] = list[1]
        result['payment_amount'] = list[2]
        result['customer_id'] = list[3]
        result['supplier_id'] = list[4]
        result['resource_id'] = list[5]
        result['resource_name'] = list[6]
        result['card_id'] = list[7]
        result['card_type'] = list[8]
        result['card_number'] = list[9]
        result['card_security_code'] = list[10]
        return result

    def build_card_attributes(self, payment_id, payment_date, payment_amount, card_id, card_type, card_number, card_security_code, customer_id, resource_id, supplier_id ):
        result = {}
        result['payment_id'] = payment_id
        result['payment_date'] = payment_date
        result['payment_amount'] = payment_amount
        result['customer_id'] = customer_id
        result['supplier_id'] = supplier_id
        result['resource_id'] = resource_id
        result['card_id'] = card_id
        result['card_type'] = card_type
        result['card_number'] = card_number
        result['card_security_code'] = card_security_code
        return result


    def getAllPayment(self):
        dao = cardDAO()
        card_list = dao.getAllCard()
        result_list = []
        for row in card_list:
            result = self.build_card_dict(row)
            result_list.append(result)
        return result_list
        # return jsonify(Card=result_list)


    def getAllById(self, card_id):
        dao = cardDAO()
        row = dao.getCardById(card_id)
        if row:
            result = self.build_card_dict(row)
            return result

    def insertCardJson(self, form):
        print("form: ", form)
        if len(form) != 8:
            return jsonify(Error="Malformed post request"), 400
        else:
            card_type = form['card_type']
            card_number = form['card_number']
            card_security_code = form['card_security_code']
            payment_date = form['payment_date']
            payment_amount = form['payment_amount']
            resource_id = form['resource_id']
            supplier_id = form['supplier_id']
            customer_id = form['customer_id']

            if card_type and card_number and card_security_code and payment_date and payment_amount and resource_id and supplier_id and customer_id:
                dao = cardDAO()
                card_and_payment_id = dao.insertCard(card_type, card_number, card_security_code, payment_date, payment_amount, resource_id, supplier_id, customer_id)
                result = self.build_card_attributes(card_and_payment_id[1], payment_date, payment_amount, card_and_payment_id[0], card_type, card_number, card_security_code, customer_id, resource_id, supplier_id)
                return jsonify(Payment=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
