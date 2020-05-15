from flask import jsonify

from dao.address import AddressDAO
from dao.customers import CustomerDAO
from dao.email import EmailDAO
from dao.phone import PhoneDAO
from dao.users import UsersDAO


class CustomerHandler:

    def build_customer_dict(self, row):
        result = {}
        result['customer_id'] = row[0]
        result['user_id'] = row[1]
        result['customer_fname'] = row[2]
        result['customer_lname'] = row[3]
        result['customer_uname'] = row[4]
        result['customer_passwd'] = row[5]
        result['customer_country'] = row[6]
        result['customer_city'] = row[7]
        result['customer_street_address'] = row[8]
        result['customer_zipcode'] = row[9]
        result['customer_phone'] = row[10]
        result['customer_email'] = row[11]

        return result

    def build_customer_attributes(self, customer_id, user_id, user_fname, user_lname,
                                  user_uname, user_passwd, customer_country, customer_city,
                                  customer_street_address, customer_zipcode, customer_phone, customer_email):
        result = {}
        result['customer_id'] = customer_id
        result['user_id'] = user_id
        result['customer_fname'] = user_fname
        result['customer_lname'] = user_lname
        result['customer_uname'] = user_uname
        result['customer_passwd'] = user_passwd
        result['customer_country'] = customer_country
        result['customer_city'] = customer_city
        result['customer_street_address'] = customer_street_address
        result['customer_zipcode'] = customer_zipcode
        result['customer_phone'] = customer_phone
        result['customer_email'] = customer_email
        return result

    def getAllCustomers(self):
        cdao = CustomerDAO()
        result_list = []
        for row in cdao.getAllCustomers():
            result = self.build_customer_dict(row)
            result_list.append(result)
        return jsonify(Customers=result_list)

    def getCustomersById(self, customer_id):
        cdao = CustomerDAO()
        row = cdao.getCustomerById(customer_id)
        if not row:
            return jsonify(Error="Customer Not Found"), 404
        else:
            customer = self.build_customer_dict(row)
            return jsonify(Customer=customer)

    def insertCustomersJson(self, json):
        print("json: ", json)
        if len(json) != 10:
            return jsonify(Error="Malformed post request"), 400
        else:
            customer_fname = json['customer_fname']
            customer_lname = json['customer_lname']
            customer_uname = json['customer_uname']
            customer_passwd = json['customer_passwd']
            customer_country = json['customer_country']
            customer_city = json['customer_city']
            customer_street_address = json['customer_street_address']
            customer_zipcode = json['customer_zipcode']
            customer_phone = json['customer_phone']
            customer_email = json['customer_email']
            if customer_fname and customer_lname and customer_uname and customer_passwd and customer_country \
                    and customer_city and customer_street_address and customer_zipcode and customer_phone \
                    and customer_email:
                udao = UsersDAO()
                cdao = CustomerDAO()
                addao = AddressDAO()
                pdao = PhoneDAO()
                edao = EmailDAO()
                user_id = udao.insert(customer_fname, customer_lname,
                                      customer_uname, customer_passwd)
                customer_id = cdao.insert(user_id)
                addao.insert(customer_country, customer_city, customer_street_address,
                             customer_zipcode, user_id)
                pdao.insert(customer_phone, user_id)
                edao.insert(customer_email, user_id)
                result = self.build_customer_attributes(customer_id, user_id, customer_fname,
                                                        customer_lname,
                                                        customer_uname,
                                                        customer_passwd, customer_country, customer_city,
                                                        customer_street_address, customer_zipcode, customer_phone,
                                                        customer_email)
                return jsonify(Customer=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateCustomers(self, customers_id, form):
        if not self.getCustomersById(customers_id):
            return jsonify(Error="Customer not found."), 404
        else:
            if form:
                return jsonify(Error="Malformed update request"), 400
            else:
                self.update_customers(customers_id)
                result = self.build_customers_attributes(customers_id)
                return jsonify(Customer=result), 200

    def deleteCustomers(self, customer_id):
        udao = UsersDAO()
        cdao = CustomerDAO()
        customer = cdao.getCustomerById(customer_id)
        if not customer:
            return jsonify(Error="Customer not found."), 404
        else:
            user_id = cdao.delete(customer_id)
            udao.delete(user_id)
            return jsonify(DeleteStatus="OK"), 200
