from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<string:pet_name>')
def show_pet(pet_name):
    pet = next((item for item in pets if item["pet_name"] == pet_name), None)
    if pet is not None:
        return render_template('show.html', pet=pet)
    else:
        return "Pet not found", 404

