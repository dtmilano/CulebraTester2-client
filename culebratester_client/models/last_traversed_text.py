# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.54
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LastTraversedText(object):
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
        'last_traversed_text': 'str'
    }

    attribute_map = {
        'last_traversed_text': 'lastTraversedText'
    }

    def __init__(self, last_traversed_text=None):  # noqa: E501
        """LastTraversedText - a model defined in Swagger"""  # noqa: E501
        self._last_traversed_text = None
        self.discriminator = None
        if last_traversed_text is not None:
            self.last_traversed_text = last_traversed_text

    @property
    def last_traversed_text(self):
        """Gets the last_traversed_text of this LastTraversedText.  # noqa: E501

        text of the last traversal event, else return an empty string  # noqa: E501

        :return: The last_traversed_text of this LastTraversedText.  # noqa: E501
        :rtype: str
        """
        return self._last_traversed_text

    @last_traversed_text.setter
    def last_traversed_text(self, last_traversed_text):
        """Sets the last_traversed_text of this LastTraversedText.

        text of the last traversal event, else return an empty string  # noqa: E501

        :param last_traversed_text: The last_traversed_text of this LastTraversedText.  # noqa: E501
        :type: str
        """

        self._last_traversed_text = last_traversed_text

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
        if issubclass(LastTraversedText, dict):
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
        if not isinstance(other, LastTraversedText):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
