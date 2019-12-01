# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "culebratester-client"
VERSION = "2.0.4b1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="CulebraTester",
    author_email="",
    url="http://github.com/dtmilano/CulebraTester2-client",
    keywords=["Swagger", "CulebraTester"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using &#x60;adb&#x60; - the server should have been started using &#x60;./culebratester2 start-server&#x60;  then you will be able to invoke the API and see the responses.   # noqa: E501
    """
)
