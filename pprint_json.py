import json
import os.path
import sys


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            try:
                data_list = json.loads(file.read())
                return data_list
            except ValueError:
                return "json data does not exists or incorrect"
    else:
        return None


def pretty_print_json(unformatted_json):
    return json.dumps(
        unformatted_json,
        sort_keys=True,
        indent=4,
        ensure_ascii=False,
    )


if __name__ == '__main__':
    user_unformatted_data_list = load_data(sys.argv[1])
    print(pretty_print_json(user_unformatted_data_list))
