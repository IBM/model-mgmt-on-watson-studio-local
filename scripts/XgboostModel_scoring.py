import os
import sys

import pandas as pd
import requests
import ast

ver = sys.argv[1]

test_features = pd.read_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/test_features'+'-'+ver+'.csv',index_col=0)
test_features = test_features.iloc[:,1:]
test_features.columns = ['f0','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12']

predictions = pd.Series()

for i in range(len(test_features)):
    
    P1 = test_features['f0'][i]
    P2 = test_features['f1'][i]
    P3 = test_features['f2'][i]
    P4 = test_features['f3'][i]
    P5 = test_features['f4'][i]
    P6 = test_features['f5'][i]
    P7 = test_features['f6'][i]
    P8 = test_features['f7'][i]
    P9 = test_features['f8'][i]
    P10 = test_features['f9'][i]
    P11 = test_features['f10'][i]
    P12 = test_features['f11'][i]
    P13 = test_features['f12'][i]
    
    value_string = '[{"f0":'+str(P1)+',"f1":'+str(P2)+',"f2":'+str(P3)+',"f3":'+str(P4)+',"f4":'+str(P5)+',"f5":'+str(P6)+',"f6":'+str(P7)+',"f7":'+str(P8)+',"f8":'+str(P9)+',"f9":'+str(P10)+',"f10":'+str(P11)+',"f11":'+str(P12)+',"f12":'+str(P13)+'}]'
    data = {"input_json_str":value_string}
    
    body = {"args": data}
    
    header = {'Content-Type': 'application/json','Cache-Control': 'no-cache','Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZpc2hudSIsInBhY2thZ2VOYW1lIjoieGdib29zdC1tb2RlbCIsInBhY2thZ2VSb3V0ZSI6InhnYm9vc3QiLCJpYXQiOjE1MzExNTkzNTR9.s5tuOK7PGWkSiKJW4Qj1u8ptAr8-zfcnrC7bV_Jwi8H2jErTB8j4swDnawgBGFWYcfURzwX3c-cliWZeePfr7RE3JoBnHMbi0DWSgPzPxpCSyeui_iMcYBuesXKF8ag45Werc9UpVSlIwRcDhaElR8_EGUAwMYukdaoK_VwiFw1-MtfGDG7Dnlg3OEM9xNKYrTOR4PYEoCnAPlMfQbTobRC5OcEBXEAU3z_GUw06kIjKj7kvAwDEgtJ8o4wKl3F3Z6CXTDMo-qEzmcJftq7DemjTubxwUUO238GDTrQWfK_sOfRHRyXsWBLQclq0uhq77j0k-4CXufY04aS2M6Jzuw'}

    url = 'https://hca.datascienceelite.com/dmodel/v1/xgboost/pyscript/xgboost-model/score'
    
    submit_request = requests.post(url=url,json=body,headers=header,verify=False)
    
    scoring_response = submit_request.json()
    
    result = scoring_response["result"][0].replace("null","0")
    
    predicted_value = float(ast.literal_eval(result)["predictions"][0])
    
    predictions = predictions.append(pd.Series(predicted_value))
    

test_features = test_features[['f0','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12']]

predictions.index = [x for x in range(len(predictions)) ]

predictions = predictions.to_frame()


scoring_result = pd.concat([test_features,predictions],axis=1,ignore_index=True)

scoring_result.to_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/xgboostscoring_output'+'-'+ver+'.csv')
    
    
    