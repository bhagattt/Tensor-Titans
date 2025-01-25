from flask import Flask
from app.routes.investment import investment_bp

def create_app():
    app = Flask(__name__)

    # Register routes
    app.register_blueprint(investment_bp, url_prefix='/api')

    return app