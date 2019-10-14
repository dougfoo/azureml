import requests
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core import Environment,Workspace, Experiment, Run

# send a random row from the test set to score
input_data = "{\"data\": [[0.5], [1], [1.5], [2], [3]]}"  # one col per example
headers = {'Content-Type': 'application/json'}


ws = Workspace.get(name='DiamondMLWS',
                   subscription_id='7a2efedb-22fb-4344-bf58-c4b1a17f440a',
                   resource_group='diamond-ml'
                  )
service = Webservice(ws,'diamondsvc')

print('service: ', service, service.scoring_uri)

resp = requests.post(service.scoring_uri, input_data, headers=headers)

print("POST to url", service.scoring_uri)
#print("input data:", input_data)
print("inputs: 0.5,1,1.5,2,3")
print("prediction:", resp.text)

