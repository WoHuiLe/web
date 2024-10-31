from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

class BaseParameters(BaseModel):
    data:str
    
    
class GetDataRouter(APIRouter):
    def __init__(self, **kwargs):
        super().__init__(prefix="/Data")
        self.init_routes()
        
        
    def init_routes(self):
        self.add_api_route(path="/data", endpoint=self.get_data, methods=["GET"],summary=["Get Data test"])
        
    def get_data(self):
        print("get data:函数被调用")
        return {"data":"test data"}
        
    
        