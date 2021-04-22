"""Entrypoint to the expenses application"""

from flask import Flask

from . import authorization, db, expense, organization, user


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(DATABASE="expenses.db")

    # register DB handlers
    app.register_blueprint(db.bp)
    # register user handlers
    app.register_blueprint(user.bp)
    # register expenses routes
    app.register_blueprint(expense.bp)
    # register organizations routes
    app.register_blueprint(organization.bp)

    authorization.init_oso(app)

    return app


app = create_app()
