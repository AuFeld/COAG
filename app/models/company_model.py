from typing import Optional
from pydantic import BaseModel, Field, HttpUrl


class GrowjoSchema(BaseModel):
    _id: str = Field(...)
    company_name: Optional[str] = Field(...)
    url: Optional[HttpUrl] = Field(...)
    city: Optional[str] = Field(...)
    country: Optional[str] = Field(...)
    employess: Optional[int] = Field(...)
    linkedin_url: Optional[HttpUrl] = Field(...) 
    founded: Optional[int] = Field(...)
    industry: Optional[str] = Field(...)
    growjo_ranking: Optional[int] = Field(...)
    previous_ranking: Optional[int] = Field(...) 
    estimated_revenues: Optional[int] = Field(...)
    job_openings: Optional[int] = Field(...)
    keywords: Optional[str] = Field(...)
    lead_investors: Optional[str] = Field(...)
    accelerator: Optional[str] = Field(...)
    btype: Optional[str] = Field(...)
    valuation: Optional[int] = Field(...)
    total_funding: Optional[str] = Field(...)
    product_url: Optional[HttpUrl] = Field(...)
    indeed_url: Optional[HttpUrl] = Field(...)
    growth_percentage: Optional[str] = Field(...)

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
    _id : Optional[str]
    company_name: Optional[str]
    url: Optional[HttpUrl]
    city: Optional[str]
    country: Optional[str]
    employess: Optional[int]
    linkedin_url: Optional[HttpUrl] 
    founded: Optional[int]
    industry: Optional[str]
    growjo_ranking: Optional[int]
    previous_ranking: Optional[int] 
    estimated_revenues: Optional[int]
    job_openings: Optional[int]
    keywords: Optional[str]
    lead_investors: Optional[str]
    accelerator: Optional[str]
    btype: Optional[str]
    valuation: Optional[str]
    total_funding: Optional[str]
    product_url: Optional[HttpUrl]
    indeed_url: Optional[HttpUrl]
    growth_percentage: Optional[str]

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