from flask_restx import Namespace, fields


class AuthDto:
    ns = Namespace("auth", description="Регистрация, аутентификация и получение токенов.")

    auth_register = ns.model(
        "Registration data",
        {
            "first_name": fields.String(description="User first name"),  # Optional
            "last_name": fields.String(description="User password"),  # Optional
            "email": fields.String(required=True, description="User email"),
            "password": fields.String(required=True, description="User password"),
        },
    )

    auth_login = ns.model(
        "Login data",
        {
            "email": fields.String(required=True, description="User email"),
            "password": fields.String(required=True, description="User password"),
        },
    )

    auth_change = ns.model(
        "User data",
        {
            "first_name": fields.String(description="User first name"),  # Optional
            "last_name": fields.String(description="User password"),  # Optional
            "email": fields.String(description="User email"),  # Optional
            "password": fields.String(description="User password"),  # Optional
        },
    )


class UserDto:
    ns = Namespace("users", "API управления пользователями для администраторов.")
    user_response = ns.model(
        "User",
        {
            "id": fields.Integer(readonly=True, description="User id number"),
            "first_name": fields.String(required=True, description="User first name"),
            "last_name": fields.String(required=True, description="User password"),
            "email": fields.String(required=True, description="User email"),
        },
    )

    user_request = ns.model(
        "User",
        {
            "first_name": fields.String(required=True, description="User first name"),
            "last_name": fields.String(required=True, description="User last name"),
            "email": fields.String(required=True, description="User email"),
            "password_hash": fields.String(required=True, description="User password"),
        },
    )

    role_response = ns.model(
        "Role",
        {
            "id": fields.Integer(readonly=True, description="Role id number"),
            "name": fields.String(required=True, description="Role name"),
        },
    )

    user_roles_req = ns.model(
        "User_roles",
        {
            "ids": fields.List(fields.Integer(required=True, description="Role id"), required=True),
        },
    )
    user_permissions_res = ns.model(
        "User_roles",
        {
            "id": fields.Integer(readonly=True, description="Permission id number"),
            "name": fields.String(required=True, description="Permission name"),
        },
    )


class RolesDto:
    ns = Namespace("roles", "API управления ролями для администраторов.")
    role_response = ns.model(
        "Roles",
        {
            "id": fields.Integer(readonly=True, description="Role id number"),
            "name": fields.String(required=True, description="Role name"),
        },
    )
    role_permissions_req = ns.model(
        "Role_permissions",
        {
            "ids": fields.List(fields.Integer(required=True, description="Permission id"), required=True),
        },
    )


class PermissionsDto:
    ns = Namespace("permissions", "API управления правами пользователей для администраторов.")

    permission_response = ns.model(
        "Permissions",
        {
            "id": fields.Integer(readonly=True, description="Permission id number"),
            "name": fields.String(required=True, description="Permission name"),
        },
    )


class SocialDto:
    ns = Namespace("social", "Вход через социальные сервисы")
