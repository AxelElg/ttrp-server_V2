from domain.db import read_data, write_data

db = "todos"


def get_todos():
    return read_data(db)


def get_todo(id):
    data = read_data(db)
    for t in data:
        if t["id"] == id:
            return t


def add_todo(todo):
    data = read_data(db)
    existing_ids = [t["id"] for t in data]
    i = 0

    while True:
        if i in existing_ids:
            i += 1
        else:
            break

    data.append({"id": i, "todo": todo, "done": False})

    write_data(db, data)
    return data


def update_todo_status(id):
    data = read_data(db)

    for t in data:
        if t["id"] == id:
            t["done"] = not t["done"]
            break

    write_data(db, data)
    return data


def update_todo_description(id, new_description):
    data = read_data(db)

    for t in data:
        if t["id"] == id:
            t["todo"] = new_description
            break

    write_data(db, data)
    return data


def delete_todo(id):
    data = read_data(db)

    for i, t in enumerate(data):
        if t["id"] == id:
            del data[i]
            break

    write_data(db, data)
    return data
