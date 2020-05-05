from flask import jsonify

from dao.card import cardDAO


class cardHandler:


    def build_card_dict(self, list):
        result = {}
        result['payment_id'] = list[0]
        result['payment_date'] = list[1]
        result['payment_amount'] = list[2]
        result['supplier_id'] = list[3]
        result['resource_id'] = list[4]
        result['resource_name'] = list[5]
        result['card_id'] = list[6]
        result['card_type'] = list[7]
        result['card_number'] = list[8]
        result['card_security_code'] = list[9]
        # select payment_id, payment_date, payment_amount, supplier_id, resource_id, resource_name, card_id, card_type, card_number, card_security_code
        return result

    def build_card_attributes(self, payment_id, payment_method):
        result = {}
        result['payment_id'] = payment_id
        result['payment_method'] = payment_method

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


    def getCardById(self, card_id):
        dao = cardDAO()
        row = dao.getCardById(card_id)
        if not row:
            return jsonify(Error="Card Not Found"), 404
        else:
            card = self.build_card_dict(row)
            return jsonify(Card=card)


