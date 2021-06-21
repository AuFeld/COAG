from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from pydantic.types import date

class IndeedModel(BaseModel): 
    id: str = Field(...)
    jobtitle: Optional[str] = Field(...)
    company: Optional[str] = Field(...)
    location: Optional[str] = Field(...)
    summary: Optional[str] = Field(...)
    requirements: Optional[str] = Field(...)
    description: Optional[str] = Field(...)
    state: Optional[str] = Field(...)
    city: Optional[str] = Field(...)
    dateposted: Optional[date] = Field(...)
    schedule: Optional[str] = Field(...)
    salary: Optional[str] = Field(...)
    role: Optional[str] = Field(...)
    focus: Optional[str] = Field(...)


    '''
    :orm_mode: 
    tells pydantic to read the data even if it's not a dict, 
    but an ORM model or any other arbitrary object w/ attributes
    '''
    class Config: 
        orm_mode = False,
        schema_extra = {
            "example": {
                "jobtitle": "Software Engineer",
                "company": "Hooli",
                "city": "Palo Alto",
                "state": "CA",
            }
        }

    def ResponseModel(data, message):
        return {
            "data": [data],
            "code": 200,
            "message": message,
        }
    
    def ErrorResponseModel(error, code, message):
        return{"error": error, "code": code, "message": message}