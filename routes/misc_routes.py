from flask import Blueprint, render_template

misc_bp = Blueprint('misc', __name__)

@misc_bp.route('/about', methods=['GET'])
def about():
  return render_template('about.html')

@misc_bp.route('/contact', methods=['GET'])
def contact():
  return render_template('contact.html')