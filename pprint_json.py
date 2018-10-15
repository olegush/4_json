import json
import os.path
import sys


def load_data(filepath):
    with open(filepath, 'rb') as file:
        return json.loads(file.read())


def pretty_print_json(decoded_json):
    return json.dumps(
        decoded_json,
        sort_keys=True,
        indent=4,
        ensure_ascii=False,
    )


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('need filename')
    else:
        user_filepath = sys.argv[1]
        if not os.path.exists(user_filepath):
            exit('need correct file path')
        else:
            loaded_json = load_data(user_filepath)
            if not loaded_json:
                exit('can not load the json')
            else:
                print(pretty_print_json(loaded_json))
