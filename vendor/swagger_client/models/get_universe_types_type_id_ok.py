# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetUniverseTypesTypeIdOk(object):
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
        'type_id': 'int',
        'name': 'str',
        'description': 'str',
        'published': 'bool',
        'group_id': 'int',
        'market_group_id': 'int',
        'radius': 'float',
        'volume': 'float',
        'packaged_volume': 'float',
        'icon_id': 'int',
        'capacity': 'float',
        'portion_size': 'int',
        'mass': 'float',
        'graphic_id': 'int',
        'dogma_attributes': 'list[GetUniverseTypesTypeIdDogmaAttribute]',
        'dogma_effects': 'list[GetUniverseTypesTypeIdDogmaEffect]'
    }

    attribute_map = {
        'type_id': 'type_id',
        'name': 'name',
        'description': 'description',
        'published': 'published',
        'group_id': 'group_id',
        'market_group_id': 'market_group_id',
        'radius': 'radius',
        'volume': 'volume',
        'packaged_volume': 'packaged_volume',
        'icon_id': 'icon_id',
        'capacity': 'capacity',
        'portion_size': 'portion_size',
        'mass': 'mass',
        'graphic_id': 'graphic_id',
        'dogma_attributes': 'dogma_attributes',
        'dogma_effects': 'dogma_effects'
    }

    def __init__(self, type_id=None, name=None, description=None, published=None, group_id=None, market_group_id=None, radius=None, volume=None, packaged_volume=None, icon_id=None, capacity=None, portion_size=None, mass=None, graphic_id=None, dogma_attributes=None, dogma_effects=None):
        """
        GetUniverseTypesTypeIdOk - a model defined in Swagger
        """

        self._type_id = None
        self._name = None
        self._description = None
        self._published = None
        self._group_id = None
        self._market_group_id = None
        self._radius = None
        self._volume = None
        self._packaged_volume = None
        self._icon_id = None
        self._capacity = None
        self._portion_size = None
        self._mass = None
        self._graphic_id = None
        self._dogma_attributes = None
        self._dogma_effects = None
        self.discriminator = None

        self.type_id = type_id
        self.name = name
        self.description = description
        self.published = published
        self.group_id = group_id
        if market_group_id is not None:
          self.market_group_id = market_group_id
        if radius is not None:
          self.radius = radius
        if volume is not None:
          self.volume = volume
        if packaged_volume is not None:
          self.packaged_volume = packaged_volume
        if icon_id is not None:
          self.icon_id = icon_id
        if capacity is not None:
          self.capacity = capacity
        if portion_size is not None:
          self.portion_size = portion_size
        if mass is not None:
          self.mass = mass
        if graphic_id is not None:
          self.graphic_id = graphic_id
        if dogma_attributes is not None:
          self.dogma_attributes = dogma_attributes
        if dogma_effects is not None:
          self.dogma_effects = dogma_effects

    @property
    def type_id(self):
        """
        Gets the type_id of this GetUniverseTypesTypeIdOk.
        type_id integer

        :return: The type_id of this GetUniverseTypesTypeIdOk.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetUniverseTypesTypeIdOk.
        type_id integer

        :param type_id: The type_id of this GetUniverseTypesTypeIdOk.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

    @property
    def name(self):
        """
        Gets the name of this GetUniverseTypesTypeIdOk.
        name string

        :return: The name of this GetUniverseTypesTypeIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetUniverseTypesTypeIdOk.
        name string

        :param name: The name of this GetUniverseTypesTypeIdOk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this GetUniverseTypesTypeIdOk.
        description string

        :return: The description of this GetUniverseTypesTypeIdOk.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GetUniverseTypesTypeIdOk.
        description string

        :param description: The description of this GetUniverseTypesTypeIdOk.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def published(self):
        """
        Gets the published of this GetUniverseTypesTypeIdOk.
        published boolean

        :return: The published of this GetUniverseTypesTypeIdOk.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this GetUniverseTypesTypeIdOk.
        published boolean

        :param published: The published of this GetUniverseTypesTypeIdOk.
        :type: bool
        """
        if published is None:
            raise ValueError("Invalid value for `published`, must not be `None`")

        self._published = published

    @property
    def group_id(self):
        """
        Gets the group_id of this GetUniverseTypesTypeIdOk.
        group_id integer

        :return: The group_id of this GetUniverseTypesTypeIdOk.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this GetUniverseTypesTypeIdOk.
        group_id integer

        :param group_id: The group_id of this GetUniverseTypesTypeIdOk.
        :type: int
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")

        self._group_id = group_id

    @property
    def market_group_id(self):
        """
        Gets the market_group_id of this GetUniverseTypesTypeIdOk.
        This only exists for types that can be put on the market

        :return: The market_group_id of this GetUniverseTypesTypeIdOk.
        :rtype: int
        """
        return self._market_group_id

    @market_group_id.setter
    def market_group_id(self, market_group_id):
        """
        Sets the market_group_id of this GetUniverseTypesTypeIdOk.
        This only exists for types that can be put on the market

        :param market_group_id: The market_group_id of this GetUniverseTypesTypeIdOk.
        :type: int
        """

        self._market_group_id = market_group_id

    @property
    def radius(self):
        """
        Gets the radius of this GetUniverseTypesTypeIdOk.
        radius number

        :return: The radius of this GetUniverseTypesTypeIdOk.
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """
        Sets the radius of this GetUniverseTypesTypeIdOk.
        radius number

        :param radius: The radius of this GetUniverseTypesTypeIdOk.
        :type: float
        """

        self._radius = radius

    @property
    def volume(self):
        """
        Gets the volume of this GetUniverseTypesTypeIdOk.
        volume number

        :return: The volume of this GetUniverseTypesTypeIdOk.
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """
        Sets the volume of this GetUniverseTypesTypeIdOk.
        volume number

        :param volume: The volume of this GetUniverseTypesTypeIdOk.
        :type: float
        """

        self._volume = volume

    @property
    def packaged_volume(self):
        """
        Gets the packaged_volume of this GetUniverseTypesTypeIdOk.
        packaged_volume number

        :return: The packaged_volume of this GetUniverseTypesTypeIdOk.
        :rtype: float
        """
        return self._packaged_volume

    @packaged_volume.setter
    def packaged_volume(self, packaged_volume):
        """
        Sets the packaged_volume of this GetUniverseTypesTypeIdOk.
        packaged_volume number

        :param packaged_volume: The packaged_volume of this GetUniverseTypesTypeIdOk.
        :type: float
        """

        self._packaged_volume = packaged_volume

    @property
    def icon_id(self):
        """
        Gets the icon_id of this GetUniverseTypesTypeIdOk.
        icon_id integer

        :return: The icon_id of this GetUniverseTypesTypeIdOk.
        :rtype: int
        """
        return self._icon_id

    @icon_id.setter
    def icon_id(self, icon_id):
        """
        Sets the icon_id of this GetUniverseTypesTypeIdOk.
        icon_id integer

        :param icon_id: The icon_id of this GetUniverseTypesTypeIdOk.
        :type: int
        """

        self._icon_id = icon_id

    @property
    def capacity(self):
        """
        Gets the capacity of this GetUniverseTypesTypeIdOk.
        capacity number

        :return: The capacity of this GetUniverseTypesTypeIdOk.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this GetUniverseTypesTypeIdOk.
        capacity number

        :param capacity: The capacity of this GetUniverseTypesTypeIdOk.
        :type: float
        """

        self._capacity = capacity

    @property
    def portion_size(self):
        """
        Gets the portion_size of this GetUniverseTypesTypeIdOk.
        portion_size integer

        :return: The portion_size of this GetUniverseTypesTypeIdOk.
        :rtype: int
        """
        return self._portion_size

    @portion_size.setter
    def portion_size(self, portion_size):
        """
        Sets the portion_size of this GetUniverseTypesTypeIdOk.
        portion_size integer

        :param portion_size: The portion_size of this GetUniverseTypesTypeIdOk.
        :type: int
        """

        self._portion_size = portion_size

    @property
    def mass(self):
        """
        Gets the mass of this GetUniverseTypesTypeIdOk.
        mass number

        :return: The mass of this GetUniverseTypesTypeIdOk.
        :rtype: float
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """
        Sets the mass of this GetUniverseTypesTypeIdOk.
        mass number

        :param mass: The mass of this GetUniverseTypesTypeIdOk.
        :type: float
        """

        self._mass = mass

    @property
    def graphic_id(self):
        """
        Gets the graphic_id of this GetUniverseTypesTypeIdOk.
        graphic_id integer

        :return: The graphic_id of this GetUniverseTypesTypeIdOk.
        :rtype: int
        """
        return self._graphic_id

    @graphic_id.setter
    def graphic_id(self, graphic_id):
        """
        Sets the graphic_id of this GetUniverseTypesTypeIdOk.
        graphic_id integer

        :param graphic_id: The graphic_id of this GetUniverseTypesTypeIdOk.
        :type: int
        """

        self._graphic_id = graphic_id

    @property
    def dogma_attributes(self):
        """
        Gets the dogma_attributes of this GetUniverseTypesTypeIdOk.
        dogma_attributes array

        :return: The dogma_attributes of this GetUniverseTypesTypeIdOk.
        :rtype: list[GetUniverseTypesTypeIdDogmaAttribute]
        """
        return self._dogma_attributes

    @dogma_attributes.setter
    def dogma_attributes(self, dogma_attributes):
        """
        Sets the dogma_attributes of this GetUniverseTypesTypeIdOk.
        dogma_attributes array

        :param dogma_attributes: The dogma_attributes of this GetUniverseTypesTypeIdOk.
        :type: list[GetUniverseTypesTypeIdDogmaAttribute]
        """

        self._dogma_attributes = dogma_attributes

    @property
    def dogma_effects(self):
        """
        Gets the dogma_effects of this GetUniverseTypesTypeIdOk.
        dogma_effects array

        :return: The dogma_effects of this GetUniverseTypesTypeIdOk.
        :rtype: list[GetUniverseTypesTypeIdDogmaEffect]
        """
        return self._dogma_effects

    @dogma_effects.setter
    def dogma_effects(self, dogma_effects):
        """
        Sets the dogma_effects of this GetUniverseTypesTypeIdOk.
        dogma_effects array

        :param dogma_effects: The dogma_effects of this GetUniverseTypesTypeIdOk.
        :type: list[GetUniverseTypesTypeIdDogmaEffect]
        """

        self._dogma_effects = dogma_effects

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
        if not isinstance(other, GetUniverseTypesTypeIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
