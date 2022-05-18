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
from typing import Any


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

    _error_valid_lst = None


class JsonError(BaseError):
    """
    Handle the error json message
    """

    _required_count: int = 0

    _no_in_range: int = 0

    _type_in_count: int = 0

    _over_max_count: int = 0

    _below_min_count: int = 0

    _string_min_len: int = 0

    def __init__(self,
                 error_type: JsonErrorType,
                 error_valid_lst: Any = None):
        """
        error type confirm
        :param error_type:
        :param error_valid_lst: 错误信息列表
        """
        self._error_type = error_type
        self._error_valid_lst = error_valid_lst
        self.count_errors_type()

    def to_string(self) -> str:
        ret = ""
        if self._error_type == JsonErrorType.GenerateError:
            return JsonErrorType.GenerateError.value
        elif self._error_type == JsonErrorType.FileNotFoundError:
            return "JSON File Not Found"
        else:
            for error in self._error_valid_lst:
                ret += f"错误位置:{list(error.absolute_path)}\n错误信息:{error.message}\n\n"
        return ret

    def count_errors_type(self) :
        """
        Counting the errors type
        :return:
        """
        for error in self._error_valid_lst:
            if error.validator == 'required':
                self._required_count += 1
            elif error.validator == 'enum':
                self._no_in_range += 1
            elif error.validator == 'type':
                self._type_in_count += 1
            elif error.validator == 'maximum':
                self._over_max_count += 1
            elif error.validator == 'minimum':
                self._below_min_count += 1
            elif error.validator == 'minLength':
                self._string_min_len += 1
            else:
                print(f"元素{error.validator}")

    def to_total(self) -> str:
        """
        calculate the result
        :return:
        """
        ret: str = ""
        if self._required_count != 0:
            ret += f"必选元素丢失:{self._required_count}\t"
        if self._no_in_range != 0:
            ret += f"不在枚举值: {self._no_in_range}\t"
        if self._type_in_count != 0:
            ret += f"类型错误: {self._type_in_count}\t"
        if self._over_max_count != 0:
            ret += f"高于最大值: {self._over_max_count}\t"
        if self._below_min_count != 0:
            ret += f"低于最小值: {self._below_min_count}\t"
        if self._string_min_len != 0:
            ret += f"字符串值为空: {self._string_min_len}\n"
        return ret
