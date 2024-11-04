from fastapi import APIRouter,Path
from typing import List
from pydantic import BaseModel

class BaseParameters(BaseModel):
    data:str

class DataRequestParameters(BaseModel):
    name:str
    age:int
    address:List[str]
    
class Data(BaseModel):
    name:str
class GetDataRouter(APIRouter):
    def __init__(self, **kwargs):
        super().__init__(prefix="/Data")
        self.init_routes()
        
        
    def init_routes(self):
        # self.add_api_route(path="/data/{id}", endpoint=self.get_data, methods=["GET"],summary="Get Data test")
        self.add_api_route(path="/data", endpoint=self.get_data, methods=["POST"],tags=["data"])
        self.add_api_route(path="/test", endpoint=self.test_ui, methods=["GET"],tags=["test"])
        
    # def get_data(self,request:DataRequestParameters):
    # def get_data(self, id: str = Path(..., description="The ID of the item to get")):
    def get_data(self,data: Data):
        # name = request.args.get('name')
        # age = request.args.get('age')
        # address = request.args.get('address')
        # print("id:",id)
        print("get data:函数被调用le")
        print(data)
        return {"data":"test data","id":"aaa"}
        # return {"name":name,"age":age,"address":address}
    def test_ui(self):
        return {"data":"test data"}
         
    
        