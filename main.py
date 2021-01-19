from flask import Flask
from Models import db
import os
from Shop import Shop
from Room import Room
from Models import app, db, wasDB, api
from Rooms import Rooms

if not wasDB:
    print("A")
    db.create_all()

api.add_resource(Shop,"/Shop/<int:shop_id>")
api.add_resource(Room, "/Room/<int:room_id>")
api.add_resource(Rooms,"/Rooms/")
if __name__ == "__main__":
    app.run(debug=True)


