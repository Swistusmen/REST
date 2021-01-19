from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
databaseName="database.db"
wasDB= False
if os.path.exists(databaseName):
    wasDB=True

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+databaseName
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if wasDB:
    db.create_all()
db= SQLAlchemy()