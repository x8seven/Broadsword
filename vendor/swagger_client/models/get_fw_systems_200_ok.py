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


class GetFwSystems200Ok(object):
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
        'solar_system_id': 'int',
        'owner_faction_id': 'int',
        'occupier_faction_id': 'int',
        'victory_points': 'int',
        'victory_points_threshold': 'int',
        'contested': 'bool'
    }

    attribute_map = {
        'solar_system_id': 'solar_system_id',
        'owner_faction_id': 'owner_faction_id',
        'occupier_faction_id': 'occupier_faction_id',
        'victory_points': 'victory_points',
        'victory_points_threshold': 'victory_points_threshold',
        'contested': 'contested'
    }

    def __init__(self, solar_system_id=None, owner_faction_id=None, occupier_faction_id=None, victory_points=None, victory_points_threshold=None, contested=None):
        """
        GetFwSystems200Ok - a model defined in Swagger
        """

        self._solar_system_id = None
        self._owner_faction_id = None
        self._occupier_faction_id = None
        self._victory_points = None
        self._victory_points_threshold = None
        self._contested = None
        self.discriminator = None

        self.solar_system_id = solar_system_id
        self.owner_faction_id = owner_faction_id
        self.occupier_faction_id = occupier_faction_id
        self.victory_points = victory_points
        self.victory_points_threshold = victory_points_threshold
        self.contested = contested

    @property
    def solar_system_id(self):
        """
        Gets the solar_system_id of this GetFwSystems200Ok.
        solar_system_id integer

        :return: The solar_system_id of this GetFwSystems200Ok.
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """
        Sets the solar_system_id of this GetFwSystems200Ok.
        solar_system_id integer

        :param solar_system_id: The solar_system_id of this GetFwSystems200Ok.
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")

        self._solar_system_id = solar_system_id

    @property
    def owner_faction_id(self):
        """
        Gets the owner_faction_id of this GetFwSystems200Ok.
        owner_faction_id integer

        :return: The owner_faction_id of this GetFwSystems200Ok.
        :rtype: int
        """
        return self._owner_faction_id

    @owner_faction_id.setter
    def owner_faction_id(self, owner_faction_id):
        """
        Sets the owner_faction_id of this GetFwSystems200Ok.
        owner_faction_id integer

        :param owner_faction_id: The owner_faction_id of this GetFwSystems200Ok.
        :type: int
        """
        if owner_faction_id is None:
            raise ValueError("Invalid value for `owner_faction_id`, must not be `None`")

        self._owner_faction_id = owner_faction_id

    @property
    def occupier_faction_id(self):
        """
        Gets the occupier_faction_id of this GetFwSystems200Ok.
        occupier_faction_id integer

        :return: The occupier_faction_id of this GetFwSystems200Ok.
        :rtype: int
        """
        return self._occupier_faction_id

    @occupier_faction_id.setter
    def occupier_faction_id(self, occupier_faction_id):
        """
        Sets the occupier_faction_id of this GetFwSystems200Ok.
        occupier_faction_id integer

        :param occupier_faction_id: The occupier_faction_id of this GetFwSystems200Ok.
        :type: int
        """
        if occupier_faction_id is None:
            raise ValueError("Invalid value for `occupier_faction_id`, must not be `None`")

        self._occupier_faction_id = occupier_faction_id

    @property
    def victory_points(self):
        """
        Gets the victory_points of this GetFwSystems200Ok.
        victory_points integer

        :return: The victory_points of this GetFwSystems200Ok.
        :rtype: int
        """
        return self._victory_points

    @victory_points.setter
    def victory_points(self, victory_points):
        """
        Sets the victory_points of this GetFwSystems200Ok.
        victory_points integer

        :param victory_points: The victory_points of this GetFwSystems200Ok.
        :type: int
        """
        if victory_points is None:
            raise ValueError("Invalid value for `victory_points`, must not be `None`")

        self._victory_points = victory_points

    @property
    def victory_points_threshold(self):
        """
        Gets the victory_points_threshold of this GetFwSystems200Ok.
        victory_points_threshold integer

        :return: The victory_points_threshold of this GetFwSystems200Ok.
        :rtype: int
        """
        return self._victory_points_threshold

    @victory_points_threshold.setter
    def victory_points_threshold(self, victory_points_threshold):
        """
        Sets the victory_points_threshold of this GetFwSystems200Ok.
        victory_points_threshold integer

        :param victory_points_threshold: The victory_points_threshold of this GetFwSystems200Ok.
        :type: int
        """
        if victory_points_threshold is None:
            raise ValueError("Invalid value for `victory_points_threshold`, must not be `None`")

        self._victory_points_threshold = victory_points_threshold

    @property
    def contested(self):
        """
        Gets the contested of this GetFwSystems200Ok.
        contested boolean

        :return: The contested of this GetFwSystems200Ok.
        :rtype: bool
        """
        return self._contested

    @contested.setter
    def contested(self, contested):
        """
        Sets the contested of this GetFwSystems200Ok.
        contested boolean

        :param contested: The contested of this GetFwSystems200Ok.
        :type: bool
        """
        if contested is None:
            raise ValueError("Invalid value for `contested`, must not be `None`")

        self._contested = contested

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
        if not isinstance(other, GetFwSystems200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
