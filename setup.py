from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:

            lines=file.readlines()
            ## process each line
            for line in lines:
                requirements = line.strip()
                ## ignore empty lines and -e.
                if requirements and requirements!= '-e .':
                    requirement_list.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list


setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="sajidshaik",
    author_email="sajidshaik.7595@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

print(get_requirements())
