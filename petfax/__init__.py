from flask import Flask 
from . import facts


def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    from . import pet
    app.register_blueprint(pet.bp)

    
    app.register_blueprint(facts.bp)

    return app
