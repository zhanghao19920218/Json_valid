# coding=utf-8
"""
@File    : file_io.py
@Time    : 2022/5/18 22:52
@Author  : haozhang45
@Email   : haozhang45@iflytek.com
@Software : PyCharm
@Description:  The file to write the json error
"""
from typing import List


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
