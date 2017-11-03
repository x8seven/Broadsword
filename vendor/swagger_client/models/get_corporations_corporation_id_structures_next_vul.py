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


class GetCorporationsCorporationIdStructuresNextVul(object):
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
        'day': 'int',
        'hour': 'int'
    }

    attribute_map = {
        'day': 'day',
        'hour': 'hour'
    }

    def __init__(self, day=None, hour=None):
        """
        GetCorporationsCorporationIdStructuresNextVul - a model defined in Swagger
        """

        self._day = None
        self._hour = None
        self.discriminator = None

        self.day = day
        self.hour = hour

    @property
    def day(self):
        """
        Gets the day of this GetCorporationsCorporationIdStructuresNextVul.
        day integer

        :return: The day of this GetCorporationsCorporationIdStructuresNextVul.
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """
        Sets the day of this GetCorporationsCorporationIdStructuresNextVul.
        day integer

        :param day: The day of this GetCorporationsCorporationIdStructuresNextVul.
        :type: int
        """
        if day is None:
            raise ValueError("Invalid value for `day`, must not be `None`")

        self._day = day

    @property
    def hour(self):
        """
        Gets the hour of this GetCorporationsCorporationIdStructuresNextVul.
        hour integer

        :return: The hour of this GetCorporationsCorporationIdStructuresNextVul.
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """
        Sets the hour of this GetCorporationsCorporationIdStructuresNextVul.
        hour integer

        :param hour: The hour of this GetCorporationsCorporationIdStructuresNextVul.
        :type: int
        """
        if hour is None:
            raise ValueError("Invalid value for `hour`, must not be `None`")

        self._hour = hour

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
        if not isinstance(other, GetCorporationsCorporationIdStructuresNextVul):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
