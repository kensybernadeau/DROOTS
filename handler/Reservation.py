from flask import jsonify


class ReservationHandler:

    reservation = [('1'), ('2'), ('3')]

    #----------------utils-------------------
    def give_me_reservation(self):
        return self.reservation

    def getById(self, request_id):
        for f in self.reservation:
            if request_id == f:
                return f

    def insert_reservation(self):
        self.reservation.append(len(self.reservation) + 1)
        return len(self.reservation)
# ME QUEDE AQUI
#
#

    def update_reservation(self, reservation_id):
        self.reservation.pop(reservation_id - 1)
        self.reservation.insert(reservation_id - 1)

    def delete_reservation(self, reservation_id):
        self.reservation.pop(reservation_id - 1)
    #--------------end utils-----------------

    def build_reservation_dict(self, list):
        result = {}
        result['reservation_id'] = list
        return result

    def build_reservation_attributes(self, reservation_id):
        result = {}
        result['reservation_id'] = reservation_id
        return result

    def getAllReservation(self):
        # dao = SupplierDAO()
        # suppliers_list = dao.getAllSuppliers()
        list = self.give_me_reservation()
        result_list = []
        for row in list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getReservationById(self, reservation_id):
        # dao = PartsDAO()
        # row = dao.getPartById(pid)
        row = self.getById(reservation_id)
        if not row:
            return jsonify(Error="Reservation Not Found"), 404
        else:
            reservation = self.build_reservation_dict(row)
            return jsonify(Reservation=reservation)

    def insertReservationJson(self, form):
        print("form: ", form)
        if len(form) != 0:
            return jsonify(Error="Malformed post request"), 400
        else:
                # dao = PartsDAO()
                # pid = dao.insert(pname, pcolor, pmaterial, pprice)
                reservation_id = self.insert_reservation()
                result = self.build_reservation_dict(reservation_id)
                return jsonify(Reservation=result), 201


    def updateReservation(self, reservation_id, form):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getReservationById(reservation_id):
            return jsonify(Error = "Request not found."), 404
        else:
            if len(form) != 0:
                return jsonify(Error="Malformed update request"), 400
            else:
                    # dao.update(pid, pname, pcolor, pmaterial, pprice)
                    self.update_reservation(reservation_id)
                    result = self.build_reservation_attributes(reservation_id)
                    return jsonify(Reservation=result), 200

    def deleteReservation(self, reservation_id):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getReservationById(reservation_id):
            return jsonify(Error="Reservation not found."), 404
        else:
            # dao.delete(pid)
            self.delete_reservation(reservation_id)
            return jsonify(DeleteStatus="OK"), 200