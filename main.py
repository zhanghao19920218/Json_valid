import sys

from Source.custom_error import JsonError
from Source.file_io import write_log_into_files
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
            write_log_into_files(log_file_name='log_demo.txt',
                                 log_lines=[json_error.to_total(),
                                            json_error.to_string()])
            # print(json_error.to_string())
            print(json_error.to_total())
    else:
        print("请输入路径")