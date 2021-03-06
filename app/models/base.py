from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = db.session
