from app import *
from db import *
from uuid import uuid4

class Users(Resource, Users_db):

	def __init__(self):
		Resource.__init__(self)
		Users_db.__init__(self)
		super().__init__()

	def get(self):
		data = self.get_database()
		return { "users": data },200

	def post(self):
		parser = reqparse.RequestParser()
		print(parser)
		parser.add_argument("name", required=True)
		parser.add_argument("city", required=True)
		parser.add_argument("locations")
		args = parser.parse_args()
		data = self.set_newUserInDataBase(args)
		return {"user":data}, 200
	
	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument("userId",required=True )
		parser.add_argument("location",required=True )
		args = parser.parse_args()
		data = self.update_User(args)
		print(data)
		return 200