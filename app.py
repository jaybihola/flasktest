import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)


# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#
#     if "name" not in store_data:
#         abort(400, message="Bad Request. Ensure 'name' is included")
#
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400, message="Store already exists")
#
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store, 201
#
#
# @app.get("/store")
# def get_stores():
#     return {"stores": list(stores.values())}
#
#
# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         abort(404, message="Store not found")
#
#
# @app.put("/store/<string:store_id>")
# def update_store(store_id):
#     store_data = request.get_json()
#
#     if "name" not in store_data:
#         abort(400, message="Bad request. Please provide fields to update")
#
#     try:
#         curr_store = stores[store_id]
#         curr_store |= store_data
#         return curr_store
#     except KeyError:
#         abort(404, message="Item not found")
#
#
#
# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "Store deleted"}
#     except KeyError:
#         abort(404, message="Store not found")
#
#
# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#
#     if ("price" not in item_data or "store_id" not in item_data or "name" not in item_data):
#         abort(400, message="Bad request. Ensure 'price', 'store_id', and 'name are included")
#
#     if item_data["store_id"] not in stores:
#         abort(404, message="Store not found")
#
#     for item in items.values():
#         if item["name"] == item_data["name"] \
#                 and item["store_id"] == item_data["store_id"]:
#             abort(400, message="Item already exists")
#
#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item
#
#     return item, 201
#
#
# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}, 200
#
#
# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except:
#         abort(404, message="Item not found")
#
#
# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#
#     if "price" not in item_data or "name" not in item_data:
#         abort(400, message="Bad request. Please provide fields to update")
#
#     try:
#         curr_item = items[item_id]
#         curr_item |= item_data
#         return curr_item
#     except KeyError:
#         abort(404, message="Item not found")
#
#
# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted"}
#     except KeyError:
#         abort(404, message="Item not found")