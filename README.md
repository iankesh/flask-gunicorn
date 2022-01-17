# flask-gunicorn

### Pre-Requisites
sudo apt update

sudo apt install software-properties-common

sudo apt install python3-pip

sudo pip3 install flask

sudo pip3 install gunicorn

### Flask:
export FLASK_APP="app.main:create_app"

flask run

### Gunicorn:
gunicorn -w 4 "app.main:create_app(testing=True)"

Live edit: gunicorn -w 4 --reload "app.main:create_app(testing=True)"

set port: gunicorn -w 4 --reload -b localhost:5000 "app.main:create_app(testing=True)"