from rolepermissions.roles import AbstractUserRole

class Author(AbstractUserRole):
    available_permissions = {
        'create_post': True,
    }

class Moderator(AbstractUserRole):
    available_permissions = {
        'edit_post': True
    }

