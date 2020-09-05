def init_app(app):
    @app.route('/')
    def index():
        return 'This is a sample of SambaTech Media API'
