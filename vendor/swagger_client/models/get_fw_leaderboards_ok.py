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


class GetFwLeaderboardsOk(object):
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
        'kills': 'GetFwLeaderboardsKills',
        'victory_points': 'GetFwLeaderboardsVictoryPoints'
    }

    attribute_map = {
        'kills': 'kills',
        'victory_points': 'victory_points'
    }

    def __init__(self, kills=None, victory_points=None):
        """
        GetFwLeaderboardsOk - a model defined in Swagger
        """

        self._kills = None
        self._victory_points = None
        self.discriminator = None

        self.kills = kills
        self.victory_points = victory_points

    @property
    def kills(self):
        """
        Gets the kills of this GetFwLeaderboardsOk.

        :return: The kills of this GetFwLeaderboardsOk.
        :rtype: GetFwLeaderboardsKills
        """
        return self._kills

    @kills.setter
    def kills(self, kills):
        """
        Sets the kills of this GetFwLeaderboardsOk.

        :param kills: The kills of this GetFwLeaderboardsOk.
        :type: GetFwLeaderboardsKills
        """
        if kills is None:
            raise ValueError("Invalid value for `kills`, must not be `None`")

        self._kills = kills

    @property
    def victory_points(self):
        """
        Gets the victory_points of this GetFwLeaderboardsOk.

        :return: The victory_points of this GetFwLeaderboardsOk.
        :rtype: GetFwLeaderboardsVictoryPoints
        """
        return self._victory_points

    @victory_points.setter
    def victory_points(self, victory_points):
        """
        Sets the victory_points of this GetFwLeaderboardsOk.

        :param victory_points: The victory_points of this GetFwLeaderboardsOk.
        :type: GetFwLeaderboardsVictoryPoints
        """
        if victory_points is None:
            raise ValueError("Invalid value for `victory_points`, must not be `None`")

        self._victory_points = victory_points

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
        if not isinstance(other, GetFwLeaderboardsOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
