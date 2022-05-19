# coding=utf-8
"""
@File    : file_io.py
@Time    : 2022/5/18 22:52
@Author  : haozhang45
@Email   : haozhang45@iflytek.com
@Software : PyCharm
@Description:  The file to write the json error
"""
import os
from typing import List, Tuple


def write_log_into_files(log_file_name: str,
                         log_lines: List[str]):
    """
    write log information to files
    :param log_file_name:
    :param log_lines
    :return:
    """
    with open(file=log_file_name,
              mode='wt',
              encoding='utf-8') as write_file:
        for line in log_lines:
            write_file.write(line)


def read_files_from_path(path_dir: str) -> Tuple[List[str], List[str]]:
    """
    read files from path
    :param path_dir:
    :return:
    """
    ret: List[str] = []
    log_files: List[str] = []
    for root, dirs, files in os.walk(path_dir):
        # filter not json files
        json_files: List[str] = list(filter(lambda file_name: file_name.endswith("json"), files))
        # concat the parent directory and file_name
        ret: List[str] = list(map(lambda file_name: os.path.join(root, file_name), json_files))
        # filter result with log
        log_files: List[str] = list(map(lambda file_name: file_name.replace(".json", ".txt"), json_files))
    return ret, log_files


if __name__ == '__main__':
    print(read_files_from_path(path_dir='../testcase'))