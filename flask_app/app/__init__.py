from app.extensions import db
from app.utils.utils_db import init_db
from config import Config
from flask import Flask
from flask_migrate import Migrate

def create_app(config_class=Config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config_class)

    ##
    # Initialize Flask extensions
    ##

    # Set db
    db.init_app(app)

    ##
    # Migrate database
    ##

    migrate = Migrate(app,db)

    ##
    # Register blueprints
    ##

    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    with app.app_context():
        init_db()    

    return app