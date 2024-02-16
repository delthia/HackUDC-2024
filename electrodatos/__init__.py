from flask import Flask

app = Flask(__name__)

from electrodatos import routes
