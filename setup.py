from setuptools import find_packages, setup
from typing import List 



HYPEN_CONST = '-e .'

# This function will return the list of requirements
def get_requirements(file_path:str) -> List[str]: 
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_CONST in requirements:
            requirements.remove(HYPEN_CONST)
    return requirements


setup(
    name= 'Student-Performance-Predictor', 
    version='0.0.1', 
    author='Sneha',
    author_email='barve.sneha26@outlook.com', 
    packages=find_packages (), 
    install_requires=get_requirements('requirements.txt')

)