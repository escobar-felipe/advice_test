from flask import Blueprint

from .views import index, vehicles

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/owner/<owner_id>", view_func=vehicles, endpoint="ownerview"
)


def init_app(app):
    app.register_blueprint(bp)
