import os

import click
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from application import create_app, db

app = create_app("production")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(32)
migrate = Migrate(app, db)
cli = FlaskGroup(create_app=lambda: app)


@cli.command()
@click.option("--host", default="127.0.0.1")
@click.option("--port", default=7345, type=int)
def runserver(host, port):
    app.run(host=host, port=port)


if __name__ == "__main__":
    cli()
