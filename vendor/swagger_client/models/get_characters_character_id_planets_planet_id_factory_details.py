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


class GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails(object):
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
        'schematic_id': 'int'
    }

    attribute_map = {
        'schematic_id': 'schematic_id'
    }

    def __init__(self, schematic_id=None):
        """
        GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails - a model defined in Swagger
        """

        self._schematic_id = None
        self.discriminator = None

        self.schematic_id = schematic_id

    @property
    def schematic_id(self):
        """
        Gets the schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails.
        schematic_id integer

        :return: The schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails.
        :rtype: int
        """
        return self._schematic_id

    @schematic_id.setter
    def schematic_id(self, schematic_id):
        """
        Sets the schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails.
        schematic_id integer

        :param schematic_id: The schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails.
        :type: int
        """
        if schematic_id is None:
            raise ValueError("Invalid value for `schematic_id`, must not be `None`")

        self._schematic_id = schematic_id

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
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
