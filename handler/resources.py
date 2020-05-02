from flask import jsonify

from dao.food import FoodDAO
from dao.health import HealthDAO
from dao.power_resources import PowerResourcesDAO
from dao.resources import ResourcesDAO
from handler.Batteries import BatteriesHandler
from handler.clothing import ClothingHandler
from handler.food import FoodHandler
from handler.fuel import FuelHandler
from handler.health import HealthHandler
from handler.ice import IceHandler
from handler.power_resources import PowerResourcesHandler
from handler.water import WaterHandler


class ResourcesHandler:
    resources = [(1, "baby food", "false"),
                 (2, "tool", "true")]

    # ----------------utils-------------------
    def give_me_resource(self):
        return self.resources

    def getById(self, resource_id):
        for f in self.resources:
            if resource_id == f[0]:
                return f

    def insert_resource(self, resource_category, resource_availability):
        self.resources.append((len(self.resources) + 1, resource_category, resource_availability))
        return len(self.resources)

    def update_resource(self, resource_id, resource_category, resource_availability):
        self.resources.remove(self.getById(resource_id))
        self.resources.insert(resource_id - 1, (resource_id, resource_category, resource_availability))

    def delete_resource(self, resource_id):
        self.resources.remove(self.getById(resource_id))

    # --------------end utils-----------------

    def build_resource_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['resource_category'] = row[1]
        result['resource_availability'] = row[2]
        return result

    def build_resource_attributes(self, resource_id, resource_category, resource_availability):
        result = {}
        result['resource_id'] = resource_id
        result['resource_category'] = resource_category
        result['resource_availability'] = resource_availability
        return result

    def get_available_resources(self):
        handler_list = [FoodHandler(), HealthHandler(), WaterHandler(), IceHandler(), ClothingHandler(),
                        BatteriesHandler(), PowerResourcesHandler(), FuelHandler()]
        resources_list = []
        for handler in handler_list:
            resources_list.extend(handler.get_available_resources())
        return jsonify(Resources_Available=resources_list)

    # def get_resources_by_name(self):
    #     handler_list = [FoodHandler(), HealthHandler()]
    #     resources_list = []
    #     for handler in handler_list:
    #         resources_list.extend(handler.)
    #     return jsonify(Resources=resources_list)

    def getAllResources(self):
        flist = self.give_me_resource()
        result_list = []
        for row in flist:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def getResourceById(self, resource_id):
        row = self.getById(resource_id)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    def insertResourceJson(self, form):
        print("form: ", form)
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            resource_category = form['resource_category']
            resource_availability = form['resource_availability']
            if resource_category and resource_availability:
                resource_id = self.insert_resource(resource_category, resource_availability)
                result = self.build_resource_attributes(resource_id, resource_category, resource_availability)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateResource(self, resource_id, form):
        if not self.getResourceById(resource_id):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                resource_category = form['resource_category']
                resource_availability = form['resource_availability']
                if resource_category and resource_availability:
                    self.update_resource(resource_id, resource_category, resource_availability)
                    result = self.build_resource_attributes(resource_id, resource_category, resource_availability)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteResource(self, resource_id):
        if not self.getResourceById(resource_id):
            return jsonify(Error="Resource not found."), 404
        else:
            # dao.delete(pid)
            self.delete_resource(resource_id)
            return jsonify(DeleteStatus="OK"), 200



