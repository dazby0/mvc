from setuptools import setup, find_packages

setup(
    name="django-polls",
    version="0.1",
    packages=find_packages(),
    install_requires=["Django>=4.2"],
    include_package_data=True,
)
