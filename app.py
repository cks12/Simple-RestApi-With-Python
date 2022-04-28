from flask import Flask
from flask_restful import Resource, Api, reqparse
from functools import wraps
import asyncio

class Extensions():
    def __init__(self) -> None:
        pass
    def async_action(self, f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            return asyncio.run(f(*args, **kwargs))
        return wrapped

class server (Extensions):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        super().__init__()

app = server()