# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.43
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse200(object):
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
        'obj': 'AnyValue',
        'oid': 'int'
    }

    attribute_map = {
        'obj': 'obj',
        'oid': 'oid'
    }

    def __init__(self, obj=None, oid=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._obj = None
        self._oid = None
        self.discriminator = None
        if obj is not None:
            self.obj = obj
        if oid is not None:
            self.oid = oid

    @property
    def obj(self):
        """Gets the obj of this InlineResponse200.  # noqa: E501


        :return: The obj of this InlineResponse200.  # noqa: E501
        :rtype: AnyValue
        """
        return self._obj

    @obj.setter
    def obj(self, obj):
        """Sets the obj of this InlineResponse200.


        :param obj: The obj of this InlineResponse200.  # noqa: E501
        :type: AnyValue
        """

        self._obj = obj

    @property
    def oid(self):
        """Gets the oid of this InlineResponse200.  # noqa: E501


        :return: The oid of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this InlineResponse200.


        :param oid: The oid of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._oid = oid

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
