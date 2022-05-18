# coding=utf-8
"""
@File    : constant.py
@Time    : 2022/5/16 22:43
@Author  : haozhang45
@Email   : haozhang45@iflytek.com
@Software : PyCharm
@Description: 
"""
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root

CONFIG_FILE_PATH: str = os.path.join(ROOT_DIR, "..", "config.json")  # config file path
