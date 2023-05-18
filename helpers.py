import configparser

class Helper:
    def get_config_value(self,key):
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config["app"][key]
