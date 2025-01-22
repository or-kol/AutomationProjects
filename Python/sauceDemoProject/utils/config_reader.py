import configparser
import sys

class ConfigReader:

    @staticmethod
    def read_config(section, key):
        root_dir = sys.path[0]
        config = configparser.ConfigParser()
        config.read(root_dir + "/config.ini")

        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")

    @staticmethod
    def get_keys(section):
        root_dir = sys.path[0]
        config = configparser.ConfigParser()
        config.read(root_dir + "/config.ini")

        keys = config.options(section)

        return keys

    @staticmethod
    def get_values(section):
        root_dir = sys.path[0]
        config = configparser.ConfigParser(strict=True)
        config.read(root_dir + "/config.ini")

        keys = config.options(section)

        values = [config.get(section, key) for key in keys]

        return values