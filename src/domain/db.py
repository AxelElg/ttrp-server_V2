import json


def read_data(db):
    with open("db/%s.json" % (db), encoding="utf-8") as todos:
        return json.load(todos)


def write_data(db, data):
    with open("db/%s.json" % (db), mode="w+", encoding="utf-8") as todos:
        json.dump(data, todos, indent=2)
