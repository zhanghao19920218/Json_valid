import os
import sys

from Source.custom_error import JsonError
from Source.file_io import write_log_into_files, read_files_from_path
from Source.json_valid_model import JsonValidModel


def handle_one_json(file_json: str,
                    file_log: str):
    """
    handle json, write log to text
    :param file_json:
    :param file_log:
    :return:
    """
    try:
        model = JsonValidModel(file_name=file_json)
        model.load_json()
        model.validate_scheme()
        print("JSON检验正常")
    except JsonError as json_error:
        write_log_into_files(log_file_name=file_log,
                             log_lines=[json_error.to_total(),
                                        json_error.to_string()])
        print(json_error.to_total())


def write_files_to_log_out(json_dir: str,
                           output_dir: str):
    """

    :param json_dir:
    :param output_dir:
    :return:
    """
    input_files, log_files_names = read_files_from_path(path_dir=json_dir)
    for index, input_file in enumerate(input_files):
        handle_one_json(file_json=input_file,
                        file_log=os.path.join(output_dir, log_files_names[index]))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        json_dirname = sys.argv[1]
        log_dir = sys.argv[2]
        write_files_to_log_out(
            json_dir=json_dirname,
            output_dir=log_dir
        )
    else:
        print("1.请输入路径\n 2. 请输入输出日志文件夹")
