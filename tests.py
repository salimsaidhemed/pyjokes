from pyjokes import Joke
from helpers import Helper
class Test_jokes:
    def test_joke_class_defined(self):
        joke = Joke()
        assert joke != None
    
    def test_joke_is_not_none(self):
        joke = Joke()
        response = joke.get_jokes()
        assert response != None
    
    def test_get_joke(self):
        joke = Joke()
        response = joke.get_jokes()
        assert response["status"] == 200

class Test_helpers:
    def test_helper_class_defined(self):
        helper = Helper()
        assert helper != None

    def test_config_value_is_not_none(self):
        helper = Helper()
        key = "api_url"
        assert helper.get_config_value(key) != None
    
    def test_get_config_value(self):
        helper = Helper()
        key = "api_url"
        value = "https://icanhazdadjoke.com/"
        assert helper.get_config_value(key) == value