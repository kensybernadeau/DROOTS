from flask import jsonify


class PaymentHandler:
    payment = [(1,'visa'), (2,'efectivo'), (3,'efectivo')]

    # ----------------utils-------------------
    def give_me_payment(self):
        return self.payment

    def getById(self, payment_id):
        for f in self.payment:
            if payment_id == f[0]:
                return f

    def insert_payment(self, payment_method):
        self.payment.append((len(self.payment) + 1, payment_method))
        return len(self.payment)

    def update_payment(self, payment_id, payment_method):
        self.payment.remove(self.getById(payment_id))
        self.payment.insert(payment_id - 1, payment_method)

    def delete_payment(self, payment_id):
        self.payment.remove(self.getById(payment_id))

    # --------------end utils-----------------

    def build_payment_dict(self, list):
        result = {}
        result['payment_id'] = list[0]
        result['payment_method'] = list[1]

        return result

    def build_payment_attributes(self, payment_id, payment_method):
        result = {}
        result['payment_id'] = payment_id
        result['payment_method'] = payment_method

        return result

    def getAllPayment(self):
        list = self.give_me_payment()
        result_list = []
        for row in list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Payment=result_list)

    def getPaymentById(self, payment_id):
        row = self.getById(payment_id)
        if not row:
            return jsonify(Error="Payment Not Found"), 404
        else:
            payment = self.build_payment_dict(row)
            return jsonify(Payment=payment)

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

    def updatePayment(self, payment_id, payment_method, form):
        if not self.getPaymentById(payment_id):
            return jsonify(Error="Payment not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                self.update_payment(payment_id, payment_method)
                result = self.build_payment_attributes(payment_id,payment_method)
                return jsonify(Payment=result), 200

    def deletePayment(self, payment_id):
        if not self.getPaymentById(payment_id):
            return jsonify(Error="Payment not found."), 404
        else:
            self.delete_payment(payment_id)
            return jsonify(DeleteStatus="OK"), 200
