from flask import jsonify


class FoodHandler:

    food = [(1, "water", 20, "05/30/2020", "16oz", "for people"),
            (2, "lechuga", 30, "05/30/2020", "romana", "for babies")]

    #----------------utils-------------------
    def give_me_food(self):
        return self.food

    def getById(self, food_id):
        for f in self.food:
            if food_id == f[0]:
                return f

    def insert_food(self, food_name, food_quantity, food_exp_date, food_type, food_description):
        self.food.append((len(self.food) + 1, food_name, food_quantity, food_exp_date, food_type, food_description))
        return len(self.food)

    def update_food(self, food_id, food_name, food_quantity, food_exp_date, food_type, food_description):
        self.food.remove(self.getById(food_id))
        self.food.insert(food_id-1, (food_id, food_name, food_quantity, food_exp_date, food_type, food_description))

    def delete_food(self, food_id):
        self.food.remove(self.getById(food_id))
    #--------------end utils-----------------

    def build_food_dict(self, row):
        result = {}
        result['food_id'] = row[0]
        result['food_name'] = row[1]
        result['food_quantity'] = row[2]
        result['food_exp_date'] = row[3]
        result['food_type'] = row[4]
        result['food_description'] = row[5]
        return result

    def build_food_attributes(self, food_id, food_name, food_quantity, food_exp_date, food_type, food_description):
        result = {}
        result['food_id'] = food_id
        result['food_name'] = food_name
        result['food_quantity'] = food_quantity
        result['food_exp_date'] = food_exp_date
        result['food_type'] = food_type
        result['food_description'] = food_description
        return result

    def getAllFood(self):
        flist = self.give_me_food()
        result_list = []
        for row in flist:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food=result_list)

    def getFoodById(self, food_id):
        row = self.getById(food_id)
        if not row:
            return jsonify(Error="Food Not Found"), 404
        else:
            food = self.build_food_dict(row)
            return jsonify(Food=food)

    def insertFoodJson(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            food_name = form['food_name']
            food_quantity = form['food_quantity']
            food_exp_date = form['food_exp_date']
            food_type = form['food_type']
            food_description = form['food_description']
            if food_name and food_quantity and food_exp_date and food_type  and food_description:
                food_id = self.insert_food(food_name, food_quantity, food_exp_date, food_type, food_description)
                result = self.build_food_attributes(food_id, food_name, food_quantity, food_exp_date, food_type, food_description)
                return jsonify(Food=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateFood(self, food_id, form):
        if not self.getFoodById(food_id):
            return jsonify(Error = "Food not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                food_name = form['food_name']
                food_quantity = form['food_quantity']
                food_exp_date = form['food_exp_date']
                food_type = form['food_type']
                food_description = form['food_description']
                if food_name and food_quantity and food_exp_date and food_type  and food_description:
                    self.update_food(food_id, food_name, food_quantity, food_exp_date, food_type, food_description)
                    result = self.build_food_attributes(food_id, food_name, food_quantity, food_exp_date, food_type,
                                                        food_description)
                    return jsonify(food=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteFood(self, food_id):
        if not self.getFoodById(food_id):
            return jsonify(Error="Food not found."), 404
        else:
            self.delete_food(food_id)
            return jsonify(DeleteStatus="OK"), 200