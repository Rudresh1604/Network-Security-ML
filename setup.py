'''
The setup file is an essential part of packaging and distributing python projects 
'''

from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    # this function will return list of requirements
    requirement_lst:List[str]=[]
    try:
        with open('requirement.txt','r') as file:
            # read lines from file
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)


    except FileNotFoundError:
        print("requirement.txt file not found")

    return requirement_lst



setup(
    name="NetworkSecurity",
    author="Rudresh Dharkar",
    version="0.0.1",
    author_email="rudreshdharkar@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)