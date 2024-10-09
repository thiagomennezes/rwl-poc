
from app.orchestration import Orchestrator
from flask import Blueprint, request
import json


bp = Blueprint("orchestrator", __name__)

@bp.route("/pipelines/start/", methods=["POST"])
def add():
    """
    Start a pipeline
    ---
    parameters:
        - in: body
          name: data
          required: true
          schema:
            type: object
            properties:
                lhs:
                    type: number
                rhs:
                    type: number
    responses:
        200:
            description: Success
    """
    payload = request.json
    orchestrator = Orchestrator()
    result = orchestrator.start(payload.get("lhs"), payload.get("rhs"))
    return json.dumps({"message": "Succes", "data": result}), 200