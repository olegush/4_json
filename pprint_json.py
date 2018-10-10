import json


def load_data(filepath):
    with open(filepath, 'rb') as file:
        data_json = json.loads(file.read())
    return data_json


def pretty_print_json(user_data):
    return json.dumps(user_data, sort_keys=True, indent=4)


if __name__ == '__main__':
    user_data_obj = load_data('data.json')
    print(pretty_print_json(user_data_obj))
