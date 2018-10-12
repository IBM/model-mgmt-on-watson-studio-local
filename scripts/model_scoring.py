import os
import sys

import pandas as pd
import requests

# Update the following values from deployed assets
AUTH_TOKEN = '<add authorization token>'
MODEL_ENDPOINT = '<add model endpoint>'

ver = sys.argv[1]

features = pd.read_csv(os.environ['DSX_PROJECT_DIR'] +
                       '/datasets/features' + '-' + ver + '.csv')

predictions = pd.Series()

for i in range(len(features)):

    P1 = features['0'][i]
    P2 = features['1'][i]

    value_string = [{"0": str(P1), "1": str(P2)}]
    data = {"input_json": value_string}

    body = {"args": data}
    header = {'Content-Type': 'application/json',
              'Cache-Control': 'no-cache',
              'Authorization': AUTH_TOKEN}
    submit_request = requests.post(url=MODEL_ENDPOINT,
                                   json=body,
                                   headers=header,
                                   verify=False)

    scoring_response = submit_request.json()
    predicted_value = int(scoring_response["result"]["predictions"][0])
    predictions = predictions.append(pd.Series(predicted_value))

features = features[["0", "1"]]
predictions.index = [x for x in range(len(predictions))]
predictions = predictions.to_frame()

scoring_result = pd.concat([features, predictions], axis=1, ignore_index=True)
scoring_result.to_csv(os.environ['DSX_PROJECT_DIR'] +
                      '/datasets/scoring_output' + '-' + ver + '.csv')
