from flask import jsonify

from dao.address import AddressDAO
from dao.supplier import SupplierDAO
from dao.users import UsersDAO


class SupplierHandler:

    def build_supplier_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['user_id'] = row[1]
        result['supplier_fname'] = row[2]
        result['supplier_lname'] = row[3]
        result['supplier_uname'] = row[4]
        result['supplier_passwd'] = row[5]
        result['address_id'] = row[6]
        result['supplier_country'] = row[7]
        result['supplier_city'] = row[8]
        result['supplier_street_address'] = row[9]
        result['supplier_zipcode'] = row[10]

        return result

    def build_supplier_attributes(self, supplier_id, user_id, user_fname, user_lname,
                                  user_uname, user_passwd, address_id, supplier_country, supplier_city,
                                  supplier_street_address, supplier_zipcode):
        result = {}
        result['supplier_id'] = supplier_id
        result['user_id'] = user_id
        result['supplier_fname'] = user_fname
        result['supplier_lname'] = user_lname
        result['supplier_uname'] = user_uname
        result['supplier_passwd'] = user_passwd
        result['address_id'] = address_id
        result['supplier_country'] = supplier_country
        result['supplier_city'] = supplier_city
        result['supplier_street_address'] = supplier_street_address
        result['supplier_zipcode'] = supplier_zipcode
        return result

    def getAllSupplier(self):
        sdao = SupplierDAO()
        result_list = []
        for row in sdao.getAllSuppliers():
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    def getSupplierById(self, supplier_id):
        sdao = SupplierDAO()
        row = sdao.getSupplierById(supplier_id)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier=supplier)

    def insertSupplierJson(self, json):
        print("json: ", json)
        if len(json) != 8:
            return jsonify(Error="Malformed post request"), 400
        else:
            supplier_fname = json['supplier_fname']
            supplier_lname = json['supplier_lname']
            supplier_uname = json['supplier_uname']
            supplier_passwd = json['supplier_passwd']
            supplier_country = json['supplier_country']
            supplier_city = json['supplier_city']
            supplier_street_address = json['supplier_street_address']
            supplier_zipcode = json['supplier_zipcode']
            if supplier_fname and supplier_lname and supplier_uname and supplier_passwd and supplier_country\
                    and supplier_city and supplier_street_address and supplier_zipcode:
                udao = UsersDAO()
                sdao = SupplierDAO()
                addao = AddressDAO()
                user_id = udao.insert(supplier_fname, supplier_lname, supplier_uname, supplier_passwd)
                supplier_id = sdao.insert(user_id)
                address_id = addao.insert(supplier_country, supplier_city, supplier_street_address,
                                          supplier_zipcode, user_id)
                result = self.build_supplier_attributes(supplier_id, user_id, supplier_fname, supplier_lname,
                                                        supplier_uname, supplier_passwd, address_id, supplier_country,
                                                        supplier_city, supplier_street_address, supplier_zipcode)
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateSupplier(self, supplier_id, form):
        if not self.getSupplierById(supplier_id):
            return jsonify(Error="Supplier not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                supplier_location = form['supplier_location']
                if supplier_location:
                    self.update_supplier(supplier_id, supplier_location)
                    result = self.build_supplier_attributes(supplier_id, supplier_location)
                    return jsonify(Supplier=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteSupplier(self, supplier_id):
        if not self.getSupplierById(supplier_id):
            return jsonify(Error="Supplier not found."), 404
        else:
            self.delete_supplier(supplier_id)
            return jsonify(DeleteStatus="OK"), 200
