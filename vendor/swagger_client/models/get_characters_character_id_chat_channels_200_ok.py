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


class GetCharactersCharacterIdChatChannels200Ok(object):
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
        'channel_id': 'int',
        'name': 'str',
        'owner_id': 'int',
        'comparison_key': 'str',
        'has_password': 'bool',
        'motd': 'str',
        'allowed': 'list[GetCharactersCharacterIdChatChannelsAllowed]',
        'operators': 'list[GetCharactersCharacterIdChatChannelsOperator]',
        'blocked': 'list[GetCharactersCharacterIdChatChannelsBlocked]',
        'muted': 'list[GetCharactersCharacterIdChatChannelsMuted]'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'name': 'name',
        'owner_id': 'owner_id',
        'comparison_key': 'comparison_key',
        'has_password': 'has_password',
        'motd': 'motd',
        'allowed': 'allowed',
        'operators': 'operators',
        'blocked': 'blocked',
        'muted': 'muted'
    }

    def __init__(self, channel_id=None, name=None, owner_id=None, comparison_key=None, has_password=None, motd=None, allowed=None, operators=None, blocked=None, muted=None):
        """
        GetCharactersCharacterIdChatChannels200Ok - a model defined in Swagger
        """

        self._channel_id = None
        self._name = None
        self._owner_id = None
        self._comparison_key = None
        self._has_password = None
        self._motd = None
        self._allowed = None
        self._operators = None
        self._blocked = None
        self._muted = None
        self.discriminator = None

        self.channel_id = channel_id
        self.name = name
        self.owner_id = owner_id
        self.comparison_key = comparison_key
        self.has_password = has_password
        self.motd = motd
        self.allowed = allowed
        self.operators = operators
        self.blocked = blocked
        self.muted = muted

    @property
    def channel_id(self):
        """
        Gets the channel_id of this GetCharactersCharacterIdChatChannels200Ok.
        Unique channel ID. Always negative for player-created channels. Permanent (CCP created) channels have a positive ID, but don't appear in the API

        :return: The channel_id of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """
        Sets the channel_id of this GetCharactersCharacterIdChatChannels200Ok.
        Unique channel ID. Always negative for player-created channels. Permanent (CCP created) channels have a positive ID, but don't appear in the API

        :param channel_id: The channel_id of this GetCharactersCharacterIdChatChannels200Ok.
        :type: int
        """
        if channel_id is None:
            raise ValueError("Invalid value for `channel_id`, must not be `None`")

        self._channel_id = channel_id

    @property
    def name(self):
        """
        Gets the name of this GetCharactersCharacterIdChatChannels200Ok.
        Displayed name of channel

        :return: The name of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetCharactersCharacterIdChatChannels200Ok.
        Displayed name of channel

        :param name: The name of this GetCharactersCharacterIdChatChannels200Ok.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def owner_id(self):
        """
        Gets the owner_id of this GetCharactersCharacterIdChatChannels200Ok.
        owner_id integer

        :return: The owner_id of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this GetCharactersCharacterIdChatChannels200Ok.
        owner_id integer

        :param owner_id: The owner_id of this GetCharactersCharacterIdChatChannels200Ok.
        :type: int
        """
        if owner_id is None:
            raise ValueError("Invalid value for `owner_id`, must not be `None`")

        self._owner_id = owner_id

    @property
    def comparison_key(self):
        """
        Gets the comparison_key of this GetCharactersCharacterIdChatChannels200Ok.
        Normalized, unique string used to compare channel names

        :return: The comparison_key of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: str
        """
        return self._comparison_key

    @comparison_key.setter
    def comparison_key(self, comparison_key):
        """
        Sets the comparison_key of this GetCharactersCharacterIdChatChannels200Ok.
        Normalized, unique string used to compare channel names

        :param comparison_key: The comparison_key of this GetCharactersCharacterIdChatChannels200Ok.
        :type: str
        """
        if comparison_key is None:
            raise ValueError("Invalid value for `comparison_key`, must not be `None`")

        self._comparison_key = comparison_key

    @property
    def has_password(self):
        """
        Gets the has_password of this GetCharactersCharacterIdChatChannels200Ok.
        If this is a password protected channel

        :return: The has_password of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """
        Sets the has_password of this GetCharactersCharacterIdChatChannels200Ok.
        If this is a password protected channel

        :param has_password: The has_password of this GetCharactersCharacterIdChatChannels200Ok.
        :type: bool
        """
        if has_password is None:
            raise ValueError("Invalid value for `has_password`, must not be `None`")

        self._has_password = has_password

    @property
    def motd(self):
        """
        Gets the motd of this GetCharactersCharacterIdChatChannels200Ok.
        Message of the day for this channel

        :return: The motd of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: str
        """
        return self._motd

    @motd.setter
    def motd(self, motd):
        """
        Sets the motd of this GetCharactersCharacterIdChatChannels200Ok.
        Message of the day for this channel

        :param motd: The motd of this GetCharactersCharacterIdChatChannels200Ok.
        :type: str
        """
        if motd is None:
            raise ValueError("Invalid value for `motd`, must not be `None`")

        self._motd = motd

    @property
    def allowed(self):
        """
        Gets the allowed of this GetCharactersCharacterIdChatChannels200Ok.
        allowed array

        :return: The allowed of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: list[GetCharactersCharacterIdChatChannelsAllowed]
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """
        Sets the allowed of this GetCharactersCharacterIdChatChannels200Ok.
        allowed array

        :param allowed: The allowed of this GetCharactersCharacterIdChatChannels200Ok.
        :type: list[GetCharactersCharacterIdChatChannelsAllowed]
        """
        if allowed is None:
            raise ValueError("Invalid value for `allowed`, must not be `None`")

        self._allowed = allowed

    @property
    def operators(self):
        """
        Gets the operators of this GetCharactersCharacterIdChatChannels200Ok.
        operators array

        :return: The operators of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: list[GetCharactersCharacterIdChatChannelsOperator]
        """
        return self._operators

    @operators.setter
    def operators(self, operators):
        """
        Sets the operators of this GetCharactersCharacterIdChatChannels200Ok.
        operators array

        :param operators: The operators of this GetCharactersCharacterIdChatChannels200Ok.
        :type: list[GetCharactersCharacterIdChatChannelsOperator]
        """
        if operators is None:
            raise ValueError("Invalid value for `operators`, must not be `None`")

        self._operators = operators

    @property
    def blocked(self):
        """
        Gets the blocked of this GetCharactersCharacterIdChatChannels200Ok.
        blocked array

        :return: The blocked of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: list[GetCharactersCharacterIdChatChannelsBlocked]
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """
        Sets the blocked of this GetCharactersCharacterIdChatChannels200Ok.
        blocked array

        :param blocked: The blocked of this GetCharactersCharacterIdChatChannels200Ok.
        :type: list[GetCharactersCharacterIdChatChannelsBlocked]
        """
        if blocked is None:
            raise ValueError("Invalid value for `blocked`, must not be `None`")

        self._blocked = blocked

    @property
    def muted(self):
        """
        Gets the muted of this GetCharactersCharacterIdChatChannels200Ok.
        muted array

        :return: The muted of this GetCharactersCharacterIdChatChannels200Ok.
        :rtype: list[GetCharactersCharacterIdChatChannelsMuted]
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """
        Sets the muted of this GetCharactersCharacterIdChatChannels200Ok.
        muted array

        :param muted: The muted of this GetCharactersCharacterIdChatChannels200Ok.
        :type: list[GetCharactersCharacterIdChatChannelsMuted]
        """
        if muted is None:
            raise ValueError("Invalid value for `muted`, must not be `None`")

        self._muted = muted

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
        if not isinstance(other, GetCharactersCharacterIdChatChannels200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
