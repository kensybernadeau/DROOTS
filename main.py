from flask import Flask, jsonify, request
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
from handler.Administrator import AdministratorsHandler
from handler.food import FoodHandler
from handler.fuel import FuelHandler
from handler.power_resources import PowerResourcesHandler
from handler.user import UserHandler

app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'


@app.route('/droots/resources/food', methods=['GET', 'POST'])
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


@app.route('/droots/resources/food/<int:food_id>', methods=['GET', 'PUT', 'DELETE'])
def getFoodById(food_id):
    if request.method == 'GET':
        return FoodHandler().getFoodById(food_id)
    elif request.method == 'PUT':
        return FoodHandler().updatePart(food_id, request.json)
    elif request.method == 'DELETE':
        return FoodHandler().deletePart(food_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)

    else:
        return UserHandler().getAllUsers()


@app.route('/droots/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(user_id):
    if request.method == 'GET':
        return UserHandler().getUserById(user_id)

    elif request.method == 'PUT':
        return UserHandler().updateUser(user_id, request.form)

    elif request.method == 'DELETE':
        return UserHandler().deleteUser(user_id)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/powerresources', methods=['GET', 'POST'])
def getAllPowerResources():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PowerResourcesHandler().insertPowerResourceJson(request.json)

    else:
        if not request.args:
            return PowerResourcesHandler().getAllPowerResources()
        else:
            return PowerResourcesHandler().searchPowerResources(request.args)


@app.route('/droots/resources/powerresources/<int:power_resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getPowerResourceById(power_resource_id):
    if request.method == 'GET':
        return PowerResourcesHandler().getPowerResourceById(power_resource_id)

    elif request.method == 'PUT':
        return PowerResourcesHandler().updatePowerResource(power_resource_id, request.form)

    elif request.method == 'DELETE':
        return PowerResourcesHandler().deletePowerResource(power_resource_id)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/fuel', methods=['GET', 'POST'])
def getAllFuels():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FuelHandler().insertFuelJson(request.json)

    else:
        if not request.args:
            return FuelHandler().getAllFuels()
        else:
            return FuelHandler().searchFuels(request.args)


@app.route('/droots/resources/fuel/<int:fuel_id>', methods=['GET', 'PUT', 'DELETE'])
def getFuelById(fuel_id):
    if request.method == 'GET':
        return FuelHandler().getFuelById(fuel_id)

    elif request.method == 'PUT':
        return FuelHandler().updateFuel(fuel_id, request.form)

    elif request.method == 'DELETE':
        return FuelHandler().deleteFuel(fuel_id)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/administrators', methods=['GET', 'POST'])
def getAllAdministrators():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return AdministratorsHandler().insertAdministratorJson(request.json)

    else:
        return AdministratorsHandler().getAllAdministrators()


@app.route('/droots/administrators/<int:administrator_id>', methods=['GET', 'PUT', 'DELETE'])
def getAdministratorById(administrator_id):
    if request.method == 'GET':
        return AdministratorsHandler().getAdministratorById(administrator_id)

    elif request.method == 'PUT':
        return AdministratorsHandler().updateAdministrator(administrator_id, request.form)

    elif request.method == 'DELETE':
        return AdministratorsHandler().deleteAdministrator(administrator_id)

    else:
        return jsonify(Error="Method not allowed."), 405


if __name__ == '__main__':
    app.run()
