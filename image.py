from azureml.core import Environment,Workspace, Experiment, Run
from azureml.core.webservice import Webservice
from azureml.core.model import Model, InferenceConfig
from azureml.core.image import Image, ContainerImage

# register
ws = Workspace.get(name='DiamondMLWS',
                   subscription_id='7a2efedb-22fb-4344-bf58-c4b1a17f440a',
                   resource_group='diamond-ml'
                  )

# # Re-fetch model.
# model = Model.register(model_path="outputs/sklearn_diamond_simple_model.pkl",
#                            model_name="sklearn_diamond_simple_model",
#                            tags={"key": "0.1"},
#                            description="test",
#                            workspace=ws)
model = Model(ws, name='sklearn_diamond_simple_model')
                           
print(model.name, model.id, model.version, sep='\t')

image_config = ContainerImage.image_configuration(runtime= "python",
                                 execution_script="score.py",
                                 conda_file="myenv.yml",
                                 tags = {'data': "diamonds", 'type': "sklearn"},
                                 description = "Diamonds sklearn model")

image = Image.create(name = "myimage1",
                     # this is the model object 
                     models = [model],
                     image_config = image_config, 
                     workspace = ws)

image.wait_for_creation(show_output = True)

print('Done')
