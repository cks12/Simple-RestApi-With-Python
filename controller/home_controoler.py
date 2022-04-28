from app import * 

class main(Resource):
    def get(self):
        return {"I'm a live": True},200