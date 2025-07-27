from flask import Flask 

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    from app.main import main_bp
    from app.main import routes
    app.register_blueprint(main_bp)
    
    from app.auth import auth_bp
    from app.auth import routes
    app.register_blueprint(auth_bp)
    
    return app
