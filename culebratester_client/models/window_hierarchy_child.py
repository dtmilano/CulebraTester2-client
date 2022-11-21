# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.56
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WindowHierarchyChild(object):
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
        'id': 'int',
        'parent': 'int',
        'text': 'str',
        'package': 'str',
        'checkable': 'bool',
        'clickable': 'bool',
        'index': 'int',
        'content_description': 'str',
        'focusable': 'bool',
        'resource_id': 'str',
        'enabled': 'bool',
        'password': 'bool',
        'long_clickable': 'bool',
        'long_text': 'str',
        'clazz': 'str',
        'scrollable': 'bool',
        'selected': 'bool',
        'checked': 'bool',
        'focused': 'bool',
        'bounds': 'list[int]',
        'children': 'list[WindowHierarchyChild]'
    }

    attribute_map = {
        'id': 'id',
        'parent': 'parent',
        'text': 'text',
        'package': 'package',
        'checkable': 'checkable',
        'clickable': 'clickable',
        'index': 'index',
        'content_description': 'contentDescription',
        'focusable': 'focusable',
        'resource_id': 'resourceId',
        'enabled': 'enabled',
        'password': 'password',
        'long_clickable': 'longClickable',
        'long_text': 'longText',
        'clazz': 'clazz',
        'scrollable': 'scrollable',
        'selected': 'selected',
        'checked': 'checked',
        'focused': 'focused',
        'bounds': 'bounds',
        'children': 'children'
    }

    def __init__(self, id=None, parent=None, text=None, package=None, checkable=None, clickable=None, index=None, content_description=None, focusable=None, resource_id=None, enabled=None, password=None, long_clickable=None, long_text=None, clazz=None, scrollable=None, selected=None, checked=None, focused=None, bounds=None, children=None):  # noqa: E501
        """WindowHierarchyChild - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._parent = None
        self._text = None
        self._package = None
        self._checkable = None
        self._clickable = None
        self._index = None
        self._content_description = None
        self._focusable = None
        self._resource_id = None
        self._enabled = None
        self._password = None
        self._long_clickable = None
        self._long_text = None
        self._clazz = None
        self._scrollable = None
        self._selected = None
        self._checked = None
        self._focused = None
        self._bounds = None
        self._children = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if parent is not None:
            self.parent = parent
        if text is not None:
            self.text = text
        if package is not None:
            self.package = package
        if checkable is not None:
            self.checkable = checkable
        if clickable is not None:
            self.clickable = clickable
        if index is not None:
            self.index = index
        if content_description is not None:
            self.content_description = content_description
        if focusable is not None:
            self.focusable = focusable
        if resource_id is not None:
            self.resource_id = resource_id
        if enabled is not None:
            self.enabled = enabled
        if password is not None:
            self.password = password
        if long_clickable is not None:
            self.long_clickable = long_clickable
        if long_text is not None:
            self.long_text = long_text
        if clazz is not None:
            self.clazz = clazz
        if scrollable is not None:
            self.scrollable = scrollable
        if selected is not None:
            self.selected = selected
        if checked is not None:
            self.checked = checked
        if focused is not None:
            self.focused = focused
        if bounds is not None:
            self.bounds = bounds
        if children is not None:
            self.children = children

    @property
    def id(self):
        """Gets the id of this WindowHierarchyChild.  # noqa: E501


        :return: The id of this WindowHierarchyChild.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WindowHierarchyChild.


        :param id: The id of this WindowHierarchyChild.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def parent(self):
        """Gets the parent of this WindowHierarchyChild.  # noqa: E501


        :return: The parent of this WindowHierarchyChild.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this WindowHierarchyChild.


        :param parent: The parent of this WindowHierarchyChild.  # noqa: E501
        :type: int
        """

        self._parent = parent

    @property
    def text(self):
        """Gets the text of this WindowHierarchyChild.  # noqa: E501


        :return: The text of this WindowHierarchyChild.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this WindowHierarchyChild.


        :param text: The text of this WindowHierarchyChild.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def package(self):
        """Gets the package of this WindowHierarchyChild.  # noqa: E501


        :return: The package of this WindowHierarchyChild.  # noqa: E501
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this WindowHierarchyChild.


        :param package: The package of this WindowHierarchyChild.  # noqa: E501
        :type: str
        """

        self._package = package

    @property
    def checkable(self):
        """Gets the checkable of this WindowHierarchyChild.  # noqa: E501


        :return: The checkable of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._checkable

    @checkable.setter
    def checkable(self, checkable):
        """Sets the checkable of this WindowHierarchyChild.


        :param checkable: The checkable of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._checkable = checkable

    @property
    def clickable(self):
        """Gets the clickable of this WindowHierarchyChild.  # noqa: E501


        :return: The clickable of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._clickable

    @clickable.setter
    def clickable(self, clickable):
        """Sets the clickable of this WindowHierarchyChild.


        :param clickable: The clickable of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._clickable = clickable

    @property
    def index(self):
        """Gets the index of this WindowHierarchyChild.  # noqa: E501


        :return: The index of this WindowHierarchyChild.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this WindowHierarchyChild.


        :param index: The index of this WindowHierarchyChild.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def content_description(self):
        """Gets the content_description of this WindowHierarchyChild.  # noqa: E501


        :return: The content_description of this WindowHierarchyChild.  # noqa: E501
        :rtype: str
        """
        return self._content_description

    @content_description.setter
    def content_description(self, content_description):
        """Sets the content_description of this WindowHierarchyChild.


        :param content_description: The content_description of this WindowHierarchyChild.  # noqa: E501
        :type: str
        """

        self._content_description = content_description

    @property
    def focusable(self):
        """Gets the focusable of this WindowHierarchyChild.  # noqa: E501


        :return: The focusable of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._focusable

    @focusable.setter
    def focusable(self, focusable):
        """Sets the focusable of this WindowHierarchyChild.


        :param focusable: The focusable of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._focusable = focusable

    @property
    def resource_id(self):
        """Gets the resource_id of this WindowHierarchyChild.  # noqa: E501


        :return: The resource_id of this WindowHierarchyChild.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this WindowHierarchyChild.


        :param resource_id: The resource_id of this WindowHierarchyChild.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def enabled(self):
        """Gets the enabled of this WindowHierarchyChild.  # noqa: E501


        :return: The enabled of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WindowHierarchyChild.


        :param enabled: The enabled of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def password(self):
        """Gets the password of this WindowHierarchyChild.  # noqa: E501


        :return: The password of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this WindowHierarchyChild.


        :param password: The password of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._password = password

    @property
    def long_clickable(self):
        """Gets the long_clickable of this WindowHierarchyChild.  # noqa: E501


        :return: The long_clickable of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._long_clickable

    @long_clickable.setter
    def long_clickable(self, long_clickable):
        """Sets the long_clickable of this WindowHierarchyChild.


        :param long_clickable: The long_clickable of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._long_clickable = long_clickable

    @property
    def long_text(self):
        """Gets the long_text of this WindowHierarchyChild.  # noqa: E501


        :return: The long_text of this WindowHierarchyChild.  # noqa: E501
        :rtype: str
        """
        return self._long_text

    @long_text.setter
    def long_text(self, long_text):
        """Sets the long_text of this WindowHierarchyChild.


        :param long_text: The long_text of this WindowHierarchyChild.  # noqa: E501
        :type: str
        """

        self._long_text = long_text

    @property
    def clazz(self):
        """Gets the clazz of this WindowHierarchyChild.  # noqa: E501


        :return: The clazz of this WindowHierarchyChild.  # noqa: E501
        :rtype: str
        """
        return self._clazz

    @clazz.setter
    def clazz(self, clazz):
        """Sets the clazz of this WindowHierarchyChild.


        :param clazz: The clazz of this WindowHierarchyChild.  # noqa: E501
        :type: str
        """

        self._clazz = clazz

    @property
    def scrollable(self):
        """Gets the scrollable of this WindowHierarchyChild.  # noqa: E501


        :return: The scrollable of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._scrollable

    @scrollable.setter
    def scrollable(self, scrollable):
        """Sets the scrollable of this WindowHierarchyChild.


        :param scrollable: The scrollable of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._scrollable = scrollable

    @property
    def selected(self):
        """Gets the selected of this WindowHierarchyChild.  # noqa: E501


        :return: The selected of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this WindowHierarchyChild.


        :param selected: The selected of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def checked(self):
        """Gets the checked of this WindowHierarchyChild.  # noqa: E501


        :return: The checked of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this WindowHierarchyChild.


        :param checked: The checked of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._checked = checked

    @property
    def focused(self):
        """Gets the focused of this WindowHierarchyChild.  # noqa: E501


        :return: The focused of this WindowHierarchyChild.  # noqa: E501
        :rtype: bool
        """
        return self._focused

    @focused.setter
    def focused(self, focused):
        """Sets the focused of this WindowHierarchyChild.


        :param focused: The focused of this WindowHierarchyChild.  # noqa: E501
        :type: bool
        """

        self._focused = focused

    @property
    def bounds(self):
        """Gets the bounds of this WindowHierarchyChild.  # noqa: E501


        :return: The bounds of this WindowHierarchyChild.  # noqa: E501
        :rtype: list[int]
        """
        return self._bounds

    @bounds.setter
    def bounds(self, bounds):
        """Sets the bounds of this WindowHierarchyChild.


        :param bounds: The bounds of this WindowHierarchyChild.  # noqa: E501
        :type: list[int]
        """

        self._bounds = bounds

    @property
    def children(self):
        """Gets the children of this WindowHierarchyChild.  # noqa: E501


        :return: The children of this WindowHierarchyChild.  # noqa: E501
        :rtype: list[WindowHierarchyChild]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this WindowHierarchyChild.


        :param children: The children of this WindowHierarchyChild.  # noqa: E501
        :type: list[WindowHierarchyChild]
        """

        self._children = children

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
        if issubclass(WindowHierarchyChild, dict):
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
        if not isinstance(other, WindowHierarchyChild):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
