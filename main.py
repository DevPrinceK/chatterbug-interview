import json
import random
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from utils import PassswordGenerator, ExternalAPI

app = FastAPI()

# initial route - tests if server is alive and lists endpoints
@app.get("/")
async def ping():
    '''
    This is the initial route of the API. 
    It is used to test if the server is alive and lists the available endpoints.
    [METHOD: GET]
    [PARAMS: None]
    '''
    return JSONResponse({
        "message": "Welcome to the Coding Excersise for Junior Full Stack Developer at chatterbug.io!",
        "base_url": "127.0.0.1:8000",
        "endpoints": {
            "/": "Initial route. Lists available endpoints.",
            "/generate-password/": "Generate a random password.",
            "/placeholders/": "Get a random placeholder."
        }
    })

# route to generate a password
@app.post("/generate-password/")
async def generate_password(params: dict) -> JSONResponse:
    '''no p
    This route is used to generate a random password.
    [METHOD: GET]
    [PARAMS: allow_special_chars, use_passphrase, length]
    '''
    pg = PassswordGenerator()
    password = pg.generate(**params)
    # check if password generation was successful before returning
    if "error" in password:
        return JSONResponse( {
            "error": password["error"]
        })
    return JSONResponse({"password": password, "length": len(password)})

# route to get placeholders
@app.get("/placeholders/")
async def get_placeholders():
    '''
    This route is used to get placeholders for the frontend.
    [METHOD: GET]
    [PARAMS: None]
    '''
    ea = ExternalAPI(method="GET")
    response = ea.request(path=f"https://jsonplaceholder.typicode.com/posts/{random.randint(1, 10)}")
    # check if placeholders were fetched successfully before returning
    if "error" in response:
        return {
            "error": response["error"]
        }
    return JSONResponse(response)