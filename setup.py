from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requiremnts(file_path: str) -> List[str]:
    """
    this function is returrn the list of requrements
    """
    requrements = []
    with open(file_path) as file_obj:
        requrements = file_obj.readlines()
        requrements=[req.replace("\n", "") for req in requrements]
        
        if HYPEN_E_DOT in requrements:
          requrements.remove(HYPEN_E_DOT)
          
    return requrements


setup(
    name="mlproject",
    version="0.0.1",
    author="hiren",
    author_email="kanzariyahiren655@gmail.com",
    packages=find_packages(),
    install_requires=get_requiremnts("requirements.txt"),
)
