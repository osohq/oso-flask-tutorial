def init_oso(app):
    from oso import Oso  # (1)

    from .user import User
    from .expense import Expense

    oso = Oso()  # (2)

    oso.register_class(User)  # (3)
    oso.register_class(Expense)
    app.oso = oso  # (4)

    oso.load_file("app/authorization.polar")


# start-authorize
from flask import current_app, g
from werkzeug.exceptions import Forbidden


def authorize(action, resource):
    """Can the current user perform `action` on `resource`?"""
    if current_app.oso.is_allowed(g.current_user, action, resource):
        return resource
    else:
        raise Forbidden("Not Authorized!")
