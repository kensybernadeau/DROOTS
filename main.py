from flask import Flask, jsonify, request
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
from handler.food import FoodHandler

app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'


@app.route('/DROOTS/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
    else:
        return {"": "Ford", "model": "Mustang", "year": 1964}


@app.route('/DROOTS/food', methods=['GET', 'POST'])
def getAllFood():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return FoodHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return FoodHandler().getAllFood()
        else:
            return FoodHandler().search_food(request.args)

@app.route('/DROOTS/food/<int:food_id>', methods=['GET', 'PUT', 'DELETE'])
def getFoodById(food_id):
    if request.method == 'GET':
        return FoodHandler().getFoodById(food_id)
    elif request.method == 'PUT':
        return FoodHandler().updatePart(food_id, request.form)
    elif request.method == 'DELETE':
        return FoodHandler().deletePart(food_id)
    else:
        return jsonify(Error="Method not allowed."), 405


if __name__ == '__main__':
    app.run()