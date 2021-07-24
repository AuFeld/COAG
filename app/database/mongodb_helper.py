
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
        "state": str(entity["state"]),
        "current_employees": str(entity["current_employees"]),
        "last_employees": str(entity["last_employees"]),
        "linkedin_url": str(entity["linkedin_url"]),
        "founded": str(entity["founded"]), 
        "industry": str(entity["industry"]),
        "ranking": str(entity["ranking"]), 
        "previous_ranking": str(entity["previous_ranking"]), 
        "total_funding": str(entity["total_funding"]),
        "points": str(entity["points"]),
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
