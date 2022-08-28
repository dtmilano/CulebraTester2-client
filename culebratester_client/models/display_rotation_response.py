# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.45
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DisplayRotationResponse(object):
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
        'display_rotation': 'DisplayRotationEnum'
    }

    attribute_map = {
        'display_rotation': 'displayRotation'
    }

    def __init__(self, display_rotation=None):  # noqa: E501
        """DisplayRotationResponse - a model defined in Swagger"""  # noqa: E501
        self._display_rotation = None
        self.discriminator = None
        if display_rotation is not None:
            self.display_rotation = display_rotation

    @property
    def display_rotation(self):
        """Gets the display_rotation of this DisplayRotationResponse.  # noqa: E501


        :return: The display_rotation of this DisplayRotationResponse.  # noqa: E501
        :rtype: DisplayRotationEnum
        """
        return self._display_rotation

    @display_rotation.setter
    def display_rotation(self, display_rotation):
        """Sets the display_rotation of this DisplayRotationResponse.


        :param display_rotation: The display_rotation of this DisplayRotationResponse.  # noqa: E501
        :type: DisplayRotationEnum
        """

        self._display_rotation = display_rotation

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
        if issubclass(DisplayRotationResponse, dict):
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
        if not isinstance(other, DisplayRotationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
