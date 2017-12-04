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


class PutCharactersCharacterIdMailMailIdContents(object):
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
        'read': 'bool',
        'labels': 'list[int]'
    }

    attribute_map = {
        'read': 'read',
        'labels': 'labels'
    }

    def __init__(self, read=None, labels=None):
        """
        PutCharactersCharacterIdMailMailIdContents - a model defined in Swagger
        """

        self._read = None
        self._labels = None
        self.discriminator = None

        if read is not None:
          self.read = read
        if labels is not None:
          self.labels = labels

    @property
    def read(self):
        """
        Gets the read of this PutCharactersCharacterIdMailMailIdContents.
        Whether the mail is flagged as read

        :return: The read of this PutCharactersCharacterIdMailMailIdContents.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this PutCharactersCharacterIdMailMailIdContents.
        Whether the mail is flagged as read

        :param read: The read of this PutCharactersCharacterIdMailMailIdContents.
        :type: bool
        """

        self._read = read

    @property
    def labels(self):
        """
        Gets the labels of this PutCharactersCharacterIdMailMailIdContents.
        Labels to assign to the mail. Pre-existing labels are unassigned.

        :return: The labels of this PutCharactersCharacterIdMailMailIdContents.
        :rtype: list[int]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this PutCharactersCharacterIdMailMailIdContents.
        Labels to assign to the mail. Pre-existing labels are unassigned.

        :param labels: The labels of this PutCharactersCharacterIdMailMailIdContents.
        :type: list[int]
        """

        self._labels = labels

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
        if not isinstance(other, PutCharactersCharacterIdMailMailIdContents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
