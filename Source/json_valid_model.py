# coding=utf-8
"""
@File    : json_valid_model.py
@Time    : 2022/5/16 22:06
@Author  : haozhang45
@Email   : haozhang45@iflytek.com
@Software : PyCharm
@Description: This Object File is to package valid json
"""
import json
import os.path

import jsonschema

from Source.custom_error import JsonErrorType, JsonError
from json import loads

from Source.yaml_reader import read_config


class JsonValidModel(object):
    _file_name: str = ""

    def __init__(self,
                 file_name: str):
        """
        :param file_name: file position to the json
        """
        if not os.path.exists(file_name):
            raise JsonError
        self._file_name = file_name

    def load_json(self):
        """
        make sure json can generate
        :return:
        """
        try:
            with open(file=self._file_name,
                      mode='r',
                      encoding='utf-8') as json_file:
                json_str = json.load(json_file)
        except Exception as e:
            raise JsonError(error_type=JsonErrorType.GenerateError)

    def validate_scheme(self):
        """
        validate json by schema
        :return:
        """
        with open(file=self._file_name,
                  mode='r',
                  encoding='utf-8') as json_file:
            json_str = json.load(json_file)
            ret = read_config()
            validator = jsonschema.Draft7Validator(ret)
            errors = sorted(validator.iter_errors(json_str), key=str)
            if len(list(errors)) > 0:
                raise JsonError(error_type=JsonErrorType.JsonSchemaError,
                                error_valid_lst=errors)

