# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.71
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Selector(object):
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
        'checkable': 'bool',
        'checked': 'bool',
        'clazz': 'str',
        'clickable': 'bool',
        'depth': 'int',
        'desc': 'str',
        'has_child': 'Selector',
        'has_descendant': 'Selector',
        'pkg': 'str',
        'res': 'str',
        'scrollable': 'bool',
        'text': 'str',
        'index': 'int',
        'instance': 'int'
    }

    attribute_map = {
        'checkable': 'checkable',
        'checked': 'checked',
        'clazz': 'clazz',
        'clickable': 'clickable',
        'depth': 'depth',
        'desc': 'desc',
        'has_child': 'hasChild',
        'has_descendant': 'hasDescendant',
        'pkg': 'pkg',
        'res': 'res',
        'scrollable': 'scrollable',
        'text': 'text',
        'index': 'index',
        'instance': 'instance'
    }

    def __init__(self, checkable=None, checked=None, clazz=None, clickable=None, depth=None, desc=None, has_child=None, has_descendant=None, pkg=None, res=None, scrollable=None, text=None, index=None, instance=None):  # noqa: E501
        """Selector - a model defined in Swagger"""  # noqa: E501
        self._checkable = None
        self._checked = None
        self._clazz = None
        self._clickable = None
        self._depth = None
        self._desc = None
        self._has_child = None
        self._has_descendant = None
        self._pkg = None
        self._res = None
        self._scrollable = None
        self._text = None
        self._index = None
        self._instance = None
        self.discriminator = None
        if checkable is not None:
            self.checkable = checkable
        if checked is not None:
            self.checked = checked
        if clazz is not None:
            self.clazz = clazz
        if clickable is not None:
            self.clickable = clickable
        if depth is not None:
            self.depth = depth
        if desc is not None:
            self.desc = desc
        if has_child is not None:
            self.has_child = has_child
        if has_descendant is not None:
            self.has_descendant = has_descendant
        if pkg is not None:
            self.pkg = pkg
        if res is not None:
            self.res = res
        if scrollable is not None:
            self.scrollable = scrollable
        if text is not None:
            self.text = text
        if index is not None:
            self.index = index
        if instance is not None:
            self.instance = instance

    @property
    def checkable(self):
        """Gets the checkable of this Selector.  # noqa: E501


        :return: The checkable of this Selector.  # noqa: E501
        :rtype: bool
        """
        return self._checkable

    @checkable.setter
    def checkable(self, checkable):
        """Sets the checkable of this Selector.


        :param checkable: The checkable of this Selector.  # noqa: E501
        :type: bool
        """

        self._checkable = checkable

    @property
    def checked(self):
        """Gets the checked of this Selector.  # noqa: E501


        :return: The checked of this Selector.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this Selector.


        :param checked: The checked of this Selector.  # noqa: E501
        :type: bool
        """

        self._checked = checked

    @property
    def clazz(self):
        """Gets the clazz of this Selector.  # noqa: E501


        :return: The clazz of this Selector.  # noqa: E501
        :rtype: str
        """
        return self._clazz

    @clazz.setter
    def clazz(self, clazz):
        """Sets the clazz of this Selector.


        :param clazz: The clazz of this Selector.  # noqa: E501
        :type: str
        """

        self._clazz = clazz

    @property
    def clickable(self):
        """Gets the clickable of this Selector.  # noqa: E501


        :return: The clickable of this Selector.  # noqa: E501
        :rtype: bool
        """
        return self._clickable

    @clickable.setter
    def clickable(self, clickable):
        """Sets the clickable of this Selector.


        :param clickable: The clickable of this Selector.  # noqa: E501
        :type: bool
        """

        self._clickable = clickable

    @property
    def depth(self):
        """Gets the depth of this Selector.  # noqa: E501


        :return: The depth of this Selector.  # noqa: E501
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this Selector.


        :param depth: The depth of this Selector.  # noqa: E501
        :type: int
        """

        self._depth = depth

    @property
    def desc(self):
        """Gets the desc of this Selector.  # noqa: E501


        :return: The desc of this Selector.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this Selector.


        :param desc: The desc of this Selector.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def has_child(self):
        """Gets the has_child of this Selector.  # noqa: E501


        :return: The has_child of this Selector.  # noqa: E501
        :rtype: Selector
        """
        return self._has_child

    @has_child.setter
    def has_child(self, has_child):
        """Sets the has_child of this Selector.


        :param has_child: The has_child of this Selector.  # noqa: E501
        :type: Selector
        """

        self._has_child = has_child

    @property
    def has_descendant(self):
        """Gets the has_descendant of this Selector.  # noqa: E501


        :return: The has_descendant of this Selector.  # noqa: E501
        :rtype: Selector
        """
        return self._has_descendant

    @has_descendant.setter
    def has_descendant(self, has_descendant):
        """Sets the has_descendant of this Selector.


        :param has_descendant: The has_descendant of this Selector.  # noqa: E501
        :type: Selector
        """

        self._has_descendant = has_descendant

    @property
    def pkg(self):
        """Gets the pkg of this Selector.  # noqa: E501


        :return: The pkg of this Selector.  # noqa: E501
        :rtype: str
        """
        return self._pkg

    @pkg.setter
    def pkg(self, pkg):
        """Sets the pkg of this Selector.


        :param pkg: The pkg of this Selector.  # noqa: E501
        :type: str
        """

        self._pkg = pkg

    @property
    def res(self):
        """Gets the res of this Selector.  # noqa: E501


        :return: The res of this Selector.  # noqa: E501
        :rtype: str
        """
        return self._res

    @res.setter
    def res(self, res):
        """Sets the res of this Selector.


        :param res: The res of this Selector.  # noqa: E501
        :type: str
        """

        self._res = res

    @property
    def scrollable(self):
        """Gets the scrollable of this Selector.  # noqa: E501


        :return: The scrollable of this Selector.  # noqa: E501
        :rtype: bool
        """
        return self._scrollable

    @scrollable.setter
    def scrollable(self, scrollable):
        """Sets the scrollable of this Selector.


        :param scrollable: The scrollable of this Selector.  # noqa: E501
        :type: bool
        """

        self._scrollable = scrollable

    @property
    def text(self):
        """Gets the text of this Selector.  # noqa: E501


        :return: The text of this Selector.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Selector.


        :param text: The text of this Selector.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def index(self):
        """Gets the index of this Selector.  # noqa: E501


        :return: The index of this Selector.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Selector.


        :param index: The index of this Selector.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def instance(self):
        """Gets the instance of this Selector.  # noqa: E501


        :return: The instance of this Selector.  # noqa: E501
        :rtype: int
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this Selector.


        :param instance: The instance of this Selector.  # noqa: E501
        :type: int
        """

        self._instance = instance

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
        if issubclass(Selector, dict):
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
        if not isinstance(other, Selector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
