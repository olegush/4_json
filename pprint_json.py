import json
import os.path
import sys


def load_data(filepath, error):
    with open(filepath, 'rb') as file:
        try:
            read_data = file.read()
            return read_data
        except ValueError:
            print(error)


def decode_json(data_to_decode, error):
        try:
            decoded_json = json.loads(data_to_decode)
            return decoded_json
        except ValueError:
            print(error)


def pretty_print_json(decoded_json):
    return json.dumps(
        decoded_json,
        sort_keys=True,
        indent=4,
        ensure_ascii=False,
    )


if __name__ == '__main__':
    if len(sys.argv) == 2:
        user_filepath = sys.argv[1]
        if os.path.exists(user_filepath):
            user_read_data = load_data(user_filepath, 'need json format')
            user_decoded_json = decode_json(user_read_data, 'need json format')
            print(pretty_print_json(user_decoded_json))
        else:
            print('need correct file path')
    else:
        print('need filename')
