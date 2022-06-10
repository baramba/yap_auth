from enum import Enum


class Rules(Enum):
    auth_change = "/api/v1/auth/change"
    auth_history = "/api/v1/auth/history"
    auth_login = "/api/v1/auth/login"
    auth_logout = "/api/v1/auth/logout"
    auth_register = "/api/v1/auth/registration"
    auth_refresh_token = "/api/v1/auth/refresh"
    permissions = "/api/v1/permissions/<int:id>"
    permissions_post = "/api/v1/permissions/"
    roles = "/api/v1/roles/{id}"
    roles_post = "/api/v1/roles/"
    roles_permissions = "/api/v1/roles/{id}/permissions"
    users = "/api/v1/users/{id}"
    users_post = "/api/v1/users/"
    users_roles = "/api/v1/users/{id}/roles/"
