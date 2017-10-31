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


class GetSovereigntyMap200Ok(object):
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
        'alliance_id': 'int',
        'corporation_id': 'int',
        'faction_id': 'int',
        'system_id': 'int'
    }

    attribute_map = {
        'alliance_id': 'alliance_id',
        'corporation_id': 'corporation_id',
        'faction_id': 'faction_id',
        'system_id': 'system_id'
    }

    def __init__(self, alliance_id=None, corporation_id=None, faction_id=None, system_id=None):
        """
        GetSovereigntyMap200Ok - a model defined in Swagger
        """

        self._alliance_id = None
        self._corporation_id = None
        self._faction_id = None
        self._system_id = None
        self.discriminator = None

        if alliance_id is not None:
          self.alliance_id = alliance_id
        if corporation_id is not None:
          self.corporation_id = corporation_id
        if faction_id is not None:
          self.faction_id = faction_id
        self.system_id = system_id

    @property
    def alliance_id(self):
        """
        Gets the alliance_id of this GetSovereigntyMap200Ok.
        alliance_id integer

        :return: The alliance_id of this GetSovereigntyMap200Ok.
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """
        Sets the alliance_id of this GetSovereigntyMap200Ok.
        alliance_id integer

        :param alliance_id: The alliance_id of this GetSovereigntyMap200Ok.
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def corporation_id(self):
        """
        Gets the corporation_id of this GetSovereigntyMap200Ok.
        corporation_id integer

        :return: The corporation_id of this GetSovereigntyMap200Ok.
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """
        Sets the corporation_id of this GetSovereigntyMap200Ok.
        corporation_id integer

        :param corporation_id: The corporation_id of this GetSovereigntyMap200Ok.
        :type: int
        """

        self._corporation_id = corporation_id

    @property
    def faction_id(self):
        """
        Gets the faction_id of this GetSovereigntyMap200Ok.
        faction_id integer

        :return: The faction_id of this GetSovereigntyMap200Ok.
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """
        Sets the faction_id of this GetSovereigntyMap200Ok.
        faction_id integer

        :param faction_id: The faction_id of this GetSovereigntyMap200Ok.
        :type: int
        """

        self._faction_id = faction_id

    @property
    def system_id(self):
        """
        Gets the system_id of this GetSovereigntyMap200Ok.
        system_id integer

        :return: The system_id of this GetSovereigntyMap200Ok.
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """
        Sets the system_id of this GetSovereigntyMap200Ok.
        system_id integer

        :param system_id: The system_id of this GetSovereigntyMap200Ok.
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
        if not isinstance(other, GetSovereigntyMap200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
