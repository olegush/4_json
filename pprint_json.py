import json
import os.path
import sys


def load_data(filepath):
    with open(filepath, 'rb') as file:
        try:
            decoded_json = json.loads(file.read())
            return decoded_json
        except ValueError:
            pass


def pretty_print_json(decoded_json):
    return json.dumps(
        decoded_json,
        sort_keys=True,
        indent=4,
        ensure_ascii=False,
    )


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if os.path.exists(filepath):
            user_decoded_json = load_data(filepath)
            print(pretty_print_json(user_decoded_json))
