import sys

from Source.custom_error import JsonError
from Source.json_valid_model import JsonValidModel

if __name__ == '__main__':
    if len(sys.argv) == 2:
        json_file = sys.argv[1]
        try:
            model = JsonValidModel(file_name=json_file)
            model.load_json()
            model.validate_scheme()
            print("JSON检验正常")
        except JsonError as json_error:
            print(json_error.to_string())
    else:
        print("请输入路径")