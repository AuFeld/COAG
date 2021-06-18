
"""
Helper Functions
"""

def growjo_helper(entity) -> dict:
    return {
        "_id": str(entity["_id"]),
        "company_name": str(entity["company_name"]),
        "url": str(entity["url"]), 
        "city": str(entity["city"]),
        "country": str(entity["country"]), 
        "employess": str(entity["employees"]),
        "linkedin_url": str(entity["linkedin_url"]),
        "founded": str(entity["founded"]), 
        "industry": str(entity["industry"]),
        "growjo_ranking": str(entity["growjo_ranking"]), 
        "previous_ranking": str(entity["previous_ranking"]), 
        "estimated_revenues": str(entity["estimated_revenues"]),
        "job_openings": str(entity["job_openings"]),
        "keywords": str(entity["keywords"]),
        "lead_investors": str(entity["lead_investors"]),
        "accelerator": str(entity["accelerator"]),
        "btype": str(entity["btype"]), 
        "valuation": str(entity["valuation"]), 
        "total_funding": str(entity["total_funding"]),
        "product_url": str(entity["product_url"]),
        "indeed_url": str(entity["indeed_url"]),
        "growth_percentage": str(entity["growth_percentage"]),
    }

def indeed_helper(entity) -> dict:
    return {
        "id": int(entity["id"]),
        "jobtitle": str(entity["jobtitle"]),
        "company":str(entity["company"]),
        "location": str(entity["location"]),
        "summary": str(entity["summary"]),
        "requirements": str(entity["requirements"]),
        "description": str(entity["description"]),
        "state": str(entity["state"]),
        "city": str(entity["city"]),
        "dateposted": str(entity["dateposted"]),
        "schedule": str(entity["schedule"]),
        "salary": str(entity["salary"]),
        "role": str(entity["role"]),
        "focus": str(entity["focus"]),
    }
    
def linkedin_helper(entity) -> dict:
    return {
        "id": int(entity["id"]),
        "jobtitle": str(entity["jobtitle"]),
        "company":str(entity["company"]),
        "location": str(entity["location"]),
        "summary": str(entity["summary"]),
        "requirements": str(entity["requirements"]),
        "description": str(entity["description"]),
        "state": str(entity["state"]),
        "city": str(entity["city"]),
        "dateposted": str(entity["dateposted"]),
        "schedule": str(entity["schedule"]),
        "salary": str(entity["salary"]),
        "role": str(entity["role"]),
        "focus": str(entity["focus"]),
    }
