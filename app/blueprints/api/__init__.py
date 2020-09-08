from .media import bp as media_bp


def init_app(app):
    app.register_blueprint(media_bp)
    
    # api root
    @app.route('/')
    def index():
        return 'This is a sample of SambaTech Media API'
