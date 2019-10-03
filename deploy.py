from azureml.core import Environment,Workspace, Experiment, Run
from azureml.core.image import Image, ContainerImage
from azureml.core.webservice import AciWebservice

aciconfig = AciWebservice.deploy_configuration(cpu_cores = 1, 
                                          memory_gb = 1, 
                                          tags = {"data": "diamonds", "type": "sklearn"}, 
                                          description = 'Diamond pricing')

print('aciconfig Done')

from azureml.core.webservice import Webservice

ws = Workspace.get(name='DiamondMLWS',
                   subscription_id='7a2efedb-22fb-4344-bf58-c4b1a17f440a',
                   resource_group='diamond-ml'
                  )

image = Image(workspace=ws, name='myimage1')
print('image: ',image)

service_name = 'aci-diamond-1'
service = Webservice.deploy_from_image(deployment_config = aciconfig,
                                            image = image,
                                            name = service_name,
                                            workspace = ws)

service.wait_for_deployment(show_output = True)

print('deploy ws Done')
