from typing import List
from setuptools import find_packages,setup

def get_requirements(file_path:str)->list[str]:
        requirements=[] ##open file and pass line by line and if \n replace space and ignore -e 
        with open(file_path ,encoding='utf-8') as obj_require:
            requirements=obj_require().readline()
            requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
            return requirements
        

#information on project and requirements
setup(
        name='house Power END To END ML',
        author="Mohamed Nasser",
        author_email="hagag9868@gmail.com",
        version="0.0.2",
        description="this Project handel and predict Electricity bill",
        packages=find_packages(),
        #create exterm fun get file to function 
        install_requires=get_requirements('requirement.txt')
)
