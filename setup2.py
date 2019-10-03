from azureml.core import Workspace, Experiment, Run
from azureml.train.sklearn import SKLearn
import os

# create the folder
folder_training_script = './trial_model_mnist'
os.makedirs(folder_training_script, exist_ok=True)
script_params = {
    '--data-folder': ds.as_mount(),
    '--regularization': 0.5
}

ws = Workspace.get(name='DiamondMLWS',
                   subscription_id='7a2efedb-22fb-4344-bf58-c4b1a17f440a',
                   resource_group='diamond-ml'
                  )
experiment = Experiment(workspace = ws, name = "test-diamond-1")

from azureml.core.compute import AmlCompute
from azureml.core.compute import ComputeTarget
import os

# Step 1: name the cluster and set the minimal and maximal number of nodes 
compute_name = os.environ.get("AML_COMPUTE_CLUSTER_NAME", "cpucluster")
min_nodes = os.environ.get("AML_COMPUTE_CLUSTER_MIN_NODES", 0)
max_nodes = os.environ.get("AML_COMPUTE_CLUSTER_MAX_NODES", 3)

# Step 2: choose environment variables 
vm_size = os.environ.get("AML_COMPUTE_CLUSTER_SKU", "STANDARD_D2_V2")

provisioning_config = AmlCompute.provisioning_configuration(
    vm_size = vm_size, min_nodes = min_nodes, max_nodes = max_nodes)

# create the cluster
compute_target = ComputeTarget.create(ws, compute_name, provisioning_config)


#import the Scikit-learn package 
est = SKLearn(source_directory=folder_training_script,
                script_params=script_params,
                compute_target=compute_target,
                entry_script='train.py',
                conda_packages=['scikit-learn'])

run = experiment.submit(config=est)

model = run.register_model(model_name='sklearn_diamond_simple_model.pkl',
                           model_path='outputs/sklearn_diamond_simple_model.pkl',
                           tags = {'model': "linear", 'inputs': "carat"},
                           description = "diamond pricing model")

print(model.name, model.id, model.version, sep='\t')
