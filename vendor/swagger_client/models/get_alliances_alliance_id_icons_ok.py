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


class GetAlliancesAllianceIdIconsOk(object):
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
        'px128x128': 'str',
        'px64x64': 'str'
    }

    attribute_map = {
        'px128x128': 'px128x128',
        'px64x64': 'px64x64'
    }

    def __init__(self, px128x128=None, px64x64=None):
        """
        GetAlliancesAllianceIdIconsOk - a model defined in Swagger
        """

        self._px128x128 = None
        self._px64x64 = None
        self.discriminator = None

        if px128x128 is not None:
          self.px128x128 = px128x128
        if px64x64 is not None:
          self.px64x64 = px64x64

    @property
    def px128x128(self):
        """
        Gets the px128x128 of this GetAlliancesAllianceIdIconsOk.
        px128x128 string

        :return: The px128x128 of this GetAlliancesAllianceIdIconsOk.
        :rtype: str
        """
        return self._px128x128

    @px128x128.setter
    def px128x128(self, px128x128):
        """
        Sets the px128x128 of this GetAlliancesAllianceIdIconsOk.
        px128x128 string

        :param px128x128: The px128x128 of this GetAlliancesAllianceIdIconsOk.
        :type: str
        """

        self._px128x128 = px128x128

    @property
    def px64x64(self):
        """
        Gets the px64x64 of this GetAlliancesAllianceIdIconsOk.
        px64x64 string

        :return: The px64x64 of this GetAlliancesAllianceIdIconsOk.
        :rtype: str
        """
        return self._px64x64

    @px64x64.setter
    def px64x64(self, px64x64):
        """
        Sets the px64x64 of this GetAlliancesAllianceIdIconsOk.
        px64x64 string

        :param px64x64: The px64x64 of this GetAlliancesAllianceIdIconsOk.
        :type: str
        """

        self._px64x64 = px64x64

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
        if not isinstance(other, GetAlliancesAllianceIdIconsOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
