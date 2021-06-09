from typing import Optional
from pydantic import BaseModel, Field, HttpUrl


class GrowjoSchema(BaseModel):
    _id: str = Field(...)
    company_name: Optional[str] = Field(...)
    url: Optional[HttpUrl] = Field(...)
    city: Optional[str] = Field(...)
    country: Optional[str] = Field(...)
    employess: Optional[str] = Field(...)
    linkedin_url: Optional[HttpUrl] = Field(...) 
    founded: Optional[str] = Field(...)
    industry: Optional[str] = Field(...)
    growjo_ranking: Optional[str] = Field(...)
    previous_ranking: Optional[str] = Field(...) 
    estimated_revenues: Optional[str] = Field(...)
    job_openings: Optional[str] = Field(...)
    keywords: Optional[str] = Field(...)
    lead_investors: Optional[str] = Field(...)
    accelerator: Optional[str] = Field(...)
    btype: Optional[str] = Field(...)
    valuation: Optional[str] = Field(...)
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
    employess: Optional[str]
    linkedin_url: Optional[HttpUrl] 
    founded: Optional[str]
    industry: Optional[str]
    growjo_ranking: Optional[str]
    previous_ranking: Optional[str] 
    estimated_revenues: Optional[str]
    job_openings: Optional[str]
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