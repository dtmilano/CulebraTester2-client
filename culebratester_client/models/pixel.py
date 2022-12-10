# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.61
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Pixel(object):
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
        'r': 'int',
        'g': 'int',
        'b': 'int',
        'a': 'int'
    }

    attribute_map = {
        'r': 'r',
        'g': 'g',
        'b': 'b',
        'a': 'a'
    }

    def __init__(self, r=None, g=None, b=None, a=None):  # noqa: E501
        """Pixel - a model defined in Swagger"""  # noqa: E501
        self._r = None
        self._g = None
        self._b = None
        self._a = None
        self.discriminator = None
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @property
    def r(self):
        """Gets the r of this Pixel.  # noqa: E501


        :return: The r of this Pixel.  # noqa: E501
        :rtype: int
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this Pixel.


        :param r: The r of this Pixel.  # noqa: E501
        :type: int
        """
        if r is None:
            raise ValueError("Invalid value for `r`, must not be `None`")  # noqa: E501

        self._r = r

    @property
    def g(self):
        """Gets the g of this Pixel.  # noqa: E501


        :return: The g of this Pixel.  # noqa: E501
        :rtype: int
        """
        return self._g

    @g.setter
    def g(self, g):
        """Sets the g of this Pixel.


        :param g: The g of this Pixel.  # noqa: E501
        :type: int
        """
        if g is None:
            raise ValueError("Invalid value for `g`, must not be `None`")  # noqa: E501

        self._g = g

    @property
    def b(self):
        """Gets the b of this Pixel.  # noqa: E501


        :return: The b of this Pixel.  # noqa: E501
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this Pixel.


        :param b: The b of this Pixel.  # noqa: E501
        :type: int
        """
        if b is None:
            raise ValueError("Invalid value for `b`, must not be `None`")  # noqa: E501

        self._b = b

    @property
    def a(self):
        """Gets the a of this Pixel.  # noqa: E501


        :return: The a of this Pixel.  # noqa: E501
        :rtype: int
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this Pixel.


        :param a: The a of this Pixel.  # noqa: E501
        :type: int
        """
        if a is None:
            raise ValueError("Invalid value for `a`, must not be `None`")  # noqa: E501

        self._a = a

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
        if issubclass(Pixel, dict):
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
        if not isinstance(other, Pixel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
