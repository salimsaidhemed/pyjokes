from app.helpers import Joke
class TestJoke:

    def test_canCallget_joke():
        joke = Joke()
        joke.get_joke()