# coding=utf-8
"""
@File    : custom_error.py
@Time    : 2022/5/16 22:14
@Author  : haozhang45
@Email   : haozhang45@iflytek.com
@Software : PyCharm
@Description: JSON Error to handle message
"""
from enum import Enum
from typing import List
from jsonschema.exceptions import ValidationError


class JsonErrorType(Enum):
    """
    Error Type to Json
    """
    GenerateError = "This is not a json"

    JsonSchemaError = "Json Schema Error"

    FileNotFoundError = "File Not Found Error"


class BaseError(Exception):
    """
    Base object to handle error
    """
    _error_type: JsonErrorType = JsonErrorType.GenerateError

    _error_valid_lst: List[ValidationError] = []


class JsonError(BaseError):
    """
    Handle the error json message
    """

    def __init__(self,
                 error_type: JsonErrorType,
                 error_valid_lst: List[ValidationError] = []):
        """
        error type confirm
        :param error_type:
        :param error_valid_lst: 错误信息列表
        """
        self._error_type = error_type
        self._error_valid_lst = error_valid_lst

    def to_string(self) -> str:
        ret = ""
        if self._error_type == JsonErrorType.GenerateError:
            return JsonErrorType.GenerateError.value
        elif self._error_type == JsonErrorType.FileNotFoundError:
            return "JSON File Not Found"
        else:
            for error in self._error_valid_lst:
                ret += f"错误位置:{list(error.absolute_path)}\n错误信息:{error.message}\n"
        return ret
