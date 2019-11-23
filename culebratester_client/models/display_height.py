# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class DisplayHeight(object):
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
        'display_height': 'int'
    }

    attribute_map = {
        'display_height': 'displayHeight'
    }

    def __init__(self, display_height=None):  # noqa: E501
        """DisplayHeight - a model defined in Swagger"""  # noqa: E501
        self._display_height = None
        self.discriminator = None
        if display_height is not None:
            self.display_height = display_height

    @property
    def display_height(self):
        """Gets the display_height of this DisplayHeight.  # noqa: E501

        the current display height  # noqa: E501

        :return: The display_height of this DisplayHeight.  # noqa: E501
        :rtype: int
        """
        return self._display_height

    @display_height.setter
    def display_height(self, display_height):
        """Sets the display_height of this DisplayHeight.

        the current display height  # noqa: E501

        :param display_height: The display_height of this DisplayHeight.  # noqa: E501
        :type: int
        """

        self._display_height = display_height

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
        if issubclass(DisplayHeight, dict):
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
        if not isinstance(other, DisplayHeight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
