from app import * 
from controller.user_controller import * 

if __name__ == "__main__":
	app.api.add_resource(Users,"/users")
	app.app.run(port=3333)