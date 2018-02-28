from requests_oauthlib import OAuth1
from datetime import datetime, date
import requests
import json
import os

schoology_app_key = os.environ['SCHOOLOGYKEY']
schoology_app_secret = os.environ['SCHOOLOGYSECRET']
schoology_user_id = os.environ['SCHOOLOGYID']
section_id = '1141467326'

class main():

    def __init__(self):
        self.auth = OAuth1(schoology_app_key, schoology_app_secret, '', '')

        # Right now I don't have the access to look at attendance.
        # Once I become a teacher, I think I will be able to access
        # the attendance of my virtual class.
        self.attendance_check()

    def attendance_check(self):
        print("Checking attendance")
        try:
            attendance = requests.get(f'https://api.schoology.com/v1/sections/{section_id}/attendance', auth=self.auth).json()
            print(attendance)
        except:
            print("You don't have the right credentials")

    # Fetch all of the user's courses
    def index_courses(self):
        print("Indexing course ids to names...")
        courses = requests.get(f'https://api.schoology.com/v1/users/{schoology_user_id}/sections/', auth=self.auth).json()
        print(courses)
        courses = courses['section']
        temp = {}
        for course in courses:
            temp[course['id']] = course['course_title']
        self.courses = temp
        print(temp)
        query = requests.get(f'https://api.schoology.com/v1/users/{schoology_user_id}/grades', auth=self.auth).json()
        query = query['section']
        for course in query:
            pass
            #print(course)
        query = requests.get(f'https://api.schoology.com/v1/sections/1141467326/updates', auth=self.auth).json()
        print(query)

    def get_id(self):
        print("Getting User ID")
        user_information = requests.get(f'https://api.schoology.com/v1/users/?start=1500&limit=1000', auth=self.auth).json()
        print(user_information)
        with open('users.json','w') as filewrite:
            filewrite.write(json.dumps(user_information))
            filewrite.close()

if __name__ == "__main__":
    main()
