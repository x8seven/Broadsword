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


class GetFwStatsVictoryPoints(object):
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
        'last_week': 'int',
        'total': 'int',
        'yesterday': 'int'
    }

    attribute_map = {
        'last_week': 'last_week',
        'total': 'total',
        'yesterday': 'yesterday'
    }

    def __init__(self, last_week=None, total=None, yesterday=None):
        """
        GetFwStatsVictoryPoints - a model defined in Swagger
        """

        self._last_week = None
        self._total = None
        self._yesterday = None
        self.discriminator = None

        self.last_week = last_week
        self.total = total
        self.yesterday = yesterday

    @property
    def last_week(self):
        """
        Gets the last_week of this GetFwStatsVictoryPoints.
        Last week's victory points gained

        :return: The last_week of this GetFwStatsVictoryPoints.
        :rtype: int
        """
        return self._last_week

    @last_week.setter
    def last_week(self, last_week):
        """
        Sets the last_week of this GetFwStatsVictoryPoints.
        Last week's victory points gained

        :param last_week: The last_week of this GetFwStatsVictoryPoints.
        :type: int
        """
        if last_week is None:
            raise ValueError("Invalid value for `last_week`, must not be `None`")

        self._last_week = last_week

    @property
    def total(self):
        """
        Gets the total of this GetFwStatsVictoryPoints.
        Total victory points gained since faction warfare began

        :return: The total of this GetFwStatsVictoryPoints.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this GetFwStatsVictoryPoints.
        Total victory points gained since faction warfare began

        :param total: The total of this GetFwStatsVictoryPoints.
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")

        self._total = total

    @property
    def yesterday(self):
        """
        Gets the yesterday of this GetFwStatsVictoryPoints.
        Yesterday's victory points gained

        :return: The yesterday of this GetFwStatsVictoryPoints.
        :rtype: int
        """
        return self._yesterday

    @yesterday.setter
    def yesterday(self, yesterday):
        """
        Sets the yesterday of this GetFwStatsVictoryPoints.
        Yesterday's victory points gained

        :param yesterday: The yesterday of this GetFwStatsVictoryPoints.
        :type: int
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
        if not isinstance(other, GetFwStatsVictoryPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
