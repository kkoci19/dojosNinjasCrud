from flask_app import app
from flask_app.controllers import dojos
from flask_app.controllers import ninjas
# will import controllers here

if __name__ == "__main__":
    app.run(debug=True)
