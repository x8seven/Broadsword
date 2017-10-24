# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetCorporationsCorporationIdContacts200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, contact_id=None, contact_type=None, is_watched=None, label_id=None, standing=None):
        """
        GetCorporationsCorporationIdContacts200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'contact_id': 'int',
            'contact_type': 'str',
            'is_watched': 'bool',
            'label_id': 'int',
            'standing': 'float'
        }

        self.attribute_map = {
            'contact_id': 'contact_id',
            'contact_type': 'contact_type',
            'is_watched': 'is_watched',
            'label_id': 'label_id',
            'standing': 'standing'
        }

        self._contact_id = contact_id
        self._contact_type = contact_type
        self._is_watched = is_watched
        self._label_id = label_id
        self._standing = standing

    @property
    def contact_id(self):
        """
        Gets the contact_id of this GetCorporationsCorporationIdContacts200Ok.
        contact_id integer

        :return: The contact_id of this GetCorporationsCorporationIdContacts200Ok.
        :rtype: int
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """
        Sets the contact_id of this GetCorporationsCorporationIdContacts200Ok.
        contact_id integer

        :param contact_id: The contact_id of this GetCorporationsCorporationIdContacts200Ok.
        :type: int
        """
        if contact_id is None:
            raise ValueError("Invalid value for `contact_id`, must not be `None`")

        self._contact_id = contact_id

    @property
    def contact_type(self):
        """
        Gets the contact_type of this GetCorporationsCorporationIdContacts200Ok.
        contact_type string

        :return: The contact_type of this GetCorporationsCorporationIdContacts200Ok.
        :rtype: str
        """
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        """
        Sets the contact_type of this GetCorporationsCorporationIdContacts200Ok.
        contact_type string

        :param contact_type: The contact_type of this GetCorporationsCorporationIdContacts200Ok.
        :type: str
        """
        allowed_values = ["character", "corporation", "alliance", "faction"]
        if contact_type not in allowed_values:
            raise ValueError(
                "Invalid value for `contact_type` ({0}), must be one of {1}"
                .format(contact_type, allowed_values)
            )

        self._contact_type = contact_type

    @property
    def is_watched(self):
        """
        Gets the is_watched of this GetCorporationsCorporationIdContacts200Ok.
        Whether this contact is being watched

        :return: The is_watched of this GetCorporationsCorporationIdContacts200Ok.
        :rtype: bool
        """
        return self._is_watched

    @is_watched.setter
    def is_watched(self, is_watched):
        """
        Sets the is_watched of this GetCorporationsCorporationIdContacts200Ok.
        Whether this contact is being watched

        :param is_watched: The is_watched of this GetCorporationsCorporationIdContacts200Ok.
        :type: bool
        """

        self._is_watched = is_watched

    @property
    def label_id(self):
        """
        Gets the label_id of this GetCorporationsCorporationIdContacts200Ok.
        Custom label of the contact

        :return: The label_id of this GetCorporationsCorporationIdContacts200Ok.
        :rtype: int
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """
        Sets the label_id of this GetCorporationsCorporationIdContacts200Ok.
        Custom label of the contact

        :param label_id: The label_id of this GetCorporationsCorporationIdContacts200Ok.
        :type: int
        """

        self._label_id = label_id

    @property
    def standing(self):
        """
        Gets the standing of this GetCorporationsCorporationIdContacts200Ok.
        Standing of the contact

        :return: The standing of this GetCorporationsCorporationIdContacts200Ok.
        :rtype: float
        """
        return self._standing

    @standing.setter
    def standing(self, standing):
        """
        Sets the standing of this GetCorporationsCorporationIdContacts200Ok.
        Standing of the contact

        :param standing: The standing of this GetCorporationsCorporationIdContacts200Ok.
        :type: float
        """
        if standing is None:
            raise ValueError("Invalid value for `standing`, must not be `None`")

        self._standing = standing

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
        if not isinstance(other, GetCorporationsCorporationIdContacts200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other