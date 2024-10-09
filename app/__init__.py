from flasgger import Swagger
from flask import Flask, request
from flask_cors import CORS

APP_HOST = "0.0.0.0"
APP_NAME = "rwl-activity-backend"
APP_NAME_FT = "RwlActivity"
APP_PORT = 8000

server = None

def start(debug=False, use_debugger=False, use_reloader=False):
    server = create()
    server.run(
        host=APP_HOST, port=APP_PORT, debug=debug, use_debugger=use_debugger, use_reloader=use_reloader, threaded=True
    )
    return server

def __bind_swagger(server):
    template = {
        "swagger": "2.0",
        "info": {"title": APP_NAME_FT, "uiversion": 3, "description": f"API for {APP_NAME_FT}"},
        "basePath": "/",
        "schemes": ["http"],
        "consumes": ["application/json"],
        "produces": ["application/json"],
        "securityDefinitions": {"Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}},
    }
    config = {
        "title": APP_NAME_FT,
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec",
                "route": "/apispec.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
    }
    Swagger(server, template=template, config=config, merge=True)

def create():
    server = Flask(__name__)
    from app.views import bp
    server.register_blueprint(bp)
    CORS(server)
    __bind_swagger(server)
    return server