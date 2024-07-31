from flask import Blueprint, jsonify, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
  users = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]
  return render_template('users.html', users=users)