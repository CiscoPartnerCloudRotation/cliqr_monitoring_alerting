import requests
import json
import ast
# -- Possible status values are JobRunning, JobFinished, JobStopped, JobError, NodeStarting, NodeReady, NodeTerminated --
# Testing:
# 1. Run test_server.py in the background
# 2. Job list endpoints: http://127.0.0.1:5000/v1/jobs
# 3. Test job endpoints: http://127.0.0.1:5000/v1/jobs/1768

def get_all_jobs():
    r = requests.get('http://127.0.0.1:5000/v1/jobs')
    return r.text

def get_job(jobId):
    print 'http://127.0.0.1:5000/v1/jobs/{0}'.format(jobId)
    r = requests.get('http://127.0.0.1:5000/v1/jobs/{0}'.format(jobId))
    return r.text

def eval_job_status(jobId):
    return NotImplementedError

def str_to_dict(text):
    # Used for debugging, since we don't have access to a cliqr appliance yet to verify output
    return ast.literal_eval(text)

if __name__ == "__main__":
    # Get all jobs currently running
    jobList = get_all_jobs()

    # Take this out when we're done debugging
    jobList = str_to_dict(jobList)

    # For every job in the list, get details and update status
    print jobList["jobs"]
    
    #for job in jobList["jobs"]:
    #    print job
    #jobList["jobs"][0]["id"]
    