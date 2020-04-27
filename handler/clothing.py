from flask import jsonify


class ClothingHandler:

    clothes = [(1, "top", "sm","for babies"),
              (2, "bottom", "md", "for babies")]

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
        self.clothes.remove(self.getById(clothe_id))
        self.clothes.insert(clothe_id-1, (clothe_id, clothe_type, clothe_size_, clothe_description))

    def delete_clothe(self, clothe_id):
        self.clothes.remove(self.getById(clothe_id))
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
        flist = self.give_me_clothes()
        result_list = []
        for row in flist:
            result = self.build_clothe_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClotheById(self, clothe_id):
        row = self.getById(clothe_id)
        if not row:
            return jsonify(Error="Clothe Not Found"), 404
        else:
            clothe = self.build_clothe_dict(row)
            return jsonify(Clothe=clothe)

    def insertClotheJson(self, json):
        print("json: ", json)
        if len(json) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            clothe_type = json['clothe_type']
            clothe_size = json['clothe_size']
            clothe_description = json['clothe_description']
            if clothe_type and clothe_size and clothe_description:
                clothe_id = self.insert_clothe(clothe_type, clothe_size, clothe_description)
                result = self.build_clothe_attributes(clothe_id, clothe_type, clothe_size, clothe_description)
                return jsonify(Clothe=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateClothe(self, clothe_id, form):
        if not self.getClotheById(clothe_id):
            return jsonify(Error = "Clothe not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                clothe_type = form['clothe_type']
                clothe_size = form['clothe_size']
                clothe_description = form['clothe_description']
                if clothe_type and clothe_size and clothe_description:
                    self.update_clothe(clothe_id, clothe_type, clothe_size, clothe_description)
                    result = self.build_clothe_attributes(clothe_id, clothe_size, clothe_description)
                    return jsonify(Cloth=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteClothe(self, clothe_id):
        if not self.getClotheById(clothe_id):
            return jsonify(Error="Clothe not found."), 404
        else:
            # dao.delete(pid)
            self.delete_clothe(clothe_id)
            return jsonify(DeleteStatus="OK"), 200