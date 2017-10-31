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


class PostFleetsFleetIdWingsCreated(object):
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
        'wing_id': 'int'
    }

    attribute_map = {
        'wing_id': 'wing_id'
    }

    def __init__(self, wing_id=None):
        """
        PostFleetsFleetIdWingsCreated - a model defined in Swagger
        """

        self._wing_id = None
        self.discriminator = None

        self.wing_id = wing_id

    @property
    def wing_id(self):
        """
        Gets the wing_id of this PostFleetsFleetIdWingsCreated.
        The wing_id of the newly created wing

        :return: The wing_id of this PostFleetsFleetIdWingsCreated.
        :rtype: int
        """
        return self._wing_id

    @wing_id.setter
    def wing_id(self, wing_id):
        """
        Sets the wing_id of this PostFleetsFleetIdWingsCreated.
        The wing_id of the newly created wing

        :param wing_id: The wing_id of this PostFleetsFleetIdWingsCreated.
        :type: int
        """
        if wing_id is None:
            raise ValueError("Invalid value for `wing_id`, must not be `None`")

        self._wing_id = wing_id

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
        if not isinstance(other, PostFleetsFleetIdWingsCreated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
