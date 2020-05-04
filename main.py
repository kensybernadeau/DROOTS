from flask import Flask, jsonify, request
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin
# dhf
# Activate
from handler.Administrator import AdministratorsHandler
from handler.Batteries import BatteriesHandler
from handler.Customer import CustomerHandler
from handler.HeavyEquipment import HeavyEquipmentHandler
from handler.Payment import PaymentHandler
from handler.Request import RequestHandler
from handler.Reservation import ReservationHandler
from handler.address import AddressHandler
from handler.food import FoodHandler
from handler.fuel import FuelHandler
from handler.health import HealthHandler
from handler.ice import IceHandler
from handler.power_resources import PowerResourcesHandler
from handler.supplier import SupplierHandler
from handler.user import UserHandler
from handler.clothing import ClothingHandler
from handler.tools import ToolsHandler
from handler.resources import ResourcesHandler
from handler.water import WaterHandler

app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the Disaster Relief Oriented One-on-one Technology Services ( DROOTS) DB App!'


@app.route('/droots/resources', methods=['GET', 'POST'])
def get_available_resources():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ResourcesHandler().insertResourceJson(request.json)
    else:
        if not request.args:
            return ResourcesHandler().get_available_resources()
        else:
            return ResourcesHandler().searchResources(request.args)


