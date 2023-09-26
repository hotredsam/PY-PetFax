from flask import Blueprint, render_template, request

bp = Blueprint('facts', __name__, url_prefix="/facts")

@bp.route('/new', methods=['GET'])
def new_fact():
    return render_template('facts.html')