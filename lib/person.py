#!/usr/bin/env python3



class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
    
    def __init__(self, name = "Miriam", job="Admin"):
        if isinstance(name, str) and 1 <= len(name) <= 25 and name != "":
            self._name = name.title()  
        else:
            print("Name must be string between 1 and 25 characters.")
        
        if job in self.APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
    
    def get_name(self):
        print("Retrieving name")
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 < len(name) <  25 and name != "":
            self._name = name.title()  
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        print("Retrieving job")
        return self._job 
    
    def set_job(self, job):
        if job in self.APPROVED_JOBS and isinstance(job, str):
            self._breed = job
            print(job)
        else:
            print("Job must be in list of approved jobs.")
    
    name = property(get_name, set_name)
    job = property(get_job, set_job)