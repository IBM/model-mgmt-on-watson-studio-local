# Trigger the feature extarction from wine dataset

import requests
import sys
import time

# Update the following values from deployed assets
AUTH_TOKEN = '<add authorization token>'
MODEL_SCORING_ENDPOINT = '<add model_scoring script endpoint>'
FEATURE_ENGINEERING_ENDPOINT = '<add feature_engineering script endpoint>'

args = sys.argv[1]

body = {"env": [], "args": [args]}

header = {'Content-Type': 'application/json',
          'Cache-Control': 'no-cache',
          'Authorization': AUTH_TOKEN}

url_ef = FEATURE_ENGINEERING_ENDPOINT + '/trigger'

print("Run feature engineering")
print("url_ef = ", url_ef)

extract_features = requests.post(url=url_ef,
                                 json=body,
                                 headers=header,
                                 verify=False)

response_ef = extract_features.json()
print(response_ef)

# Check the status of the extract features request

result_ef = response_ef["result"]

jobId_ef = str(result_ef['jobExecution']['runId'])
print("jobId_ef = ", jobId_ef)

status_ef = str(result_ef['jobExecution']['result'])
print("status_ef = ", status_ef)

body_sc = {}

url_sc1 = FEATURE_ENGINEERING_ENDPOINT + '/status/' + jobId_ef
print("url_sc1 = ", url_sc1)

print("Check status of feature engineering")

while status_ef == 'Waiting' or \
      status_ef == 'Running' or \
      status_ef == 'Pending':

    status_check1 = requests.post(url=url_sc1,
                                  json=body_sc,
                                  headers=header,
                                  verify=False)

    response_sc1 = status_check1.json()
    print("response_sc1 = ", response_sc1)

    result_sc1 = response_sc1["result"]

    status_ef = str(result_sc1["result"][0]["result"])
    print("status_ef = ", status_ef)

    time.sleep(3)

# Trigger the model scoring from extarcted features

if status_ef == 'Succeeded':
    url_ms = MODEL_SCORING_ENDPOINT + '/trigger'
    print("Run model scoring")

    model_scoring = requests.post(url=url_ms,
                                  json=body,
                                  headers=header,
                                  verify=False)

    response_ms = model_scoring.json()
    print("response_ms = ", response_ms)
else:
    print("Job Failed: feature status = " + status_ef)


# Check the status of the model scoring request

result_ms = response_ms["result"]

jobId_ms = str(result_ms['jobExecution']['runId'])
print("jobId_ms = ", jobId_ms)

status_ms = str(result_ms['jobExecution']['result'])
print("status_ms = ", status_ms)

url_sc2 = MODEL_SCORING_ENDPOINT + '/status/' + jobId_ms

print("Check status of model scoring")

while status_ms == 'Waiting' or \
      status_ms == 'Running' or \
      status_ms == 'Pending':

    status_check2 = requests.post(url=url_sc2,
                                  json=body_sc,
                                  headers=header,
                                  verify=False)

    response_sc2 = status_check2.json()
    print("response_sc2 = ", response_sc2)

    result_sc2 = response_sc2["result"]

    status_ms = str(result_sc2["result"][0]["result"])
    print("status_ms = ", status_ms)

    time.sleep(3)

# Final if check to verify the job completion

if status_ms == 'Succeeded':
    print("Job Complete")
else:
    print("Job Failed: scoring status = " + status_ms)
