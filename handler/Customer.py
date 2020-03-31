from flask import jsonify


class CustomerHandler:

    customers = [(1),(2),(3)]

    #----------------utils-------------------
    def give_me_customers(self):
        return self.customers

    def getById(self, customers_id):
        for f in self.customers:
            if customers_id == f:
                return f

    def insert_customers(self):
        self.customers.append(len(self.customers) + 1)
        return len(self.customers)

    def update_customers(self, customers_id):
        self.customers.pop(customers_id-1)
        self.customers.insert(customers_id-1)

    def delete_customers(self, customers_id):
        self.customers.pop(customers_id - 1)
    #--------------end utils-----------------

    def build_customers_dict(self, list):
        result = {}
        result['customers_id'] = list
        return result

    def build_customers_attributes(self, customers_id):
        result = {}
        result['customers_id'] = customers_id
        return result

    def getAllCustomers(self):
        # dao = SupplierDAO()
        # suppliers_list = dao.getAllSuppliers()
        list = self.give_me_customers()
        result_list = []
        for row in list:
            result = self.build_customers_dict(row)
            result_list.append(result)
        return jsonify(Customers=result_list)

    def getCustomersById(self, customers_id):
        # dao = PartsDAO()
        # row = dao.getPartById(pid)
        row = self.getById(customers_id)
        if not row:
            return jsonify(Error="Customer Not Found"), 404
        else:
            customers = self.build_customers_dict(row)
            return jsonify(Customer=customers)

    def insertCustomersJson(self, form):
        print("form: ", form)
        if len(form) != 0:
            return jsonify(Error="Malformed post request"), 400
        else:
                # dao = PartsDAO()
                # pid = dao.insert(pname, pcolor, pmaterial, pprice)
                customer_id = self.insert_customers()
                result = self.build_customers_attributes(customer_id)
                return jsonify(Customer=result), 201


    def updateCustomers(self, customers_id, form):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getCustomersById(customers_id):
            return jsonify(Error = "Customer not found."), 404
        else:
            if len(form) != 0:
                return jsonify(Error="Malformed update request"), 400
            else:
                    # dao.update(pid, pname, pcolor, pmaterial, pprice)
                    self.update_customers(customers_id)
                    result = self.build_customers_attributes(customers_id)
                    return jsonify(Customer=result), 200

    def deleteCustomers(self, customers_id):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getCustomersById(customers_id):
            return jsonify(Error="Customer not found."), 404
        else:
            # dao.delete(pid)
            self.delete_customers(customers_id)
            return jsonify(DeleteStatus="OK"), 200