import json
from io import StringIO
from application.models import Ad


def get():
    my_json = {
        "name": "Kalyan",
        "age": 25,
        "city": 'Delhi'
    }
    a = json.dumps(my_json)
    return (a)

# a = json.dumps(json.dumps({'lol':'kek'}))
# print(a)

print(get())


