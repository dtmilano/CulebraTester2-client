# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.47
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DisplaySizeDp(object):
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
        'display_size_dp_x': 'int',
        'display_size_dp_y': 'int'
    }

    attribute_map = {
        'display_size_dp_x': 'displaySizeDpX',
        'display_size_dp_y': 'displaySizeDpY'
    }

    def __init__(self, display_size_dp_x=None, display_size_dp_y=None):  # noqa: E501
        """DisplaySizeDp - a model defined in Swagger"""  # noqa: E501
        self._display_size_dp_x = None
        self._display_size_dp_y = None
        self.discriminator = None
        if display_size_dp_x is not None:
            self.display_size_dp_x = display_size_dp_x
        if display_size_dp_y is not None:
            self.display_size_dp_y = display_size_dp_y

    @property
    def display_size_dp_x(self):
        """Gets the display_size_dp_x of this DisplaySizeDp.  # noqa: E501

        the display x in DP  # noqa: E501

        :return: The display_size_dp_x of this DisplaySizeDp.  # noqa: E501
        :rtype: int
        """
        return self._display_size_dp_x

    @display_size_dp_x.setter
    def display_size_dp_x(self, display_size_dp_x):
        """Sets the display_size_dp_x of this DisplaySizeDp.

        the display x in DP  # noqa: E501

        :param display_size_dp_x: The display_size_dp_x of this DisplaySizeDp.  # noqa: E501
        :type: int
        """

        self._display_size_dp_x = display_size_dp_x

    @property
    def display_size_dp_y(self):
        """Gets the display_size_dp_y of this DisplaySizeDp.  # noqa: E501

        the display y in DP  # noqa: E501

        :return: The display_size_dp_y of this DisplaySizeDp.  # noqa: E501
        :rtype: int
        """
        return self._display_size_dp_y

    @display_size_dp_y.setter
    def display_size_dp_y(self, display_size_dp_y):
        """Sets the display_size_dp_y of this DisplaySizeDp.

        the display y in DP  # noqa: E501

        :param display_size_dp_y: The display_size_dp_y of this DisplaySizeDp.  # noqa: E501
        :type: int
        """

        self._display_size_dp_y = display_size_dp_y

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
        if issubclass(DisplaySizeDp, dict):
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
        if not isinstance(other, DisplaySizeDp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
