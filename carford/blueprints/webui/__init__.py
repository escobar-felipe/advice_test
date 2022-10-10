from flask import Blueprint

from .views import index, owner_page

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/owner/<owner_id>", view_func=owner_page, endpoint="ownerview"
)

def init_app(app):
    app.register_blueprint(bp)
