from setuptools import find_packages,setup
from typing import List

Hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:      #takes the input as file and return the output as list
    '''
    this function will return the list of requirements
    '''
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()           #reads the files as lines
        requirements = [req.replace("\n","") for req in requirements ]  #this will remove the \n tag which will come due to line
                                                                        #change in the file
        
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)    #we dont want the -e to come into our requirements list

        return requirements



setup(
name = 'MLproject',
version='0.0.1',
author='aman',
packages = find_packages(),
install_requires =  get_requirements('requirements.txt')

)