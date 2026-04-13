from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # must run before importing blueprints so ORS_API_KEY is available at module init

from routes.destination_routes import destination_bp
from routes.route_routes import route_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(destination_bp)
app.register_blueprint(route_bp)

if __name__ == "__main__":
    app.run(debug=True)
