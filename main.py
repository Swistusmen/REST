from flask import Flask
from Models import db
import os
from Shop import Shop
from Gallery import Gallery
from Models import app, db, wasDB, api

if not wasDB:
    print("A")
    db.create_all()

api.add_resource(Shop,"/Shop/<int:shop_id>")
api.add_resource(Gallery, "/Gallery/<int:room_id>")
if __name__ == "__main__":
    app.run(debug=True)


