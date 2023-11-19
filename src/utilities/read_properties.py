"""
To read the config.ini file, we first to need to import configparser package
1. create an object of RawConfigParser and read the config.ini file
2. Then create a class, and create three static methods
3. with the help of get function, pass the section (i.e. common info), and option (i.e. baseURL)
and return the value
"""

import configparser

config = configparser.RawConfigParser()
config.read("src/Configuration/config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get("common info", "baseURL")

    @staticmethod
    def get_username():
        return config.get("common info", "email")

    @staticmethod
    def get_password():
        return config.get("common info", "password")