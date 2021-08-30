from flask import Flask, render_template

from app.convert import MongoJSONEncoder, ObjectIdConverter
from app.server import bp

from . import db


# app constructor
def create_app():
    app = Flask(__name__, static_folder="client")

    # get config
    app.config.from_pyfile("config.cfg", silent=True)

    # init db
    db.init_app(app)
    with app.app_context():
        db.init_db()

    # set utils
    app.json_encoder = MongoJSONEncoder
    app.url_map.converters["objectid"] = ObjectIdConverter

    # register api
    app.register_blueprint(bp)

    # set template to render
    @app.route('/', defaults={"path": ""}, methods=["GET", "POST"])
    @app.route("/<path:path>")
    def index(path):
        return render_template("index.html")

    return app


def run_scheduler(_app):
    # import all jobs
    import app.jobs

    from app.scheduler import scheduler

    # start scheduler
    scheduler.app = _app
    scheduler.start()


if __name__ == "__main__":
    app = create_app()
    app.run()
