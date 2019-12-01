# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class DisplayRealSize(object):
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
        'device': 'str',
        'x': 'int',
        'y': 'int',
        'art_width': 'int',
        'art_height': 'int',
        'screenshot_width': 'int',
        'screenshot_x': 'int',
        'screenshot_y': 'int'
    }

    attribute_map = {
        'device': 'device',
        'x': 'x',
        'y': 'y',
        'art_width': 'artWidth',
        'art_height': 'artHeight',
        'screenshot_width': 'screenshotWidth',
        'screenshot_x': 'screenshotX',
        'screenshot_y': 'screenshotY'
    }

    def __init__(self, device=None, x=None, y=None, art_width=None, art_height=None, screenshot_width=None, screenshot_x=None, screenshot_y=None):  # noqa: E501
        """DisplayRealSize - a model defined in Swagger"""  # noqa: E501
        self._device = None
        self._x = None
        self._y = None
        self._art_width = None
        self._art_height = None
        self._screenshot_width = None
        self._screenshot_x = None
        self._screenshot_y = None
        self.discriminator = None
        self.device = device
        self.x = x
        self.y = y
        if art_width is not None:
            self.art_width = art_width
        if art_height is not None:
            self.art_height = art_height
        if screenshot_width is not None:
            self.screenshot_width = screenshot_width
        if screenshot_x is not None:
            self.screenshot_x = screenshot_x
        if screenshot_y is not None:
            self.screenshot_y = screenshot_y

    @property
    def device(self):
        """Gets the device of this DisplayRealSize.  # noqa: E501


        :return: The device of this DisplayRealSize.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DisplayRealSize.


        :param device: The device of this DisplayRealSize.  # noqa: E501
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def x(self):
        """Gets the x of this DisplayRealSize.  # noqa: E501


        :return: The x of this DisplayRealSize.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this DisplayRealSize.


        :param x: The x of this DisplayRealSize.  # noqa: E501
        :type: int
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this DisplayRealSize.  # noqa: E501


        :return: The y of this DisplayRealSize.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this DisplayRealSize.


        :param y: The y of this DisplayRealSize.  # noqa: E501
        :type: int
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def art_width(self):
        """Gets the art_width of this DisplayRealSize.  # noqa: E501


        :return: The art_width of this DisplayRealSize.  # noqa: E501
        :rtype: int
        """
        return self._art_width

    @art_width.setter
    def art_width(self, art_width):
        """Sets the art_width of this DisplayRealSize.


        :param art_width: The art_width of this DisplayRealSize.  # noqa: E501
        :type: int
        """

        self._art_width = art_width

    @property
    def art_height(self):
        """Gets the art_height of this DisplayRealSize.  # noqa: E501


        :return: The art_height of this DisplayRealSize.  # noqa: E501
        :rtype: int
        """
        return self._art_height

    @art_height.setter
    def art_height(self, art_height):
        """Sets the art_height of this DisplayRealSize.


        :param art_height: The art_height of this DisplayRealSize.  # noqa: E501
        :type: int
        """

        self._art_height = art_height

    @property
    def screenshot_width(self):
        """Gets the screenshot_width of this DisplayRealSize.  # noqa: E501


        :return: The screenshot_width of this DisplayRealSize.  # noqa: E501
        :rtype: int
        """
        return self._screenshot_width

    @screenshot_width.setter
    def screenshot_width(self, screenshot_width):
        """Sets the screenshot_width of this DisplayRealSize.


        :param screenshot_width: The screenshot_width of this DisplayRealSize.  # noqa: E501
        :type: int
        """

        self._screenshot_width = screenshot_width

    @property
    def screenshot_x(self):
        """Gets the screenshot_x of this DisplayRealSize.  # noqa: E501


        :return: The screenshot_x of this DisplayRealSize.  # noqa: E501
        :rtype: int
        """
        return self._screenshot_x

    @screenshot_x.setter
    def screenshot_x(self, screenshot_x):
        """Sets the screenshot_x of this DisplayRealSize.


        :param screenshot_x: The screenshot_x of this DisplayRealSize.  # noqa: E501
        :type: int
        """

        self._screenshot_x = screenshot_x

    @property
    def screenshot_y(self):
        """Gets the screenshot_y of this DisplayRealSize.  # noqa: E501


        :return: The screenshot_y of this DisplayRealSize.  # noqa: E501
        :rtype: int
        """
        return self._screenshot_y

    @screenshot_y.setter
    def screenshot_y(self, screenshot_y):
        """Sets the screenshot_y of this DisplayRealSize.


        :param screenshot_y: The screenshot_y of this DisplayRealSize.  # noqa: E501
        :type: int
        """

        self._screenshot_y = screenshot_y

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
        if issubclass(DisplayRealSize, dict):
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
        if not isinstance(other, DisplayRealSize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
