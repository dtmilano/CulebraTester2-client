# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.73
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Rect(object):
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
        'left': 'int',
        'top': 'int',
        'right': 'int',
        'bottom': 'int'
    }

    attribute_map = {
        'left': 'left',
        'top': 'top',
        'right': 'right',
        'bottom': 'bottom'
    }

    def __init__(self, left=None, top=None, right=None, bottom=None):  # noqa: E501
        """Rect - a model defined in Swagger"""  # noqa: E501
        self._left = None
        self._top = None
        self._right = None
        self._bottom = None
        self.discriminator = None
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    @property
    def left(self):
        """Gets the left of this Rect.  # noqa: E501


        :return: The left of this Rect.  # noqa: E501
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this Rect.


        :param left: The left of this Rect.  # noqa: E501
        :type: int
        """
        if left is None:
            raise ValueError("Invalid value for `left`, must not be `None`")  # noqa: E501

        self._left = left

    @property
    def top(self):
        """Gets the top of this Rect.  # noqa: E501


        :return: The top of this Rect.  # noqa: E501
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this Rect.


        :param top: The top of this Rect.  # noqa: E501
        :type: int
        """
        if top is None:
            raise ValueError("Invalid value for `top`, must not be `None`")  # noqa: E501

        self._top = top

    @property
    def right(self):
        """Gets the right of this Rect.  # noqa: E501


        :return: The right of this Rect.  # noqa: E501
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this Rect.


        :param right: The right of this Rect.  # noqa: E501
        :type: int
        """
        if right is None:
            raise ValueError("Invalid value for `right`, must not be `None`")  # noqa: E501

        self._right = right

    @property
    def bottom(self):
        """Gets the bottom of this Rect.  # noqa: E501


        :return: The bottom of this Rect.  # noqa: E501
        :rtype: int
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this Rect.


        :param bottom: The bottom of this Rect.  # noqa: E501
        :type: int
        """
        if bottom is None:
            raise ValueError("Invalid value for `bottom`, must not be `None`")  # noqa: E501

        self._bottom = bottom

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
        if issubclass(Rect, dict):
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
        if not isinstance(other, Rect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
