from ..blueprints import index_bp


def init_app(app):
    app.register_blueprint(index_bp)
    return app
