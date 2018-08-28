import os
import sys

import pandas as pd
import requests

ver = sys.argv[1]

features = pd.read_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/features'+'-'+ver+'.csv')

predictions = pd.Series()


for i in range(len(features)):
    
    P1 = features['0'][i]
    P2 = features['1'][i]
    
    value_string = '[{"0":'+str(P1)+',"1":'+str(P2)+'}]'
    data = {"input_json_str":value_string}
    
    body = {"args": data}
    
    header = {'Content-Type': 'application/json','Cache-Control': 'no-cache','Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZpc2hudSIsInBhY2thZ2VOYW1lIjoicGNhLW1vZGVsIiwicGFja2FnZVJvdXRlIjoicGNhIiwiaWF0IjoxNTI5OTE1OTkwfQ.kcOwXMU9NngHZLLPOa3J4NeQUSFia5zEbIND_YdzN-8KVGMLtURR725rZQL8KPktw1iWQwc9JlKEiKao58_DJIuZb01ekKZExD-qBozsSpjvalQaKKMA2QaI42zgeMSCyuU6zAzA4AEXFjyOoulEsZ0zBCOrZocIyLLDuLIClRSVrf_lZFsbx3roKhODqcLzeGcexN-7_HcXCotGaWsEvASkpq3ivFC4a3F3SqZ7w0cXFMAh9RrK5UPZNb4aD_0AcSed1WcddGWeBxz8JgZvOExQ5IHsukhb1bsCWa1wFSV8C6oxZb4Sb71fqHD9HDRrF4LxB-7FyLpdcvF66dm-zg'}

    url = 'https://hca.datascienceelite.com/dmodel/v1/pca/pyscript/pcamodel/score'
    
    submit_request = requests.post(url=url,json=body,headers=header,verify=False)
    
    scoring_response = submit_request.json()
    
    predicted_value = int(scoring_response["result"][0][-3])
    
    predictions = predictions.append(pd.Series(predicted_value))


features = features[["0","1"]]

predictions.index = [x for x in range(len(predictions)) ]

predictions = predictions.to_frame()


scoring_result = pd.concat([features,predictions],axis=1,ignore_index=True)

scoring_result.to_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/scoring_output'+'-'+ver+'.csv')

