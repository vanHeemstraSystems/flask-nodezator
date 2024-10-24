flask-nodezator
# Flask Nodezator

> A Python Flask application with Nodezator

Open this URL with ```https://github.dev/``` instead of ```https://github.com/``` to use the Visual Studio Code web-based IDE.

# Executive Summary

Run this application as follows:

1) Enter ```flask_app``` directory: ```$ cd flask_app```
2) If non-existent, create a virtual environment inside the ```flask_app``` directory: ```$ python3 -m venv .venv``` (macOS: ```$ virtualenv .venv```)

In case of the following, follow its advice:

The virtual environment was not created successfully because ensurepip is not
available.  

On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    sudo apt-get update
    sudo apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

On macOS see https://sourabhbajaj.com/mac-setup/Python/virtualenv.html


3) Start the virtual environment and enter: ```. .venv/bin/activate``` (macOS: ```source .venv/bin/activate```)
4) Run ```$ pip install -r requirements.txt```
5) Run: ```$ cd app``` then ```$ npm install``` finally ```$ cd ..```
6) Set the Flask App to app directory: ```(.venv) $ export FLASK_APP=app```
7) Set the Flask Environment to True for development: ```(.venv) $ export FLASK_DEBUG=True```
8) Set the SQLAlchemy Database URI: ```(.venv) $ export SQLALCHEMY_DATABASE_URI=...```, default is ```sqlite:///app.db```
9) Set SQLAlchemy Track Modifications: ```(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True```
10) Set Secret Key: ```(.venv) $ export SECRET_KEY=********```
11) Run the flask app: ~```(.venv) $ flask run```~ ```(.venv) $ python3 run.py```
12) Open the web interface as prompted
13) Use ```CTRL+c``` to exit the web server.
14) Alternatively run the flask command line interface: ```(.venv) $ flask shell```
15) Execute any flask commands: >>>
16) Use ```exit()``` to exit from the command line interface.

In general, you can take the following steps to manage your database migrations as you develop your Flask applications:

1) Modify the database models.

2) If no ```migrations``` directory yet exists in the ```flask_app``` directory, run ``` (.venv) flask_app $ flask db init```.

3) Generate a migration script with the ```flask db migrate -m "some comment"``` command. If there have been no changes since last migration, you will be prompted with ```No changes in schema detected.```. Hence, you can repeat this command without fear.

4) Review the generated migration script and correct it if necessary.

5) Apply the changes to the database with the ```flask db upgrade``` command.

6) To restore a previous database version, use the ```flask db downgrade``` command.

## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)
