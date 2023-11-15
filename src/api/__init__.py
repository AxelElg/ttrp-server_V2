from flask import Flask


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return "404 not found", 404


# Import routes
from api.routes import todo
