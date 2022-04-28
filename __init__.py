from app import * 
from controller.user_controller import * 
from controller.home_controoler import *

if __name__ == "__main__":
	app.api.add_resource(Users,"/users")
	app.api.add_resource(main,"/")
	app.app.run(port=3333)