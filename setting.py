"""
Настройки всей системы


"""
from configparser import ConfigParser
import os


conf = ConfigParser()
conf.read(f'{os.getcwd()}/setting.ini')