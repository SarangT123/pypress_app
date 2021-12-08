from flask.cli import with_appcontext
from website import app, db, Admin_users, bcrypt, User
import click


@click.command(name='admin')
@click.argument('id')
@click.argument('access')
@with_appcontext
def admin(id, access):
    db.session.add(Admin_users(user_id=id, access=access))
    db.session.commit()


@click.command(name='setup')
@with_appcontext
def setup():
    print("Please do not abort this process")
    db.create_all()
    username = input(
        "Enter a username to use as admin (atleast 3 characters) : ")
    password = input(
        "Enter a password to use for admin (atleast 8 characters): ")
    password = bcrypt.generate_password_hash(password)
    db.session.add(User(username=username, password=password))
    db.session.add(Admin_users(user_id=1, access=0))
    db.session.commit()
    print("Setup complete do 'flask run' to run the server login with your username and password '/login' and go to '/admin' to access the administation panel")


# add command function to cli commands
app.cli.add_command(setup)
app.cli.add_command(admin)
