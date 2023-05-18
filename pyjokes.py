from helpers import Helper
import requests
import cowsay
class Joke:
    def get_jokes(self,keyword=None):
        helper = Helper()
        url = helper.get_config_value("api_url")
        accept = helper.get_config_value("accept_header")
        headers = {
            "accept": accept
        }
        
        response = requests.get(url,headers=headers)
        data = response.json()
        return data

if __name__=="__main__":
    joke = Joke()
    data = joke.get_jokes()
    cowsay.cow("{}".format(data["joke"]))