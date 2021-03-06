from flask import Blueprint
from flask_restx import Api

from app.api.v1.auth import ns as auth

from .permissions import ns as permissions
from .roles import ns as roles
from .social import ns as social
from .users import ns as users

blueprint = Blueprint("Auth_v1", __name__, url_prefix="/api/v1")


authorizations = {
    "apikey": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token",
    }
}

api = Api(
    blueprint,
    title="API для аутентификации и API управления ролями",
    version="1.0",
    description="",
    validate=True,
    authorizations=authorizations,
    security="apikey",
    # All API metadatas
)


api.add_namespace(users)
api.add_namespace(roles)
api.add_namespace(permissions)
api.add_namespace(auth)
api.add_namespace(social)
