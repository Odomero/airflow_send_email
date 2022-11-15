import os
import json
import requests
from send_mail import send_email
from dotenv import load_dotenv

load_dotenv()

def get_jobs(job_tag,location):
    '''
    Extract jobs from Google Jobs api on RapidAPI.

    Input parameters:
        job_tag - job search keyword e.g "software developer"
        location - job location e.g "Germany"

    Output: 
        Returns a json object of job information
    '''

    url = "https://linkedin-jobs-search.p.rapidapi.com/"

    payload = {
        "search_terms": job_tag,
        "location": location,
        "page": "1"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv("RapidAPI-Key"),
        "X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    if response.status_code == 200: 
        data = response.json()    
        sender = os.getenv("SENDER_EMAIL")
        receiver = os.getenv("RECEIVER_EMAIL")
        password = os.getenv("APP_PASSWORD")
        sub = "Subject: Remote Python Jobs!\n\n"
        message = "Found some cool Python jobs!\n\n"
        
        for job in data:
            job_headers = [
                'job_title', 'company_name',  'linkedin_job_url_cleaned', 
                'linkedin_company_url_cleaned', 'job_location', 'posted_date'
                ]
            job_data = {job_header: job_info for job_header, job_info in job.items() if job_header in job_headers}

            message += f"{json.dumps(job_data)}\n\n"

        send_email(sender, receiver, password, sub, message)
        return "Job updates sent!!!"
    else:
        return response
    
print(get_jobs("python", "Poland"))