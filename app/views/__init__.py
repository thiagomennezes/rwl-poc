from flask import Blueprint
import sys

def __register_views(bp, views):
    for view in views:
        module = f"app.views.{view}"
        __import__(module)
        child = sys.modules[module].bp
        bp.register_blueprint(child)

bp = Blueprint("all", __name__)
__register_views(bp, ["orchestrator"])
