import random
import string
from random_word import RandomWords
import requests


class PassswordGenerator:
    '''
    This class is used to generate passwords.
    Requires a length parameter to be passed to the constructor.
    default length is 8.
    '''

    def __init__(self, length=8):
        self.length = length

    def generate(self, **kwargs):
        '''
        This method is the main password generating method.
        Optional parameters can be passed as keyword arguments.
        Example: allow_special_chars, use_passphrase, length, etc.
        '''
        allow_special_chars = kwargs.get("allow_special_chars", False)
        use_passphrase = kwargs.get("use_passphrase", False)
        length = kwargs.get("length", self.length)
        allowed_chars = string.ascii_letters + string.digits

        # ensure length is an integer greater than 8
        if not(isinstance(length, int)) or length < 8:
            return {"error": "Password length must be an integer greater than 8."}
            # raise ValueError("Password length must be an integer greater than 8.")
        
        if use_passphrase:
            rw = RandomWords()
            allowed_chars = ""
            for i in range(3):
                word = rw.get_random_word()
                allowed_chars += word.capitalize()
            return allowed_chars
            
        if allow_special_chars:
            allowed_chars += string.punctuation
        return "".join(random.choices(allowed_chars, k=length))
    
# NOTE: TESTS/TRIALS - PASSWORD GENERATOR
# pg = PassswordGenerator()
# print(pg.generate(allow_special_chars=False, length=10))
    
class ExternalAPI:
    '''
    This class is used to interact with external APIs.
    Requires an API URL to be passed to the constructor.
    Optional parameters can be passed as keyword arguments
    Example: headers, auth, body, etc.
    '''
    def __init__(self, method="GET"):
        self.method = method.upper()

    def request(self, **kwargs):
        '''
        This method is used to make generic requests to any API.
        '''
        method = kwargs.get("method", self.method).upper()
        if method == "GET":
            return self.get(**kwargs)
        elif method == "POST":
            return self.post(**kwargs)
        else:
            return {"error": "Invalid method."}

    def get(self, **kwargs):
        '''
        This method is used to make generic get requests to any API.
        '''
        path = kwargs.get("path", None)
        headers = kwargs.get("headers", {})
        auth = kwargs.get("auth", None)
        body = kwargs.get("body", None)
        # path url is required
        if path is None:
            return {"error": "Path not provided."}
        try:
            response = requests.get(path, headers=headers, auth=auth, data=body)
        except Exception as e:
            return {"error": str(e)}
        else:
            return response.json()


    def post(self, **kwargs):
        '''
        This method is used to make generic post requests to any API.
        '''
        path = kwargs.get("path", None)
        headers = kwargs.get("headers", {})
        auth = kwargs.get("auth", None)
        body = kwargs.get("body", None)
        # path url is required
        if path is None:
            return {"error": "Path not provided."}
        try:
            response = requests.post(path, headers=headers, auth=auth, data=body)
        except Exception as e:
            return {"error": str(e)}
        else:
            return response.json()


# NOTE: TESTS/TRIALS - EXTERNAL API
# ea = ExternalAPI()

# 1. JSON Placeholder API
# print(ea.get(path="https://jsonplaceholder.typicode.com/posts/5"))

# 2. THE MOVIE DB API
# url = "https://api.themoviedb.org/3/movie/changes?page=1"
# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZTUzMGQ3ZGY3ZmFkNGYzMWY4M2Q0Y2M4NjM2NTIzNiIsInN1YiI6IjYwNWRmOTEyZjNlMGRmMDA3MzkxNDViMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.e8nwm4dk5HMerwzFSRoY6oLcaIEoy-jMOk2LNLpXZw0"
# }
# print(ea.get(path=url, headers=headers))

# 3. RANDOM USER GENERATOR API
    # url = "https://randomuser.me/api/"
    # print(ea.get(path=url))

# 4. OPEN WEATHER MAP API
    # url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=1d1b3d6c9b6d5d7f8b4b5d7f8b4b5d7f"
    # print(ea.get(path=url))