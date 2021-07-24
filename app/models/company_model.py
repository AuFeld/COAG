from typing import Optional
from pydantic import BaseModel, Field, HttpUrl


class GrowjoSchema(BaseModel):
    _id: str = Field(...)
    company_name: Optional[str] = Field(...)
    url: Optional[HttpUrl] = Field(...)
    city: Optional[str] = Field(...)
    country: Optional[str] = Field(...)
    state: Optional[str] = Field(...)
    current_employess: Optional[str] = Field(...)
    last_employess: Optional[str] = Field(...)
    linkedin_url: Optional[HttpUrl] = Field(...) 
    founded: Optional[str] = Field(...)
    industry: Optional[str] = Field(...)
    ranking: Optional[str] = Field(...)
    previous_ranking: Optional[str] = Field(...) 
    total_funding: Optional[str] = Field(...)
    points: Optional[str] = Field(...)

    class Config: 
        schema_extra = {
            "example": {
                "company_name": "Initech",
                "url": "https://www.initech.com",
                "city": "San Francisco",
                "Country": "United States",
                "employees": "3",
            }
        }

class UpdateGrowjoModel(BaseModel):
    _id: str = Field(...)
    company_name: Optional[str] = Field(...)
    url: Optional[HttpUrl] = Field(...)
    city: Optional[str] = Field(...)
    country: Optional[str] = Field(...)
    state: Optional[str] = Field(...)
    current_employess: Optional[str] = Field(...)
    last_employess: Optional[str] = Field(...)
    linkedin_url: Optional[HttpUrl] = Field(...) 
    founded: Optional[str] = Field(...)
    industry: Optional[str] = Field(...)
    ranking: Optional[str] = Field(...)
    previous_ranking: Optional[str] = Field(...) 
    total_funding: Optional[str] = Field(...)
    points: Optional[str] = Field(...)


    class Config: 
        schema_extra = {
            "example": {
                "company_name": "Pied Piper",
                "url": "https://www.piedpiper.com",
                "city": "San Jose",
                "Country": "United States",
                "employees": "30",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200, 
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}