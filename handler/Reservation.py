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
        return result

    def build_reservation_attributes(self, reservation_id):
        result = {}
        result['reservation_id'] = reservation_id
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
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            reservation_id = self.insert_reservation()
            result = self.build_reservation_dict(reservation_id)
            return jsonify(Reservation=result), 201

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
