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


class GetUniverseSystemJumps200Ok(object):
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
        'ship_jumps': 'int',
        'system_id': 'int'
    }

    attribute_map = {
        'ship_jumps': 'ship_jumps',
        'system_id': 'system_id'
    }

    def __init__(self, ship_jumps=None, system_id=None):
        """
        GetUniverseSystemJumps200Ok - a model defined in Swagger
        """

        self._ship_jumps = None
        self._system_id = None
        self.discriminator = None

        self.ship_jumps = ship_jumps
        self.system_id = system_id

    @property
    def ship_jumps(self):
        """
        Gets the ship_jumps of this GetUniverseSystemJumps200Ok.
        ship_jumps integer

        :return: The ship_jumps of this GetUniverseSystemJumps200Ok.
        :rtype: int
        """
        return self._ship_jumps

    @ship_jumps.setter
    def ship_jumps(self, ship_jumps):
        """
        Sets the ship_jumps of this GetUniverseSystemJumps200Ok.
        ship_jumps integer

        :param ship_jumps: The ship_jumps of this GetUniverseSystemJumps200Ok.
        :type: int
        """
        if ship_jumps is None:
            raise ValueError("Invalid value for `ship_jumps`, must not be `None`")

        self._ship_jumps = ship_jumps

    @property
    def system_id(self):
        """
        Gets the system_id of this GetUniverseSystemJumps200Ok.
        system_id integer

        :return: The system_id of this GetUniverseSystemJumps200Ok.
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """
        Sets the system_id of this GetUniverseSystemJumps200Ok.
        system_id integer

        :param system_id: The system_id of this GetUniverseSystemJumps200Ok.
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")

        self._system_id = system_id

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
        if not isinstance(other, GetUniverseSystemJumps200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
