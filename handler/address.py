from flask import jsonify

from dao.address import AddressDAO
from dao.users import UsersDAO


class AddressHandler:

    def build_address_dict(self, row):
        result = {}
        result['address_id'] = row[0]
        result['user_country'] = row[1]
        result['user_city'] = row[2]
        result['user_street_address'] = row[3]
        result['user_zipcode'] = row[4]

        return result

    def build_address_attributes(self, address_id, user_country, user_city, user_street_address, user_zipcode):
        result = {}
        result['address_id'] = address_id
        result['user_country'] = user_country
        result['user_city'] = user_city
        result['user_street_address'] = user_street_address
        result['user_zipcode'] = user_zipcode
        return result

    def getAllAddress(self):
        addao = AddressDAO()
        result_list = []
        for row in addao.getAllAddress():
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Address=result_list)

    def getAddressById(self, address_id):
        addao = AddressDAO()
        row = addao.getAddressById(address_id)
        if not row:
            return jsonify(Error="Address Not Found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address=address)

    #def insertUserJson(self, json):
        #print("json ", json)
        #if len(json) != 5:
            #return jsonify(Error="Malformed post request"), 400
        #else:
            #user_fname = json['user_fname']
            #user_lname = json['user_lname']
            #user_location = json['user_location']
            #user_uname = json['user_uname']
            #user_passwd = json['user_passwd']
            #if user_fname and user_lname and user_location and user_uname and user_passwd:
                #udao = UsersDAO()
                #user_id = udao.insert(user_fname, user_lname, user_location, user_uname, user_passwd)
                #result = self.build_user_attributes(user_id, user_fname, user_lname, user_location, user_uname,
                                                    #user_passwd)
                #return jsonify(User=result), 201
            #else:
                #return jsonify(Error="Unexpected attributes in post request"), 400
        """
    def updateUser(self, user_id, form):
        udao = UsersDAO()
        if not udao.getUserById(user_id):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                user_fname = form['user_fname']
                user_lname = form['user_lname']
                user_location = form['user_location']
                user_uname = form['user_uname']
                user_passwd = form['user_passwd']
                if user_fname and user_lname and user_location and user_uname and user_passwd:
                    udao.update(user_id, user_fname, user_lname, user_location, user_uname, user_passwd)
                    result = self.build_user_attributes(user_id, user_fname, user_lname, user_location, user_uname,
                                                        user_passwd)
                    return jsonify(User=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
        """
    #def deleteUser(self, user_id):
        #udao = UsersDAO()
        #udelete = udao.delete(user_id)
        #if not udelete:
            #return jsonify(Error="User not found."), 404
        #else:
            #return jsonify(DeleteStatus="OK"), 200
