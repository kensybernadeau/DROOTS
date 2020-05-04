from flask import jsonify

from dao.card import cardDAO


class cardlHandler:


    def build_card_dict(self, list):
        result = {}
        result['payment_id'] = list[0]
        result['payment_method'] = list[1]

        return result

    def build_card_attributes(self, payment_id, payment_method):
        result = {}
        result['payment_id'] = payment_id
        result['payment_method'] = payment_method

        return result


    def getAllCard(self):
        dao = cardDAO()
        card_list = dao.getAllCard()
        result_list = []
        for row in card_list:
            result = self.build_card_dict(row)
            result_list.append(result)
        return jsonify(Card=result_list)


    def getCardById(self, card_id):
        dao = cardDAO()
        row = dao.getCardById(card_id)
        if not row:
            return jsonify(Error="Card Not Found"), 404
        else:
            card = self.build_card_dict(row)
            return jsonify(Card=card)


