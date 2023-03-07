import json, pytz, datetime, re, secrets
from dateutil.parser import parse
from datetime import datetime


def parse_tags(text):
    allowed_tags = [
        'python', 'aws', 'docker', 'kubernetes', 'airflow', 'data', 'api', 
        'dbt', 'backend', 'sql', 'nosql', 'mongodb', 'postgres', 'data', 
        'devops', 'data science', 'data modeling', 'flask', 'REST', 'git', 
        'github', 'jupyter', 'hadoop', 'looker', 'hive', 'pig', 'spark', 
        'cassandra', 'redis', 'kafka', 'couchdb', 'heroku', 'azure', 
        'circleci', 'html', 'engineer', 'fastapi'
    ]


def get_date_time(source, date_str): 
    if source == 'grennhouse':
        date_time = parse(date_str)
        return date_time.strftime('%Y-%m-%d')
    else: 
        return (datetime.fromtimestamp(
            date_str/1000, 
            pytz.timezone('America/New_York')).strftime('%Y-%m-%d'))

def get_unix_timestamp(date_str): 
    # define unix timestamp
    unix_timestamp = int(datetime.strptime(date_str, "%Y-%m-%d").strftime("%s"))
    return round(unix_timestamp * 1000)

def is_remote(title, location, commitment, description): 
    return any('remote' is s for s in [title, location, commitment, description]) or any('anywhere' is s for s in [title, location]) or ('distributed' in location)

def is_not_internship(title):
    '''
    keep jobs with titles that include 'internal tools' or 'international', & etc
    reject jobs which include 'intern' or 'internship'
    '''
    return (('interna' in title or 'intern' not in title) and 'co-op' not in title)

def is_not_general_app(title):
    return ('?' not in title and 'dream job' not in title and 'general application' not in title)

def job_meets_requirements(title, location, commitment, description):
    return is_remote(title, location, commitment, description) and is_not_internship(title) and is_not_general_app(title)

def remove_non_alphanumeric_chars(from_string):
    pattern = re.compile('[\W_]+', re.UNICODE)
    return pattern.sub('', from_string)

def get_slug(from_list_of_strings): 
    token_hex = '-' + secrets.token_hex(2)
    if type(from_list_of_strings) == str: 
        return remove_non_alphanumeric_chars(from_list_of_strings).strip().replace(' ', '-').lower() + token_hex
    elif type(from_list_of_strings) == list: 
        return [remove_non_alphanumeric_chars(' '.join(from_list_of_strings)).strip().replace(' ', '-').lower() + token_hex]
    else:
        return False 

def normalize_category(category):
    with open ('jobs_categories.json') as f:
        cats = json.load(f)

    result = []
    for cat in cats:
        if category in cats[cat]:
            result.append(cat)
    
    if not result: 
        result.append('Other')
        cats['Other'].append(category)
        with open ('jobs_categories.json', 'w') as f:
            json.dump(cats, f)
    return result
    