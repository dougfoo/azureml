from azureml.core import Environment,Workspace, Experiment, Run
from azureml.core.webservice import Webservice
from azureml.core.model import Model, InferenceConfig
import datetime

ws = Workspace.get(name='DiamondMLWS',
                   subscription_id='7a2efedb-22fb-4344-bf58-c4b1a17f440a',
                   resource_group='diamond-ml'
                  )

exp = Experiment(workspace=ws, name='exp1')
run = exp.start_logging()                   
run.log("Experiment start time", str(datetime.datetime.now()))
run.log("Experiment end time", str(datetime.datetime.now()))
run.complete()
