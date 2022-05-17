# coding=utf-8
"""
@File    : yaml_reader.py
@Time    : 2022/5/16 22:41
@Author  : haozhang45
@Email   : haozhang45@iflytek.com
@Software : PyCharm
@Description: Read Yaml file to configration file
"""
import json
import yaml
from Source.constant import CONFIG_FILE_PATH


class YamlConfigureModel(object):
    """
    yaml configuration model, using dict map to model
    """

    # constructor
    def __init__(self, dict1):
        self.__dict__.update(dict1)


class YamlFileReader(object):
    yaml_model: YamlConfigureModel = None

    def __init__(self,
                 file_path: str):
        """
        open file path to read yaml
        :param file_path:
        """
        with open(file=file_path, mode='r', encoding='utf-8') as yaml_file:
            yaml_obj = yaml.load(yaml_file, Loader=yaml.FullLoader)
            self.yaml_model = dict2obj(dict_param=yaml_obj)

    def create_json(self) -> dict:
        """
        using the yaml configuration model to scheme
        :return:
        """
        ret: dict = {}
        get_property(self.yaml_model, ref_dict=ret)
        return ret


def dict2obj(dict_param: dict):
    """
    using `json.loads` method and passing `json.dumps`
    method and custom object hook as arguments
    :param dict_param
    :return:
    """
    return json.loads(json.dumps(dict_param), object_hook=YamlConfigureModel)


def get_property(model: object, ref_dict: dict):
    """
    handle nested model
    :param model:
    :param ref_dict: reference dict to change value
    :return:
    """
    # if there is `not required` property in model, it must be the first dat
    if "required" not in ref_dict:
        ref_dict["required"] = []
    if "properties" not in ref_dict:
        ref_dict["properties"] = {}
    if "type" not in ref_dict:
        # This is a bug to fix first type not confirm on the yaml
        ref_dict["type"] = 'object'
    for property_, value in vars(model).items():
        if hasattr(value, 'required') and value.required == 1:
            ref_dict["required"].append(property_)
        if value.j_type == 'object':
            ref_dict["properties"][property_] = {
                "type": value.j_type
            }
            if hasattr(value, 'j_value'):
                # judge is required
                get_property(model=value.j_value, ref_dict=ref_dict["properties"][property_])
        elif value.j_type == 'array':
            ref_dict["properties"][property_] = {
                "type": value.j_type,
                "items": {

                }
            }
            if hasattr(value, 'j_value'):
                # ref_dict[property_].append({})
                get_property(model=value.j_value, ref_dict=ref_dict["properties"][property_]["items"])
        else:
            ref_dict["properties"][property_] = {
                "type": value.j_type
            }
            check_number_property(value_info=value,
                                  ref_dict=ref_dict["properties"][property_])
            check_string_property(value_info=value,
                                  ref_dict=ref_dict["properties"][property_])
        if len(ref_dict["required"]) == 0:
            # 如果没有required就删除字段
            del ref_dict["required"]


def check_number_property(value_info: object,
                          ref_dict: dict):
    """
    Check the number property of maximum and minimum
    :param value_info:
    :param ref_dict:
    :return:
    """
    if value_info.j_type == 'integer' or value_info.j_type == 'number':
        if hasattr(value_info, 'min'):
            ref_dict['minimum'] = value_info.min
        if hasattr(value_info, 'max'):
            ref_dict['maximum'] = value_info.max
        if hasattr(value_info, 'range'):
            ref_dict['enum'] = value_info.range


def check_string_property(value_info: object,
                          ref_dict: dict):
    """
    Check the string property of contain in the enumeration
    :param value_info:
    :param ref_dict:
    :return:
    """
    if value_info.j_type == 'string':
        if hasattr(value_info, 'range'):
            ref_dict['enum'] = value_info.range
        if hasattr(value_info, 'min'):
            ref_dict['minLength'] = value_info.min
        if hasattr(value_info, 'max'):
            ref_dict['maxLength'] = value_info.max


def read_config() -> dict:
    """
    read config yaml
    :return:
    """
    yaml_reader: YamlFileReader = YamlFileReader(file_path=CONFIG_FILE_PATH)
    schema_dict: dict = yaml_reader.create_json()
    return schema_dict


if __name__ == '__main__':
    read_config()
