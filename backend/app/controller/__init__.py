from .main import main
from .auth import auth
from .api import api
from .task import tasks
from .admin import admin
from .problem import problem

BLUEPRINTS = (
    (main, ''),
    (auth, '/auth'),
    (api, '/api'),
    (problem, '/problem'),
    (tasks, '/task'),
    (admin, '/admin'),
)

def config_blueprint(app):
    for blueprint, prefix in BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix = prefix)
