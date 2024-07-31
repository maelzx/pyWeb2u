from flask import Blueprint, jsonify, render_template

item_bp = Blueprint('item', __name__)

@item_bp.route('/', methods=['GET'])
def get_items():
  items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
  return render_template('items.html', items=items)