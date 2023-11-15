# from flask import request
from flask import request
from api import app
from domain.actions.todo_actions import (
    get_todo,
    get_todos,
    add_todo,
    update_todo_status,
    update_todo_description,
    delete_todo,
)


@app.route("/")
def get_all():
    return get_todos()


@app.route("/<int:id>", methods=["GET"])
def get(id=0):
    return get_todo(id)


@app.route("/", methods=["POST"])
def add_data():
    todo = request.json["todo"]
    return add_todo(todo)


@app.route("/<int:id>", methods=["PUT"])
def update_data_status(id=0):
    return update_todo_status(id)


@app.route("/<int:id>/description", methods=["PUT"])
def update_data_description(id=0):
    todo = request.json["todo"]
    return update_todo_description(id, todo)


@app.route("/<int:id>", methods=["DELETE"])
def delete_data(id=0):
    return delete_todo(id)
