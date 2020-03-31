from flask import jsonify


class ClothingHandler:

    clothes = [(1, "top", 20, "small",),
            (2, "bottom", 30, "05/30/2020", "romana", "for babies")]

    #----------------utils-------------------
    def give_me_clothes(self):
        return self.clothes

    def getById(self, clothes_id):
        for f in self.clothes:
            if clothes_id == f[0]:
                return f

    def insert_clothe(self, clothe_type, clothe_size_, clothe_description):
        self.clothes.append((len(self.clothes) + 1, clothe_type, clothe_size_, clothe_description))
        return len(self.clothes)

    def update_clothe(self, clothe_id, clothe_type, clothe_size_, clothe_description):
        self.clothes.pop(clothe_id-1)
        self.clothes.insert(clothe_id-1, (clothe_id, clothe_type, clothe_size_, clothe_description))

    def delete_clothe(self, clothe_id):
        self.clothes.pop(clothe_id - 1)
    #--------------end utils-----------------

    def build_clothe_dict(self, row):
        result = {}
        result['clothe_id'] = row[0]
        result['clothe_type'] = row[1]
        result['clothe_size'] = row[2]
        result['clothe_description'] = row[3]
        return result

    def build_clothe_attributes(self, clothe_id, clothe_type, clothe_size, clothe_description):
        result = {}
        result['clothe_id'] = clothe_id
        result['clothe_type'] = clothe_type
        result['clothe_size'] = clothe_size
        result['clothe_description'] = clothe_description
        return result

    def getAllclothes(self):
        # dao = SupplierDAO()
        # suppliers_list = dao.getAllSuppliers()
        flist = self.give_me_clothes()
        result_list = []
        for row in flist:
            result = self.build_clothe_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClotheById(self, clothe_id):
        # dao = PartsDAO()
        # row = dao.getPartById(pid)
        row = self.getById(clothe_id)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            clothe = self.build_clothe_dict(row)
            return jsonify(Clothe=clothe)

    def insertClotheJson(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            clothe_type = form['clothe_type']
            clothe_size = form['clothe_size']
            clothe_description = form['clothe_description']
            if clothe_type and clothe_size and clothe_description:
                # dao = PartsDAO()
                # pid = dao.insert(pname, pcolor, pmaterial, pprice)
                clothe_id = self.insert_clothe(clothe_type, clothe_size, clothe_description)
                result = self.build_clothe_attributes(clothe_id, clothe_type, clothe_size, clothe_description)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateClothe(self, clothe_id, form):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getClotheById(clothe_id):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                clothe_type = form['clothe_type']
                clothe_size = form['clothe_size']
                clothe_description = form['clothe_description']
                if clothe_type and clothe_size and clothe_description:
                    # dao.update(pid, pname, pcolor, pmaterial, pprice)
                    self.update_clothe(clothe_id, clothe_type, clothe_size, clothe_description)
                    result = self.build_clothe_attributes(clothe_id, clothe_size, clothe_description)
                    return jsonify(Part=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteClothe(self, clothe_id):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getClotheById(clothe_id):
            return jsonify(Error="Part not found."), 404
        else:
            # dao.delete(pid)
            self.delete_clothe(clothe_id)
            return jsonify(DeleteStatus="OK"), 200