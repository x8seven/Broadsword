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


class GetCharactersCharacterIdContactsLabels200Ok(object):
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
        'label_id': 'int',
        'label_name': 'str'
    }

    attribute_map = {
        'label_id': 'label_id',
        'label_name': 'label_name'
    }

    def __init__(self, label_id=None, label_name=None):
        """
        GetCharactersCharacterIdContactsLabels200Ok - a model defined in Swagger
        """

        self._label_id = None
        self._label_name = None
        self.discriminator = None

        self.label_id = label_id
        self.label_name = label_name

    @property
    def label_id(self):
        """
        Gets the label_id of this GetCharactersCharacterIdContactsLabels200Ok.
        label_id integer

        :return: The label_id of this GetCharactersCharacterIdContactsLabels200Ok.
        :rtype: int
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """
        Sets the label_id of this GetCharactersCharacterIdContactsLabels200Ok.
        label_id integer

        :param label_id: The label_id of this GetCharactersCharacterIdContactsLabels200Ok.
        :type: int
        """
        if label_id is None:
            raise ValueError("Invalid value for `label_id`, must not be `None`")

        self._label_id = label_id

    @property
    def label_name(self):
        """
        Gets the label_name of this GetCharactersCharacterIdContactsLabels200Ok.
        label_name string

        :return: The label_name of this GetCharactersCharacterIdContactsLabels200Ok.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """
        Sets the label_name of this GetCharactersCharacterIdContactsLabels200Ok.
        label_name string

        :param label_name: The label_name of this GetCharactersCharacterIdContactsLabels200Ok.
        :type: str
        """
        if label_name is None:
            raise ValueError("Invalid value for `label_name`, must not be `None`")

        self._label_name = label_name

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
        if not isinstance(other, GetCharactersCharacterIdContactsLabels200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
