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


class GetFwLeaderboardsCorporationsKills(object):
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
        'active_total': 'list[GetFwLeaderboardsCorporationsActiveTotal]',
        'last_week': 'list[GetFwLeaderboardsCorporationsLastWeek]',
        'yesterday': 'list[GetFwLeaderboardsCorporationsYesterday]'
    }

    attribute_map = {
        'active_total': 'active_total',
        'last_week': 'last_week',
        'yesterday': 'yesterday'
    }

    def __init__(self, active_total=None, last_week=None, yesterday=None):
        """
        GetFwLeaderboardsCorporationsKills - a model defined in Swagger
        """

        self._active_total = None
        self._last_week = None
        self._yesterday = None
        self.discriminator = None

        self.active_total = active_total
        self.last_week = last_week
        self.yesterday = yesterday

    @property
    def active_total(self):
        """
        Gets the active_total of this GetFwLeaderboardsCorporationsKills.
        Top 10 ranking of corporations active in faction warfare by total kills. A corporation is considered \"active\" if they have participated in faction warfare in the past 14 days.

        :return: The active_total of this GetFwLeaderboardsCorporationsKills.
        :rtype: list[GetFwLeaderboardsCorporationsActiveTotal]
        """
        return self._active_total

    @active_total.setter
    def active_total(self, active_total):
        """
        Sets the active_total of this GetFwLeaderboardsCorporationsKills.
        Top 10 ranking of corporations active in faction warfare by total kills. A corporation is considered \"active\" if they have participated in faction warfare in the past 14 days.

        :param active_total: The active_total of this GetFwLeaderboardsCorporationsKills.
        :type: list[GetFwLeaderboardsCorporationsActiveTotal]
        """
        if active_total is None:
            raise ValueError("Invalid value for `active_total`, must not be `None`")

        self._active_total = active_total

    @property
    def last_week(self):
        """
        Gets the last_week of this GetFwLeaderboardsCorporationsKills.
        Top 10 ranking of corporations by kills in the past week

        :return: The last_week of this GetFwLeaderboardsCorporationsKills.
        :rtype: list[GetFwLeaderboardsCorporationsLastWeek]
        """
        return self._last_week

    @last_week.setter
    def last_week(self, last_week):
        """
        Sets the last_week of this GetFwLeaderboardsCorporationsKills.
        Top 10 ranking of corporations by kills in the past week

        :param last_week: The last_week of this GetFwLeaderboardsCorporationsKills.
        :type: list[GetFwLeaderboardsCorporationsLastWeek]
        """
        if last_week is None:
            raise ValueError("Invalid value for `last_week`, must not be `None`")

        self._last_week = last_week

    @property
    def yesterday(self):
        """
        Gets the yesterday of this GetFwLeaderboardsCorporationsKills.
        Top 10 ranking of corporations by kills in the past day

        :return: The yesterday of this GetFwLeaderboardsCorporationsKills.
        :rtype: list[GetFwLeaderboardsCorporationsYesterday]
        """
        return self._yesterday

    @yesterday.setter
    def yesterday(self, yesterday):
        """
        Sets the yesterday of this GetFwLeaderboardsCorporationsKills.
        Top 10 ranking of corporations by kills in the past day

        :param yesterday: The yesterday of this GetFwLeaderboardsCorporationsKills.
        :type: list[GetFwLeaderboardsCorporationsYesterday]
        """
        if yesterday is None:
            raise ValueError("Invalid value for `yesterday`, must not be `None`")

        self._yesterday = yesterday

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
        if not isinstance(other, GetFwLeaderboardsCorporationsKills):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
