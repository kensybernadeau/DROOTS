from flask import jsonify

from dao.users import UsersDAO


class UserHandler:

    def build_user_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['user_fname'] = row[1]
        result['user_lname'] = row[2]
        result['user_uname'] = row[3]
        result['user_passwd'] = row[4]

        return result

    def build_user_attributes(self, user_id, user_fname, user_lname, user_uname, user_passwd):
        result = {}
        result['user_id'] = user_id
        result['user_fname'] = user_fname
        result['user_lname'] = user_lname
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

