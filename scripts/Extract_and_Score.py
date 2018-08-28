### Trigger the feature extarction from wine dataset

import requests
import sys

args = sys.argv[1]

body = {"env":[],"args":[args]} 
body

header = {'Content-Type': 'application/json','Cache-Control': 'no-cache','Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZpc2hudSIsInBhY2thZ2VOYW1lIjoicGNhLW1vZGVsIiwicGFja2FnZVJvdXRlIjoicGNhIiwiaWF0IjoxNTI5OTE1OTkwfQ.kcOwXMU9NngHZLLPOa3J4NeQUSFia5zEbIND_YdzN-8KVGMLtURR725rZQL8KPktw1iWQwc9JlKEiKao58_DJIuZb01ekKZExD-qBozsSpjvalQaKKMA2QaI42zgeMSCyuU6zAzA4AEXFjyOoulEsZ0zBCOrZocIyLLDuLIClRSVrf_lZFsbx3roKhODqcLzeGcexN-7_HcXCotGaWsEvASkpq3ivFC4a3F3SqZ7w0cXFMAh9RrK5UPZNb4aD_0AcSed1WcddGWeBxz8JgZvOExQ5IHsukhb1bsCWa1wFSV8C6oxZb4Sb71fqHD9HDRrF4LxB-7FyLpdcvF66dm-zg'}

url_ef = 'https://hca.datascienceelite.com/djob/v1/pca/extractfeatures/trigger'

extract_features = requests.post(url=url_ef,json=body,headers=header,verify=False)

response_ef = extract_features.json()
print response_ef


### Check the status of the extract features request

result_ef = response_ef["result"]

jobId_ef = str(result_ef['jobExecution']['runId'])
print jobId_ef

status_ef = str(result_ef['jobExecution']['result'])
print status_ef

body_sc = {}

url_sc1 = 'https://hca.datascienceelite.com/djob/v1/pca/extractfeatures/status/'+jobId_ef

import time

while status_ef == 'Waiting' or status_ef == 'Running' or status_ef == 'Pending':
  
  status_check1 = requests.post(url=url_sc1,json=body_sc,headers=header,verify=False)
  
  response_sc1 = status_check1.json()
  print response_sc1
  
  result_sc1 = response_sc1["result"]
  
  status_ef = str(result_sc1["result"][0]["result"])
  print status_ef
  
  time.sleep(3)


### Trigger the model scoring from extarcted features

if status_ef == 'Succeeded':

  url_ms = 'https://hca.datascienceelite.com/djob/v1/pca/scoremodel/trigger'
  
  model_scoring = requests.post(url=url_ms,json=body,headers=header,verify=False)
  
  response_ms = model_scoring.json()
  print response_ms

else:
  
  import nothing


### Check the status of the model scoring request

result_ms = response_ms["result"]

jobId_ms = str(result_ms['jobExecution']['runId'])
print jobId_ms

status_ms = str(result_ms['jobExecution']['result'])
print status_ms

url_sc2 = 'https://hca.datascienceelite.com/djob/v1/pca/scoremodel/status/'+jobId_ms

while status_ms == 'Waiting' or status_ms == 'Running' or status_ms == 'Pending':

  status_check2 = requests.post(url=url_sc2,json=body_sc,headers=header,verify=False)
  
  response_sc2 = status_check2.json()
  print response_sc2
  
  result_sc2 = response_sc2["result"]
  
  status_ms = str(result_sc2["result"][0]["result"])
  print status_ms
  
  time.sleep(3)

### Final if check to verify the job completion

if status_ms == 'Succeeded':
  print "Job Complete"

else:
  import nothing

