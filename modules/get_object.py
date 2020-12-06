import json

def get_json(path):
    object_file = open(path)
    object_read = object_file.read() #<str>
    object_file.close()
    return json.loads(object_read) #<list>

