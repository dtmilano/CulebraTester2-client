# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.64
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Locale(object):
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
        'language': 'str',
        'country': 'str',
        'variant': 'str'
    }

    attribute_map = {
        'language': 'language',
        'country': 'country',
        'variant': 'variant'
    }

    def __init__(self, language=None, country=None, variant=None):  # noqa: E501
        """Locale - a model defined in Swagger"""  # noqa: E501
        self._language = None
        self._country = None
        self._variant = None
        self.discriminator = None
        self.language = language
        if country is not None:
            self.country = country
        if variant is not None:
            self.variant = variant

    @property
    def language(self):
        """Gets the language of this Locale.  # noqa: E501


        :return: The language of this Locale.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Locale.


        :param language: The language of this Locale.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def country(self):
        """Gets the country of this Locale.  # noqa: E501


        :return: The country of this Locale.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Locale.


        :param country: The country of this Locale.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def variant(self):
        """Gets the variant of this Locale.  # noqa: E501


        :return: The variant of this Locale.  # noqa: E501
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this Locale.


        :param variant: The variant of this Locale.  # noqa: E501
        :type: str
        """

        self._variant = variant

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
        if issubclass(Locale, dict):
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
        if not isinstance(other, Locale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
