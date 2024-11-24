from setuptools import setup ,find_packages
from typing import List
HYPE_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements

    '''

    with open('requirements.txt') as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)

    return requirements

setup( 
    name='ml-project01', 
    version='0.1', 
    description='end to end ml project 1st', 
    author='Swapnil', 
    author_email='swapnilkhandoker111@gmail.com', 
    packages=find_packages(),
    install_requires=[get_requirements("requirements.txt")]
)