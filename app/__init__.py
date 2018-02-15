from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'firsttime'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '22be630b8e69fc'
app.config['MAIL_PASSWORD'] = 'a49752908b48ef'

mail = Mail(app)
from app import views