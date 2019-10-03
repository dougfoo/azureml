from azureml.core.conda_dependencies import CondaDependencies 

myenv = CondaDependencies.create(conda_packages=['numpy','scikit-learn'])

with open("myenv.yml","w") as f:
    f.write(myenv.serialize_to_string())

print('Done') 