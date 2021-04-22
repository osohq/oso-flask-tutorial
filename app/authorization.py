from flask import current_app, g
from oso import Oso
from werkzeug.exceptions import Forbidden

def authorize(action, resource):
    """Authorize whether the current user can perform `action` on `resource`"""
    if current_app.oso.is_allowed(g.current_user, action, resource):
        return resource
    else:
        raise Forbidden("Not Authorized!")


# start-init
def init_oso(app):
    from .user import User
    from .expense import Expense

    oso = Oso()

    oso.register_class(User)
    oso.register_class(Expense)
    oso.load_file("app/authorization.polar")
    app.oso = oso
