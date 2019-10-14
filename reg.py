from azureml.core import Environment,Workspace, Experiment, Run
from azureml.core.webservice import Webservice
from azureml.core.model import Model, InferenceConfig
import sys

name = ''
if (len(sys.argv) != 2):
    print ('supply arg for model name .. exiting') 
    sys.exit(1)
else:
    name = sys.argv[1]
    print ('running for model: '+ name)

# register
ws = Workspace.get(name='DiamondMLWS',
                   subscription_id='7a2efedb-22fb-4344-bf58-c4b1a17f440a',
                   resource_group='diamond-ml'
                  )

# Register new model.
new_model = Model.register(model_path=name+".pkl",
                           model_name=name,
                           tags={"key": "0.1"},
                           description="test",
                           workspace=ws)

print('new model registered', new_model)