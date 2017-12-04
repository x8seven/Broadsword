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


class GetCorporationsCorporationIdCustomsOffices200Ok(object):
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
        'office_id': 'int',
        'system_id': 'int',
        'reinforce_exit_start': 'int',
        'reinforce_exit_end': 'int',
        'corporation_tax_rate': 'float',
        'allow_alliance_access': 'bool',
        'alliance_tax_rate': 'float',
        'allow_access_with_standings': 'bool',
        'standing_level': 'str',
        'excellent_standing_tax_rate': 'float',
        'good_standing_tax_rate': 'float',
        'neutral_standing_tax_rate': 'float',
        'bad_standing_tax_rate': 'float',
        'terrible_standing_tax_rate': 'float'
    }

    attribute_map = {
        'office_id': 'office_id',
        'system_id': 'system_id',
        'reinforce_exit_start': 'reinforce_exit_start',
        'reinforce_exit_end': 'reinforce_exit_end',
        'corporation_tax_rate': 'corporation_tax_rate',
        'allow_alliance_access': 'allow_alliance_access',
        'alliance_tax_rate': 'alliance_tax_rate',
        'allow_access_with_standings': 'allow_access_with_standings',
        'standing_level': 'standing_level',
        'excellent_standing_tax_rate': 'excellent_standing_tax_rate',
        'good_standing_tax_rate': 'good_standing_tax_rate',
        'neutral_standing_tax_rate': 'neutral_standing_tax_rate',
        'bad_standing_tax_rate': 'bad_standing_tax_rate',
        'terrible_standing_tax_rate': 'terrible_standing_tax_rate'
    }

    def __init__(self, office_id=None, system_id=None, reinforce_exit_start=None, reinforce_exit_end=None, corporation_tax_rate=None, allow_alliance_access=None, alliance_tax_rate=None, allow_access_with_standings=None, standing_level=None, excellent_standing_tax_rate=None, good_standing_tax_rate=None, neutral_standing_tax_rate=None, bad_standing_tax_rate=None, terrible_standing_tax_rate=None):
        """
        GetCorporationsCorporationIdCustomsOffices200Ok - a model defined in Swagger
        """

        self._office_id = None
        self._system_id = None
        self._reinforce_exit_start = None
        self._reinforce_exit_end = None
        self._corporation_tax_rate = None
        self._allow_alliance_access = None
        self._alliance_tax_rate = None
        self._allow_access_with_standings = None
        self._standing_level = None
        self._excellent_standing_tax_rate = None
        self._good_standing_tax_rate = None
        self._neutral_standing_tax_rate = None
        self._bad_standing_tax_rate = None
        self._terrible_standing_tax_rate = None
        self.discriminator = None

        self.office_id = office_id
        self.system_id = system_id
        self.reinforce_exit_start = reinforce_exit_start
        self.reinforce_exit_end = reinforce_exit_end
        if corporation_tax_rate is not None:
          self.corporation_tax_rate = corporation_tax_rate
        self.allow_alliance_access = allow_alliance_access
        if alliance_tax_rate is not None:
          self.alliance_tax_rate = alliance_tax_rate
        self.allow_access_with_standings = allow_access_with_standings
        if standing_level is not None:
          self.standing_level = standing_level
        if excellent_standing_tax_rate is not None:
          self.excellent_standing_tax_rate = excellent_standing_tax_rate
        if good_standing_tax_rate is not None:
          self.good_standing_tax_rate = good_standing_tax_rate
        if neutral_standing_tax_rate is not None:
          self.neutral_standing_tax_rate = neutral_standing_tax_rate
        if bad_standing_tax_rate is not None:
          self.bad_standing_tax_rate = bad_standing_tax_rate
        if terrible_standing_tax_rate is not None:
          self.terrible_standing_tax_rate = terrible_standing_tax_rate

    @property
    def office_id(self):
        """
        Gets the office_id of this GetCorporationsCorporationIdCustomsOffices200Ok.
        unique ID of this customs office

        :return: The office_id of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """
        Sets the office_id of this GetCorporationsCorporationIdCustomsOffices200Ok.
        unique ID of this customs office

        :param office_id: The office_id of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: int
        """
        if office_id is None:
            raise ValueError("Invalid value for `office_id`, must not be `None`")

        self._office_id = office_id

    @property
    def system_id(self):
        """
        Gets the system_id of this GetCorporationsCorporationIdCustomsOffices200Ok.
        ID of the solar system this customs office is located in

        :return: The system_id of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """
        Sets the system_id of this GetCorporationsCorporationIdCustomsOffices200Ok.
        ID of the solar system this customs office is located in

        :param system_id: The system_id of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")

        self._system_id = system_id

    @property
    def reinforce_exit_start(self):
        """
        Gets the reinforce_exit_start of this GetCorporationsCorporationIdCustomsOffices200Ok.
        Together with reinforce_exit_end, marks a 2-hour period where this customs office could exit reinforcement mode during the day after initial attack

        :return: The reinforce_exit_start of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: int
        """
        return self._reinforce_exit_start

    @reinforce_exit_start.setter
    def reinforce_exit_start(self, reinforce_exit_start):
        """
        Sets the reinforce_exit_start of this GetCorporationsCorporationIdCustomsOffices200Ok.
        Together with reinforce_exit_end, marks a 2-hour period where this customs office could exit reinforcement mode during the day after initial attack

        :param reinforce_exit_start: The reinforce_exit_start of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: int
        """
        if reinforce_exit_start is None:
            raise ValueError("Invalid value for `reinforce_exit_start`, must not be `None`")
        if reinforce_exit_start is not None and reinforce_exit_start > 23:
            raise ValueError("Invalid value for `reinforce_exit_start`, must be a value less than or equal to `23`")
        if reinforce_exit_start is not None and reinforce_exit_start < 0:
            raise ValueError("Invalid value for `reinforce_exit_start`, must be a value greater than or equal to `0`")

        self._reinforce_exit_start = reinforce_exit_start

    @property
    def reinforce_exit_end(self):
        """
        Gets the reinforce_exit_end of this GetCorporationsCorporationIdCustomsOffices200Ok.
        reinforce_exit_end integer

        :return: The reinforce_exit_end of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: int
        """
        return self._reinforce_exit_end

    @reinforce_exit_end.setter
    def reinforce_exit_end(self, reinforce_exit_end):
        """
        Sets the reinforce_exit_end of this GetCorporationsCorporationIdCustomsOffices200Ok.
        reinforce_exit_end integer

        :param reinforce_exit_end: The reinforce_exit_end of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: int
        """
        if reinforce_exit_end is None:
            raise ValueError("Invalid value for `reinforce_exit_end`, must not be `None`")
        if reinforce_exit_end is not None and reinforce_exit_end > 23:
            raise ValueError("Invalid value for `reinforce_exit_end`, must be a value less than or equal to `23`")
        if reinforce_exit_end is not None and reinforce_exit_end < 0:
            raise ValueError("Invalid value for `reinforce_exit_end`, must be a value greater than or equal to `0`")

        self._reinforce_exit_end = reinforce_exit_end

    @property
    def corporation_tax_rate(self):
        """
        Gets the corporation_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        corporation_tax_rate number

        :return: The corporation_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: float
        """
        return self._corporation_tax_rate

    @corporation_tax_rate.setter
    def corporation_tax_rate(self, corporation_tax_rate):
        """
        Sets the corporation_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        corporation_tax_rate number

        :param corporation_tax_rate: The corporation_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: float
        """

        self._corporation_tax_rate = corporation_tax_rate

    @property
    def allow_alliance_access(self):
        """
        Gets the allow_alliance_access of this GetCorporationsCorporationIdCustomsOffices200Ok.
        allow_alliance_access boolean

        :return: The allow_alliance_access of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: bool
        """
        return self._allow_alliance_access

    @allow_alliance_access.setter
    def allow_alliance_access(self, allow_alliance_access):
        """
        Sets the allow_alliance_access of this GetCorporationsCorporationIdCustomsOffices200Ok.
        allow_alliance_access boolean

        :param allow_alliance_access: The allow_alliance_access of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: bool
        """
        if allow_alliance_access is None:
            raise ValueError("Invalid value for `allow_alliance_access`, must not be `None`")

        self._allow_alliance_access = allow_alliance_access

    @property
    def alliance_tax_rate(self):
        """
        Gets the alliance_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        Only present if alliance access is allowed

        :return: The alliance_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: float
        """
        return self._alliance_tax_rate

    @alliance_tax_rate.setter
    def alliance_tax_rate(self, alliance_tax_rate):
        """
        Sets the alliance_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        Only present if alliance access is allowed

        :param alliance_tax_rate: The alliance_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: float
        """

        self._alliance_tax_rate = alliance_tax_rate

    @property
    def allow_access_with_standings(self):
        """
        Gets the allow_access_with_standings of this GetCorporationsCorporationIdCustomsOffices200Ok.
        standing_level and any standing related tax rate only present when this is true

        :return: The allow_access_with_standings of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: bool
        """
        return self._allow_access_with_standings

    @allow_access_with_standings.setter
    def allow_access_with_standings(self, allow_access_with_standings):
        """
        Sets the allow_access_with_standings of this GetCorporationsCorporationIdCustomsOffices200Ok.
        standing_level and any standing related tax rate only present when this is true

        :param allow_access_with_standings: The allow_access_with_standings of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: bool
        """
        if allow_access_with_standings is None:
            raise ValueError("Invalid value for `allow_access_with_standings`, must not be `None`")

        self._allow_access_with_standings = allow_access_with_standings

    @property
    def standing_level(self):
        """
        Gets the standing_level of this GetCorporationsCorporationIdCustomsOffices200Ok.
        Access is allowed only for entities with this level of standing or better

        :return: The standing_level of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: str
        """
        return self._standing_level

    @standing_level.setter
    def standing_level(self, standing_level):
        """
        Sets the standing_level of this GetCorporationsCorporationIdCustomsOffices200Ok.
        Access is allowed only for entities with this level of standing or better

        :param standing_level: The standing_level of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: str
        """
        allowed_values = ["bad", "excellent", "good", "neutral", "terrible"]
        if standing_level not in allowed_values:
            raise ValueError(
                "Invalid value for `standing_level` ({0}), must be one of {1}"
                .format(standing_level, allowed_values)
            )

        self._standing_level = standing_level

    @property
    def excellent_standing_tax_rate(self):
        """
        Gets the excellent_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        Tax rate for entities with excellent level of standing, only present if this level is allowed, same for all other standing related tax rates

        :return: The excellent_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: float
        """
        return self._excellent_standing_tax_rate

    @excellent_standing_tax_rate.setter
    def excellent_standing_tax_rate(self, excellent_standing_tax_rate):
        """
        Sets the excellent_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        Tax rate for entities with excellent level of standing, only present if this level is allowed, same for all other standing related tax rates

        :param excellent_standing_tax_rate: The excellent_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: float
        """

        self._excellent_standing_tax_rate = excellent_standing_tax_rate

    @property
    def good_standing_tax_rate(self):
        """
        Gets the good_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        good_standing_tax_rate number

        :return: The good_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: float
        """
        return self._good_standing_tax_rate

    @good_standing_tax_rate.setter
    def good_standing_tax_rate(self, good_standing_tax_rate):
        """
        Sets the good_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        good_standing_tax_rate number

        :param good_standing_tax_rate: The good_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: float
        """

        self._good_standing_tax_rate = good_standing_tax_rate

    @property
    def neutral_standing_tax_rate(self):
        """
        Gets the neutral_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        neutral_standing_tax_rate number

        :return: The neutral_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: float
        """
        return self._neutral_standing_tax_rate

    @neutral_standing_tax_rate.setter
    def neutral_standing_tax_rate(self, neutral_standing_tax_rate):
        """
        Sets the neutral_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        neutral_standing_tax_rate number

        :param neutral_standing_tax_rate: The neutral_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: float
        """

        self._neutral_standing_tax_rate = neutral_standing_tax_rate

    @property
    def bad_standing_tax_rate(self):
        """
        Gets the bad_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        bad_standing_tax_rate number

        :return: The bad_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: float
        """
        return self._bad_standing_tax_rate

    @bad_standing_tax_rate.setter
    def bad_standing_tax_rate(self, bad_standing_tax_rate):
        """
        Sets the bad_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        bad_standing_tax_rate number

        :param bad_standing_tax_rate: The bad_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: float
        """

        self._bad_standing_tax_rate = bad_standing_tax_rate

    @property
    def terrible_standing_tax_rate(self):
        """
        Gets the terrible_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        terrible_standing_tax_rate number

        :return: The terrible_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :rtype: float
        """
        return self._terrible_standing_tax_rate

    @terrible_standing_tax_rate.setter
    def terrible_standing_tax_rate(self, terrible_standing_tax_rate):
        """
        Sets the terrible_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        terrible_standing_tax_rate number

        :param terrible_standing_tax_rate: The terrible_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.
        :type: float
        """

        self._terrible_standing_tax_rate = terrible_standing_tax_rate

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
        if not isinstance(other, GetCorporationsCorporationIdCustomsOffices200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
