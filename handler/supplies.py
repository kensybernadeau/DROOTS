from flask import jsonify

from dao.request import requestDAO
from dao.supplies import SuppliesDAO


class SuppliesHandler:

    def build_supplies_attributes(self, resource_id, supplier_id, supplies_price, supplies_stock):
        result = {}
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        result['supplies_price'] = supplies_price
        result['supplies_stock'] = supplies_stock
        return result

    def insertSuppliesJson(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        resource_id = form['resource_id']
        supplier_id = form['supplier_id']
        supplies_price = form['supplies_price']
        supplies_stock = form['supplies_stock']
        if resource_id and supplier_id and supplies_price is not None and supplies_stock:
            dao = SuppliesDAO()
            dao.insert_supplies(resource_id, supplier_id, supplies_price, supplies_stock)
            result = self.build_supplies_attributes(resource_id, supplier_id,supplies_price, supplies_stock)
            return jsonify(Supplies=result), 201