@app.route('/droots/resources/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(resource_id)
    elif request.method == 'PUT':
        return ResourcesHandler().updateResource(resource_id, request.json)
    elif request.method == 'DELETE':
        return ResourcesHandler().deleteResource(resource_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/supplied', methods=['GET', 'POST'])
def get_resources_supplied():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ResourcesHandler().insertResourceJson(request.json)
    else:
        if not request.args:
            return ResourcesHandler().get_resources_supplied()
        else:
            return ResourcesHandler().searchResources(request.rgs)

@app.route('/droots/resources/food', methods=['GET', 'POST'])
def getAllFood():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FoodHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return FoodHandler().getAllFood()


@app.route('/droots/resources/food/<int:food_id>', methods=['GET', 'PUT', 'DELETE'])
def getFoodById(food_id):
    if request.method == 'GET':
        return FoodHandler().getFoodById(food_id)
    elif request.method == 'PUT':
        return FoodHandler().updateFood(food_id, request.json)
    elif request.method == 'DELETE':
        return FoodHandler().deleteFood(food_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/droots/resources/food/canned', methods=['GET', 'POST'])
def getCannedFood():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FoodHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return FoodHandler().get_food_by_type('canned')

@app.route('/droots/resources/food/dry', methods=['GET', 'POST'])
def getDryFood():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FoodHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return FoodHandler().get_food_by_type('dry')

@app.route('/droots/resources/food/baby', methods=['GET', 'POST'])
def getBabyFood():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FoodHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return FoodHandler().get_food_by_type('baby')


@app.route('/droots/resources/water', methods=['GET', 'POST'])
def getAllWater():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return WaterHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return WaterHandler().getAllWater()


@app.route('/droots/resources/water/<int:water_id>', methods=['GET', 'PUT', 'DELETE'])
def getWaterById(water_id):
    if request.method == 'GET':
        return WaterHandler().getWaterById(water_id)
    elif request.method == 'PUT':
        return WaterHandler().updateWater(water_id, request.json)
    elif request.method == 'DELETE':
        return WaterHandler().deleteWater(water_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/droots/resources/water/smallbottle', methods=['GET', 'POST'])
def getSmallBottleWater():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return WaterHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return WaterHandler().get_water_by_type('sb')

@app.route('/droots/resources/water/onegallon', methods=['GET', 'POST'])
def getOneGallonWater():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return WaterHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return WaterHandler().get_water_by_type('1g')


@app.route('/droots/resources/ice', methods=['GET', 'POST'])
def getAllIce():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return IceHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return IceHandler().getAllIce()


@app.route('/droots/resources/ice/<int:ice_id>', methods=['GET', 'PUT', 'DELETE'])
def getIceById(ice_id):
    if request.method == 'GET':
        return IceHandler().getIceById(ice_id)
    elif request.method == 'PUT':
        return IceHandler().updateIce(ice_id, request.json)
    elif request.method == 'DELETE':
        return IceHandler().deleteIce(ice_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/health', methods=['GET', 'POST'])
def getAllHealth():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return HealthHandler().insertHealthJson(request.json)
    else:
        if not request.args:
            return HealthHandler().getAllHealth()


@app.route('/droots/resources/health/<int:health_id>', methods=['GET', 'PUT', 'DELETE'])
def getHealthById(health_id):
    if request.method == 'GET':
        return HealthHandler().getHealthById(health_id)
    elif request.method == 'PUT':
        return HealthHandler().updateHealth(health_id, request.json)
    elif request.method == 'DELETE':
        return HealthHandler().deleteHealth(health_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/supplier', methods=['GET', 'POST'])
def getAllSupplier():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return SupplierHandler().insertSupplierJson(request.json)
    else:
        if not request.args:
            return SupplierHandler().getAllSupplier()


@app.route('/droots/supplier/<int:supplier_id>', methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(supplier_id):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(supplier_id)
    elif request.method == 'PUT':
        return SupplierHandler().updateSupplier(supplier_id, request.json)
    elif request.method == 'DELETE':
        return SupplierHandler().deleteSupplier(supplier_id)
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


@app.route('/droots/resources/powerresources/<int:power_resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getPowerResourceById(power_resource_id):
    if request.method == 'GET':
        return PowerResourcesHandler().getPowerResourcesById(power_resource_id)

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
            return FuelHandler().getAllFuel()


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


@app.route('/droots/resources/clothing', methods=['GET', 'POST'])
def getAllClothes():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ClothingHandler().insertClotheJson(request.json)
    else:
        if not request.args:
            return ClothingHandler().getAllclothes()


@app.route('/droots/resources/clothing/<int:clothe_id>', methods=['GET', 'PUT', 'DELETE'])
def getClotheById(clothe_id):
    if request.method == 'GET':
        return ClothingHandler().getClotheById(clothe_id)
    elif request.method == 'PUT':
        return ClothingHandler().updateClothe(clothe_id, request.json)
    elif request.method == 'DELETE':
        return ClothingHandler().deleteClothe(clothe_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/tools', methods=['GET', 'POST'])
def getAllTools():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ToolsHandler().insertToolJson(request.json)
    else:
        if not request.args:
            return ToolsHandler().getAllTools()


@app.route('/droots/resources/tools/<int:tool_id>', methods=['GET', 'PUT', 'DELETE'])
def getToolById(tool_id):
    if request.method == 'GET':
        return ToolsHandler().getToolsById(tool_id)
    elif request.method == 'PUT':
        return ToolsHandler().updateTool(tool_id, request.json)
    elif request.method == 'DELETE':
        return ToolsHandler().deleteTool(tool_id)
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


@app.route('/droots/customer/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def getCustomerById(customer_id):
    if request.method == 'GET':
        return CustomerHandler().getCustomersById(customer_id)
    elif request.method == 'PUT':
        return CustomerHandler().updateCustomers(customer_id, request.form)
    elif request.method == 'DELETE':
        return CustomerHandler().deleteCustomers(customer_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/customer', methods=['GET', 'POST'])
def getAllCustomer():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CustomerHandler().insertCustomersJson(request.json)

    else:
        return CustomerHandler().getAllCustomers()


@app.route('/droots/customer/request/<int:request_id>', methods=['GET', 'POST', 'PUT'])
def getRequestById(request_id):
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return RequestHandler().insertRequestJson(request.json)
    elif request.method == 'GET':
        return RequestHandler().getAllRequest()
    elif request.method == 'PUT':
        return RequestHandler().updateRequest(request_id, request.form)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/customer/reservation/<int:reservation_id>', methods=['GET', 'POST', 'PUT'])
def getReservationById(reservation_id):
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ReservationHandler().insertReservationJson(request.json)
    elif request.method == 'GET':
        return ReservationHandler().getReservationById(reservation_id)
    elif request.method == 'PUT':
        return ReservationHandler().updateReservation(reservation_id, request.form)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/heavyequipment/', methods=['GET', 'POST', ])
def getAllHEquipment():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return HeavyEquipmentHandler().insertHEquipmentJson(request.json)
    elif request.method == 'GET':
        return HeavyEquipmentHandler().getAllHeavyEquipment()

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/heavyequipment/<int:hequipment_id>', methods=['GET', 'POST', 'PUT'])
def getHEquipmentById(hequipment_id):
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return HeavyEquipmentHandler().insertHEquipmentJson(request.json)
    elif request.method == 'GET':
        return HeavyEquipmentHandler().getHeavyEquipmentById(hequipment_id)
    elif request.method == 'PUT':
        return HeavyEquipmentHandler().updateHEquipment(hequipment_id, request.form)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/batteries/<int:batteries_id>', methods=['GET', 'PUT', 'DELETE'])
def getBatteriesById(batteries_id):
    if request.method == 'GET':
        return BatteriesHandler().getBatteriesById(batteries_id)
    elif request.method == 'PUT':
        return BatteriesHandler().updateBatteries(batteries_id, request.form)
    elif request.method == 'DELETE':
        return BatteriesHandler().deleteBatteries(batteries_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/batteries', methods=['GET', 'POST'])
def getAllBatteries():
    if request.method == 'GET':
        return BatteriesHandler().getAllBatteries()

    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return BatteriesHandler().insertBatteriesJson(request.json)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/payment/<int:payment_id>', methods=['GET', 'PUT', 'DELETE'])
def getPaymentById(payment_id):
    if request.method == 'GET':
        return PaymentHandler().getPaymentById(payment_id)
    elif request.method == 'PUT':
        return PaymentHandler().updatePayment(payment_id, request.json)
    elif request.method == 'DELETE':
        return PaymentHandler().deletePayment(payment_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/payment', methods=['GET', 'POST'])
def getAllPayment():
    if request.method == 'GET':
        return PaymentHandler().getAllPayment()

    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PaymentHandler().insertPaymentJson(request.json)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/address', methods=['GET', 'POST'])
def getAllAddress():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return AddressHandler().insertAddressJson(request.json)

    else:
        return AddressHandler().getAllAddress()


@app.route('/droots/address/<int:address_id>', methods=['GET', 'PUT', 'DELETE'])
def getAddressById(address_id):
    if request.method == 'GET':
        return AddressHandler().getAddressById(address_id)
    elif request.method == 'PUT':
        return AddressHandler().updateAddress(address_id, request.json)
    elif request.method == 'DELETE':
        return AddressHandler().deleteAddress(address_id)
    else:
        return jsonify(Error="Method not allowed."), 405


if __name__ == '__main__':
    app.run()
