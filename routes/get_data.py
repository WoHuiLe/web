from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

class BaseParameters(BaseModel):
    data:str

class DataRequestParameters(BaseModel):
    name:str
    age:int
    address:List[str]
    

class GetDataRouter(APIRouter):
    def __init__(self, **kwargs):
        super().__init__(prefix="/Data")
        self.init_routes()
        
        
    def init_routes(self):
        self.add_api_route(path="/data", endpoint=self.get_data, methods=["GET"],summary=["Get Data test"])
        
    # def get_data(self,request:DataRequestParameters):
    def get_data(self):
        # name = request.args.get('name')
        # age = request.args.get('age')
        # address = request.args.get('address')
        print("get data:函数被调用lele")
        return {"data":"test data"}
        # return {"name":name,"age":age,"address":address}
        
    
        