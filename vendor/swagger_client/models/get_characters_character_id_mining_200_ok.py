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


class GetCharactersCharacterIdMining200Ok(object):
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
        'date': 'date',
        'quantity': 'int',
        'solar_system_id': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'date': 'date',
        'quantity': 'quantity',
        'solar_system_id': 'solar_system_id',
        'type_id': 'type_id'
    }

    def __init__(self, date=None, quantity=None, solar_system_id=None, type_id=None):
        """
        GetCharactersCharacterIdMining200Ok - a model defined in Swagger
        """

        self._date = None
        self._quantity = None
        self._solar_system_id = None
        self._type_id = None
        self.discriminator = None

        self.date = date
        self.quantity = quantity
        self.solar_system_id = solar_system_id
        self.type_id = type_id

    @property
    def date(self):
        """
        Gets the date of this GetCharactersCharacterIdMining200Ok.
        date string

        :return: The date of this GetCharactersCharacterIdMining200Ok.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this GetCharactersCharacterIdMining200Ok.
        date string

        :param date: The date of this GetCharactersCharacterIdMining200Ok.
        :type: date
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")

        self._date = date

    @property
    def quantity(self):
        """
        Gets the quantity of this GetCharactersCharacterIdMining200Ok.
        quantity integer

        :return: The quantity of this GetCharactersCharacterIdMining200Ok.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this GetCharactersCharacterIdMining200Ok.
        quantity integer

        :param quantity: The quantity of this GetCharactersCharacterIdMining200Ok.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

    @property
    def solar_system_id(self):
        """
        Gets the solar_system_id of this GetCharactersCharacterIdMining200Ok.
        solar_system_id integer

        :return: The solar_system_id of this GetCharactersCharacterIdMining200Ok.
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """
        Sets the solar_system_id of this GetCharactersCharacterIdMining200Ok.
        solar_system_id integer

        :param solar_system_id: The solar_system_id of this GetCharactersCharacterIdMining200Ok.
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")

        self._solar_system_id = solar_system_id

    @property
    def type_id(self):
        """
        Gets the type_id of this GetCharactersCharacterIdMining200Ok.
        type_id integer

        :return: The type_id of this GetCharactersCharacterIdMining200Ok.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetCharactersCharacterIdMining200Ok.
        type_id integer

        :param type_id: The type_id of this GetCharactersCharacterIdMining200Ok.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

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
        if not isinstance(other, GetCharactersCharacterIdMining200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
