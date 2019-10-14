from azureml.core import Environment, Workspace, Experiment, Run
from azureml.core.image import Image, ContainerImage
from azureml.core.webservice import LocalWebservice, Webservice, AciWebservice
from azureml.core.model import Model, InferenceConfig

print('aciconfig Done')

ws = Workspace.get(name='DiamondMLWS',
                   subscription_id='7a2efedb-22fb-4344-bf58-c4b1a17f440a',
                   resource_group='diamond-ml'
                  )

image = Image(workspace=ws, name='myimage1')
image_config = ContainerImage.image_configuration(runtime= "python",
                                 execution_script="score.py",
                                 conda_file="myenv.yml",
                                 tags = {'data': "diamonds", 'type': "sklearn"},
                                 description = "Diamonds sklearn model")
print('image: ',image)

service_name = 'aci-diamond-3'
# service = Webservice.deploy_from_image(deployment_config = aciconfig,  
#                                             image = image,
#                                             name = service_name,
#                                             workspace = ws)
aciconfig = AciWebservice.deploy_configuration(cpu_cores = 1, 
                                          memory_gb = 1, 
                                          tags = {"data": "diamonds", "type": "sklearn"}, 
                                          description = 'Diamond pricing')

model = Model(ws, name='sklearn_diamond_simple_model')

service = Webservice.deploy_from_model(deployment_config = aciconfig,  
                                            name = service_name,
                                            models = [model],
                                            image_config = image_config,
                                            workspace = ws)

print('deploy ws Done', service, service.scoring_uri)
