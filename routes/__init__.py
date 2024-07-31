from .user_routes import user_bp
from .item_routes import item_bp
from .misc_routes import misc_bp

def init_routes(app):
  app.register_blueprint(user_bp, url_prefix='/api/users')
  app.register_blueprint(item_bp, url_prefix='/api/items')
  app.register_blueprint(misc_bp)