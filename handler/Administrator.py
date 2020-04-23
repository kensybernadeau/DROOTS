from flask import jsonify

from dao.administrators import AdministratorsDAO
from dao.users import UsersDAO


class AdministratorsHandler:

    def build_administrator_dict(self, row):
        result = {}
        result['administrator_id'] = row[0]
        result['user_id'] = row[1]

        return result

    def build_administrator_attributes(self, administrator_id, user_id, user_fname, user_lname, user_location,
                                       user_uname, user_passwd):
        result = {}
        result['administrator_id'] = administrator_id
        result['user_id'] = user_id
        result['user_fname'] = user_fname
        result['user_lname'] = user_lname
        result['user_location'] = user_location
        result['user_uname'] = user_uname
        result['user_passwd'] = user_passwd
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
        if len(json) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            administrator_fname = json['administrator_fname']
            administrator_lname = json['administrator_lname']
            administrator_location = json['administrator_location']
            administrator_uname = json['administrator_uname']
            administrator_passwd = json['administrator_passwd']
            if administrator_fname and administrator_lname and administrator_location and administrator_uname and administrator_passwd:
                udao = UsersDAO()
                adao = AdministratorsDAO()
                user_id = udao.insert(administrator_fname, administrator_lname, administrator_location,
                                      administrator_uname, administrator_passwd)
                admin_id = adao.insert(user_id)
                result = self.build_administrator_attributes(admin_id, user_id, administrator_fname,
                                                             administrator_lname, administrator_location,
                                                             administrator_uname,
                                                             administrator_passwd)
                return jsonify(Administrator=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    #def updateAdministrator(self, administrator_id, form):
        #if not self.getById(administrator_id):
            #return jsonify(Error="Administrator not found."), 404
        #else:
            #if len(form) != 2:
                #return jsonify(Error="Malformed update request"), 400
            #else:
                #administrator_fname = form['administrator_fname']
                #administrator_lname = form['administrator_lname']
                #if administrator_fname and administrator_lname:
                    #self.update_administrator(administrator_id, administrator_fname, administrator_lname)
                    #result = self.build_administrator_attributes(administrator_id, administrator_fname,
                                                                 #administrator_lname)
                    #return jsonify(Administrator=result), 200
                #else:
                    #return jsonify(Error="Unexpected attributes in update request"), 400

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
