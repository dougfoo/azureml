from azureml.core import Environment,Workspace, Experiment, Run
from azureml.core.webservice import Webservice
from azureml.core.model import Model, InferenceConfig

# register
ws = Workspace.get(name='DiamondMLWS',
                   subscription_id='7a2efedb-22fb-4344-bf58-c4b1a17f440a',
                   resource_group='diamond-ml'
                  )

# Register new model.
new_model = Model.register(model_path="outputs/sklearn_diamond_simple_model.pkl",
                           model_name="sklearn_diamond_simple_model",
                           tags={"key": "0.1"},
                           description="test",
                           workspace=ws)

print('new model registered', new_model)

