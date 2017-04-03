from flask import Flask
import time

app = Flask(__name__)
app.config.from_object('config')



from app import views
