from flask import current_app, g, request, Blueprint
from oso import Oso
from werkzeug.exceptions import Forbidden

bp = Blueprint("authorization", __name__)


@bp.before_app_request
def authorize_request():
    """Authorize the incoming request"""
    r = request._get_current_object()
    if not current_app.oso.is_allowed(g.current_user, r.method, r):
        return Forbidden("Not Authorized!")


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
