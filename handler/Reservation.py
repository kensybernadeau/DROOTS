from flask import jsonify

from dao.reservation import reservationDAO


class ReservationHandler:

    def build_reservation_dict(self, list):
        result = {}
        result['reservation_id'] = list[0]
        result['customer_id'] = list[1]
        result['supplier_id'] = list[2]
        result['resource_id'] = list[3]
        result['resource_name'] = list[4]
        result['reservation_date'] = list[5]
        return result

    def build_reservation_attributes(self, reservation_id, customer_id, reservation_date, resource_id, supplier_id):
        result = {}
        result['reservation_id'] = reservation_id
        result['customer_id'] = customer_id
        result['reservation_date'] = reservation_date
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        return result

    def getAllReservation(self):
        dao = reservationDAO()
        reservation_list = dao.getAllReservation()
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getReservationById(self, reservation_id):
        dao = reservationDAO()
        row = dao.getReservationById(reservation_id)
        if not row:
            return jsonify(Error="Reservation Not Found"), 404
        else:
            reservation = self.build_reservation_dict(row)
            return jsonify(Reservation=reservation)

    def insertReservationJson(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            customer_id = form['customer_id']
            reservation_date = form['reservation_date']
            resource_id = form['resource_id']
            supplier_id = form['supplier_id']
            if customer_id and reservation_date and resource_id and supplier_id:
                dao = reservationDAO()
                reservation_id = dao.insertReservation(customer_id, reservation_date, resource_id, supplier_id)
                result = self.build_reservation_attributes(reservation_id, customer_id, reservation_date, resource_id, supplier_id)
                return jsonify(Reservation=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def updateReservation(self, reservation_id, form):
        if not self.getReservationById(reservation_id):
            return jsonify(Error="Reservation not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                self.update_reservation(reservation_id)
                result = self.build_reservation_attributes(reservation_id)
                return jsonify(Reservation=result), 200

    def deleteReservation(self, reservation_id):
        if not self.getReservationById(reservation_id):
            return jsonify(Error="Reservation not found."), 404
        else:
            self.delete_reservation(reservation_id)
            return jsonify(DeleteStatus="OK"), 200
