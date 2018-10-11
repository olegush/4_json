import json
import os.path


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            try:
                data_json = json.loads(file.read())
            except ValueError:
                return "json data does not exists or incorrect"
            else:
                return data_json
    else:
        return "file does not exists"


def pretty_print_json(unformatted_json):
    return json.dumps(unformatted_json,
                      sort_keys=True, indent=4, ensure_ascii=False,)


if __name__ == '__main__':
    user_unformatted_json = load_data('data.json')
    print(pretty_print_json(user_unformatted_json))
