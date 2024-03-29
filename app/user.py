from dataclasses import dataclass
from flask import current_app, g, request, Blueprint
from werkzeug.exceptions import NotFound, Unauthorized

from .db import query_db

bp = Blueprint("user", __name__)


class Actor:
    """base abstract user type"""

    pass


@dataclass
class User(Actor):
    """Logged in user. Has an email address."""

    id: int
    email: str
    title: str

    @classmethod
    def get(cls, id: int):
        record = query_db(
            "select id, email, title from users where id = ?", [id], one=True
        )
        if record:
            return cls(**record)
        else:
            raise NotFound()

    @classmethod
    def lookup(cls, email: str):
        record = query_db(
            "select id, email, title from users where email = ?", [email], one=True
        )
        if record:
            return cls(**record)
        else:
            raise NotFound()


class Guest(Actor):
    """Anonymous user."""

    def __str__(self):
        return "Guest"


@bp.before_app_request
def set_current_user():
    """Set the `current_user` from the authorization header (if present)"""
    if not "current_user" in g:
        email = request.headers.get("user")
        if email:
            try:
                g.current_user = User.lookup(email)
            except Exception as e:
                current_app.logger.exception(e)
                return Unauthorized("user not found")
        else:
            g.current_user = Guest()
