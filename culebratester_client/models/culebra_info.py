# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CulebraInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'version_name': 'str',
        'version_code': 'int'
    }

    attribute_map = {
        'version_name': 'versionName',
        'version_code': 'versionCode'
    }

    def __init__(self, version_name=None, version_code=None):  # noqa: E501
        """CulebraInfo - a model defined in Swagger"""  # noqa: E501
        self._version_name = None
        self._version_code = None
        self.discriminator = None
        self.version_name = version_name
        self.version_code = version_code

    @property
    def version_name(self):
        """Gets the version_name of this CulebraInfo.  # noqa: E501


        :return: The version_name of this CulebraInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this CulebraInfo.


        :param version_name: The version_name of this CulebraInfo.  # noqa: E501
        :type: str
        """
        if version_name is None:
            raise ValueError("Invalid value for `version_name`, must not be `None`")  # noqa: E501

        self._version_name = version_name

    @property
    def version_code(self):
        """Gets the version_code of this CulebraInfo.  # noqa: E501


        :return: The version_code of this CulebraInfo.  # noqa: E501
        :rtype: int
        """
        return self._version_code

    @version_code.setter
    def version_code(self, version_code):
        """Sets the version_code of this CulebraInfo.


        :param version_code: The version_code of this CulebraInfo.  # noqa: E501
        :type: int
        """
        if version_code is None:
            raise ValueError("Invalid value for `version_code`, must not be `None`")  # noqa: E501

        self._version_code = version_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CulebraInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CulebraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
