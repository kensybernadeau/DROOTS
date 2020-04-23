from flask import jsonify

from dao.users import UsersDAO


class UserHandler:

    def build_user_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['user_fname'] = row[1]
        result['user_lname'] = row[2]
        result['user_location'] = row[3]
        result['user_uname'] = row[4]
        result['user_passwd'] = row[5]

        return result

    def build_user_attributes(self, user_id, user_fname, user_lname, user_location, user_uname, user_passwd):
        result = {}
        result['user_id'] = user_id
        result['user_fname'] = user_fname
        result['user_lname'] = user_lname
        result['user_location'] = user_location
        result['user_uname'] = user_uname
        result['user_passwd'] = user_passwd
        return result

    def getAllUsers(self):
        udao = UsersDAO()
        result_list = []
        for row in udao.getAllUsers():
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserById(self, user_id):
        udao = UsersDAO()
        row = udao.getUserById(user_id)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

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

    #def deleteUser(self, user_id):
        #udao = UsersDAO()
        #udelete = udao.delete(user_id)
        #if not udelete:
            #return jsonify(Error="User not found."), 404
        #else:
            #return jsonify(DeleteStatus="OK"), 200
