from flask import jsonify

from dao.address import AddressDAO
from dao.administrators import AdministratorsDAO
from dao.email import EmailDAO
from dao.phone import PhoneDAO
from dao.users import UsersDAO


class AdministratorsHandler:

    def build_administrator_dict(self, row):
        result = {}
        result['administrator_id'] = row[0]
        result['user_id'] = row[1]
        result['administrator_fname'] = row[2]
        result['administrator_lname'] = row[3]
        result['administrator_uname'] = row[4]
        result['administrator_passwd'] = row[5]
        result['administrator_country'] = row[6]
        result['administrator_city'] = row[7]
        result['administrator_street_address'] = row[8]
        result['administrator_zipcode'] = row[9]
        result['administrator_phone'] = row[10]
        result['administrator_email'] = row[11]
        return result

    def build_administrator_attributes(self, administrator_id, user_id, administrator_fname, administrator_lname,
                                       user_uname, user_passwd, address_id, administrator_country, administrator_city,
                                       administrator_street_address, administrator_zipcode):
        result = {}
        result['administrator_id'] = administrator_id
        result['user_id'] = user_id
        result['administrator_fname'] = administrator_fname
        result['administrator_lname'] = administrator_lname
        result['administrator_uname'] = user_uname
        result['administrator_passwd'] = user_passwd
        result['address_id'] = address_id
        result['administrator_country'] = administrator_country
        result['administrator_city'] = administrator_city
        result['administrator_street_address'] = administrator_street_address
        result['administrator_zipcode'] = administrator_zipcode
        return result

    def getAllAdministrators(self):
        adao = AdministratorsDAO()
        result_list = []
        for row in adao.getAllAdmins():
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators=result_list)

    def getAdministratorById(self, administrator_id):
        adao = AdministratorsDAO()
        row = adao.getAdminById(administrator_id)
        if not row:
            return jsonify(Error="Administrator Not Found"), 404
        else:
            admin = self.build_administrator_dict(row)
            return jsonify(Administrator=admin)

    def insertAdministratorJson(self, json):
        print("json ", json)
        if len(json) != 10:
            return jsonify(Error="Malformed post request"), 400
        else:
            administrator_fname = json['administrator_fname']
            administrator_lname = json['administrator_lname']
            administrator_uname = json['administrator_uname']
            administrator_passwd = json['administrator_passwd']
            administrator_country = json['administrator_country']
            administrator_city = json['administrator_city']
            administrator_street_address = json['administrator_street_address']
            administrator_zipcode = json['administrator_zipcode']
            administrator_phone = json['administrator_phone']
            administrator_email = json['administrator_email']
            if administrator_fname and administrator_lname and administrator_uname and \
                    administrator_passwd and administrator_country and administrator_city and \
                    administrator_street_address and administrator_zipcode and administrator_phone and \
                    administrator_email:
                udao = UsersDAO()
                adao = AdministratorsDAO()
                addao = AddressDAO()
                email_dao = EmailDAO()
                phone_dao = PhoneDAO()
                user_id = udao.insert(administrator_fname, administrator_lname,
                                      administrator_uname, administrator_passwd)
                admin_id = adao.insert(user_id)
                address_id = addao.insert(administrator_country, administrator_city,
                                          administrator_street_address, administrator_zipcode, user_id)
                email_dao.insert(administrator_email, user_id)
                phone_dao.insert(administrator_phone, user_id)
                result = self.build_administrator_attributes(admin_id, user_id, administrator_fname,
                                                             administrator_lname,
                                                             administrator_uname,
                                                             administrator_passwd, address_id, administrator_country,
                                                             administrator_city, administrator_street_address,
                                                             administrator_zipcode)
                return jsonify(Administrator=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    # def updateAdministrator(self, administrator_id, form):
    # if not self.getById(administrator_id):
    # return jsonify(Error="Administrator not found."), 404
    # else:
    # if len(form) != 2:
    # return jsonify(Error="Malformed update request"), 400
    # else:
    # administrator_fname = form['administrator_fname']
    # administrator_lname = form['administrator_lname']
    # if administrator_fname and administrator_lname:
    # self.update_administrator(administrator_id, administrator_fname, administrator_lname)
    # result = self.build_administrator_attributes(administrator_id, administrator_fname,
    # administrator_lname)
    # return jsonify(Administrator=result), 200
    # else:
    # return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteAdministrator(self, admin_id):
        udao = UsersDAO()
        adao = AdministratorsDAO()
        admin = adao.getAdminById(admin_id)
        if not admin:
            return jsonify(Error="Administrator not found."), 404
        else:
            user_id = adao.delete(admin_id)
            udao.delete(user_id)
            return jsonify(DeleteStatus="OK"), 200
