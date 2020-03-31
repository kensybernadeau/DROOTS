from flask import jsonify


class SupplierHandler:

    supplier = [(1, "San Lorezo"), (2, "San Juan")]

    #----------------utils-------------------
    def give_me_supplier(self):
        return self.supplier

    def getById(self, supplier_id):
        for f in self.supplier:
            if supplier_id == f[0]:
                return f

    def insert_supplier(self, supplier_location):
        self.supplier.append((len(self.supplier) + 1, supplier_location))
        return len(self.supplier)

    def update_supplier(self, supplier_id, supplier_location):
        self.supplier.pop(supplier_id-1)
        self.supplier.insert(supplier_id-1, (supplier_id, supplier_location))

    def delete_supplier(self, supplier_id):
        f = self.getById(supplier_id)
        self.supplier.remove(f)
    #--------------end utils-----------------

    def build_supplier_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['supplier_location'] = row[1]
        return result

    def build_supplier_attributes(self, supplier_id, supplier_location):
        result = {}
        result['supplier_id'] = supplier_id
        result['supplier_location'] = supplier_location
        return result

    def getAllSupplier(self):
        # dao = SupplierDAO()
        # suppliers_list = dao.getAllSuppliers()
        flist = self.give_me_supplier()
        result_list = []
        for row in flist:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    def getSupplierById(self, supplier_id):
        # dao = SuppliersDAO()
        # row = dao.getSupplierById(pid)
        row = self.getById(supplier_id)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier=supplier)

    def insertSupplierJson(self, form):
        print("form: ", form)
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            supplier_location = form['supplier_location']
            if supplier_location:
                # dao = SuppliersDAO()
                # pid = dao.insert(pname, pcolor, pmaterial, pprice)
                supplier_id = self.insert_supplier(supplier_location)
                result = self.build_supplier_attributes(supplier_id, supplier_location)
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateSupplier(self, supplier_id, form):
        # dao = SuppliersDAO()
        # if not dao.getSupplierById(pid):
        if not self.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                supplier_location = form['supplier_location']
                if supplier_location:
                    # dao.update(pid, pname, pcolor, pmaterial, pprice)
                    self.update_supplier(supplier_id, supplier_location)
                    result = self.build_supplier_attributes(supplier_id, supplier_location)
                    return jsonify(Supplier=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteSupplier(self, supplier_id):
        # dao = SuppliersDAO()
        # if not dao.getSupplierById(pid):
        if not self.getSupplierById(supplier_id):
            return jsonify(Error="Supplier not found."), 404
        else:
            # dao.delete(pid)
            self.delete_supplier(supplier_id)
            return jsonify(DeleteStatus="OK"), 200