# Must do seperately
# run env.py script to create myenv.yml
# build score.py script

# setup ACI
from azureml.core.webservice import AciWebservice
aciconfig = AciWebservice.deploy_configuration(cpu_cores=1, 
                                               memory_gb=1, 
                                               tags={"data": "diamonds",  
                                                     "method": "sklearn"},
                                               description='Predict Diamonds with sklearn')

# model setup
from azureml.core import Workspace
from azureml.core.model import Model
import os
# ws = Workspace.from_config()  # which ws does this fetch?
ws = Workspace.get(name='DiamondMLWS',
                   subscription_id='7a2efedb-22fb-4344-bf58-c4b1a17f440a',
                   resource_group='diamond-ml')
model = Model(ws, 'sklearn_diamond_simple_model')
model.download(target_dir=os.getcwd(), exist_ok=True)  # write copy of pkl file

# setup service
from azureml.core.webservice import Webservice
from azureml.core.model import InferenceConfig

inference_config = InferenceConfig(runtime= "python", 
                                   entry_script="score.py",
                                   conda_file="myenv.yml")

service = Model.deploy(workspace=ws, 
                       name='diamondsvc',
                       models=[model],
                       inference_config=inference_config,
                       deployment_config=aciconfig)

service.wait_for_deployment(show_output=True)

print(service.scoring_uri)
