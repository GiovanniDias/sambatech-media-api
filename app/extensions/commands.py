import click
from flask.cli import with_appcontext
from .database import db


def create_db():
    db.create_all()


def drop_db():
    db.drop_all()


@click.command('create-db')
@with_appcontext
def create_db_command():
    click.echo('Loading models...')
    try:
        create_db()
        click.echo('Database successfully initialized!')
    except BaseException as e:
        click.echo(e)


@click.command('drop-db')
@with_appcontext
def drop_db_command():
    click.echo('Dropping all tables...')
    try:
        drop_db()
        click.echo('Tables successfully dropped!')
    except BaseException as e:
        click.echo(e)


@click.command('recreate-db')
@with_appcontext
def recreate_db_command():
    click.echo('Dropping all tables...')
    try:
        drop_db()
        click.echo('Tables successfully dropped!')
    except BaseException as e:
        click.echo(e)
    
    click.echo('Loading models...')
    try:
        create_db()
        click.echo('Database successfully initialized!')
    except BaseException as e:
        click.echo(e)


def init_app(app):
    app.cli.add_command(create_db_command)
    app.cli.add_command(drop_db_command)
    app.cli.add_command(recreate_db_command)
