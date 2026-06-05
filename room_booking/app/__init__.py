from flask import Flask

from app.models import db


def create_app(config=None):

    app = Flask(__name__)

    if config is None:
        from config import DevelopmentConfig

        config = DevelopmentConfig

    app.config.from_object(config)

    db.init_app(app)

    from app.routes.bookings import bookings_bp
    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(bookings_bp)
    app.register_blueprint(dashboard_bp)

    with app.app_context():
        db.create_all()

    return app
