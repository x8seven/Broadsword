# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetCorporationsCorporationIdBookmarks200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'bookmark_id': 'int',
        'coordinates': 'GetCorporationsCorporationIdBookmarksCoordinates',
        'created': 'datetime',
        'creator_id': 'int',
        'folder_id': 'int',
        'item': 'GetCorporationsCorporationIdBookmarksItem',
        'label': 'str',
        'location_id': 'int',
        'notes': 'str'
    }

    attribute_map = {
        'bookmark_id': 'bookmark_id',
        'coordinates': 'coordinates',
        'created': 'created',
        'creator_id': 'creator_id',
        'folder_id': 'folder_id',
        'item': 'item',
        'label': 'label',
        'location_id': 'location_id',
        'notes': 'notes'
    }

    def __init__(self, bookmark_id=None, coordinates=None, created=None, creator_id=None, folder_id=None, item=None, label=None, location_id=None, notes=None):
        """
        GetCorporationsCorporationIdBookmarks200Ok - a model defined in Swagger
        """

        self._bookmark_id = None
        self._coordinates = None
        self._created = None
        self._creator_id = None
        self._folder_id = None
        self._item = None
        self._label = None
        self._location_id = None
        self._notes = None
        self.discriminator = None

        self.bookmark_id = bookmark_id
        if coordinates is not None:
          self.coordinates = coordinates
        self.created = created
        self.creator_id = creator_id
        if folder_id is not None:
          self.folder_id = folder_id
        if item is not None:
          self.item = item
        self.label = label
        self.location_id = location_id
        self.notes = notes

    @property
    def bookmark_id(self):
        """
        Gets the bookmark_id of this GetCorporationsCorporationIdBookmarks200Ok.
        bookmark_id integer

        :return: The bookmark_id of this GetCorporationsCorporationIdBookmarks200Ok.
        :rtype: int
        """
        return self._bookmark_id

    @bookmark_id.setter
    def bookmark_id(self, bookmark_id):
        """
        Sets the bookmark_id of this GetCorporationsCorporationIdBookmarks200Ok.
        bookmark_id integer

        :param bookmark_id: The bookmark_id of this GetCorporationsCorporationIdBookmarks200Ok.
        :type: int
        """
        if bookmark_id is None:
            raise ValueError("Invalid value for `bookmark_id`, must not be `None`")

        self._bookmark_id = bookmark_id

    @property
    def coordinates(self):
        """
        Gets the coordinates of this GetCorporationsCorporationIdBookmarks200Ok.

        :return: The coordinates of this GetCorporationsCorporationIdBookmarks200Ok.
        :rtype: GetCorporationsCorporationIdBookmarksCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """
        Sets the coordinates of this GetCorporationsCorporationIdBookmarks200Ok.

        :param coordinates: The coordinates of this GetCorporationsCorporationIdBookmarks200Ok.
        :type: GetCorporationsCorporationIdBookmarksCoordinates
        """

        self._coordinates = coordinates

    @property
    def created(self):
        """
        Gets the created of this GetCorporationsCorporationIdBookmarks200Ok.
        created string

        :return: The created of this GetCorporationsCorporationIdBookmarks200Ok.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this GetCorporationsCorporationIdBookmarks200Ok.
        created string

        :param created: The created of this GetCorporationsCorporationIdBookmarks200Ok.
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created

    @property
    def creator_id(self):
        """
        Gets the creator_id of this GetCorporationsCorporationIdBookmarks200Ok.
        creator_id integer

        :return: The creator_id of this GetCorporationsCorporationIdBookmarks200Ok.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this GetCorporationsCorporationIdBookmarks200Ok.
        creator_id integer

        :param creator_id: The creator_id of this GetCorporationsCorporationIdBookmarks200Ok.
        :type: int
        """
        if creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")

        self._creator_id = creator_id

    @property
    def folder_id(self):
        """
        Gets the folder_id of this GetCorporationsCorporationIdBookmarks200Ok.
        folder_id integer

        :return: The folder_id of this GetCorporationsCorporationIdBookmarks200Ok.
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """
        Sets the folder_id of this GetCorporationsCorporationIdBookmarks200Ok.
        folder_id integer

        :param folder_id: The folder_id of this GetCorporationsCorporationIdBookmarks200Ok.
        :type: int
        """

        self._folder_id = folder_id

    @property
    def item(self):
        """
        Gets the item of this GetCorporationsCorporationIdBookmarks200Ok.

        :return: The item of this GetCorporationsCorporationIdBookmarks200Ok.
        :rtype: GetCorporationsCorporationIdBookmarksItem
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this GetCorporationsCorporationIdBookmarks200Ok.

        :param item: The item of this GetCorporationsCorporationIdBookmarks200Ok.
        :type: GetCorporationsCorporationIdBookmarksItem
        """

        self._item = item

    @property
    def label(self):
        """
        Gets the label of this GetCorporationsCorporationIdBookmarks200Ok.
        label string

        :return: The label of this GetCorporationsCorporationIdBookmarks200Ok.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this GetCorporationsCorporationIdBookmarks200Ok.
        label string

        :param label: The label of this GetCorporationsCorporationIdBookmarks200Ok.
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label

    @property
    def location_id(self):
        """
        Gets the location_id of this GetCorporationsCorporationIdBookmarks200Ok.
        location_id integer

        :return: The location_id of this GetCorporationsCorporationIdBookmarks200Ok.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this GetCorporationsCorporationIdBookmarks200Ok.
        location_id integer

        :param location_id: The location_id of this GetCorporationsCorporationIdBookmarks200Ok.
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")

        self._location_id = location_id

    @property
    def notes(self):
        """
        Gets the notes of this GetCorporationsCorporationIdBookmarks200Ok.
        notes string

        :return: The notes of this GetCorporationsCorporationIdBookmarks200Ok.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this GetCorporationsCorporationIdBookmarks200Ok.
        notes string

        :param notes: The notes of this GetCorporationsCorporationIdBookmarks200Ok.
        :type: str
        """
        if notes is None:
            raise ValueError("Invalid value for `notes`, must not be `None`")

        self._notes = notes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetCorporationsCorporationIdBookmarks200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
