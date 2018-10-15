import json
import os.path
import sys


def load_data(filepath, error):
    with open(filepath, 'rb') as file:
        try:
            return file.read()
        except ValueError:
            print(error)


def pretty_print_json(data_to_decode, error):
    try:
        decoded_json = json.loads(data_to_decode)
        return json.dumps(
            decoded_json,
            sort_keys=True,
            indent=4,
            ensure_ascii=False,
        )
    except ValueError:
        print(error)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        user_filepath = sys.argv[1]
        if os.path.exists(user_filepath):
            user_read_data = load_data(user_filepath, 'file does not reading')
            print(pretty_print_json(user_read_data, 'need json format'))
        else:
            print('need correct file path')
    else:
        print('need filename')
