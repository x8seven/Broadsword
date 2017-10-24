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


class GetUniverseGraphicsGraphicIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, collision_file=None, graphic_file=None, graphic_id=None, icon_folder=None, sof_dna=None, sof_fation_name=None, sof_hull_name=None, sof_race_name=None):
        """
        GetUniverseGraphicsGraphicIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'collision_file': 'str',
            'graphic_file': 'str',
            'graphic_id': 'int',
            'icon_folder': 'str',
            'sof_dna': 'str',
            'sof_fation_name': 'str',
            'sof_hull_name': 'str',
            'sof_race_name': 'str'
        }

        self.attribute_map = {
            'collision_file': 'collision_file',
            'graphic_file': 'graphic_file',
            'graphic_id': 'graphic_id',
            'icon_folder': 'icon_folder',
            'sof_dna': 'sof_dna',
            'sof_fation_name': 'sof_fation_name',
            'sof_hull_name': 'sof_hull_name',
            'sof_race_name': 'sof_race_name'
        }

        self._collision_file = collision_file
        self._graphic_file = graphic_file
        self._graphic_id = graphic_id
        self._icon_folder = icon_folder
        self._sof_dna = sof_dna
        self._sof_fation_name = sof_fation_name
        self._sof_hull_name = sof_hull_name
        self._sof_race_name = sof_race_name

    @property
    def collision_file(self):
        """
        Gets the collision_file of this GetUniverseGraphicsGraphicIdOk.
        collision_file string

        :return: The collision_file of this GetUniverseGraphicsGraphicIdOk.
        :rtype: str
        """
        return self._collision_file

    @collision_file.setter
    def collision_file(self, collision_file):
        """
        Sets the collision_file of this GetUniverseGraphicsGraphicIdOk.
        collision_file string

        :param collision_file: The collision_file of this GetUniverseGraphicsGraphicIdOk.
        :type: str
        """

        self._collision_file = collision_file

    @property
    def graphic_file(self):
        """
        Gets the graphic_file of this GetUniverseGraphicsGraphicIdOk.
        graphic_file string

        :return: The graphic_file of this GetUniverseGraphicsGraphicIdOk.
        :rtype: str
        """
        return self._graphic_file

    @graphic_file.setter
    def graphic_file(self, graphic_file):
        """
        Sets the graphic_file of this GetUniverseGraphicsGraphicIdOk.
        graphic_file string

        :param graphic_file: The graphic_file of this GetUniverseGraphicsGraphicIdOk.
        :type: str
        """

        self._graphic_file = graphic_file

    @property
    def graphic_id(self):
        """
        Gets the graphic_id of this GetUniverseGraphicsGraphicIdOk.
        graphic_id integer

        :return: The graphic_id of this GetUniverseGraphicsGraphicIdOk.
        :rtype: int
        """
        return self._graphic_id

    @graphic_id.setter
    def graphic_id(self, graphic_id):
        """
        Sets the graphic_id of this GetUniverseGraphicsGraphicIdOk.
        graphic_id integer

        :param graphic_id: The graphic_id of this GetUniverseGraphicsGraphicIdOk.
        :type: int
        """
        if graphic_id is None:
            raise ValueError("Invalid value for `graphic_id`, must not be `None`")

        self._graphic_id = graphic_id

    @property
    def icon_folder(self):
        """
        Gets the icon_folder of this GetUniverseGraphicsGraphicIdOk.
        icon_folder string

        :return: The icon_folder of this GetUniverseGraphicsGraphicIdOk.
        :rtype: str
        """
        return self._icon_folder

    @icon_folder.setter
    def icon_folder(self, icon_folder):
        """
        Sets the icon_folder of this GetUniverseGraphicsGraphicIdOk.
        icon_folder string

        :param icon_folder: The icon_folder of this GetUniverseGraphicsGraphicIdOk.
        :type: str
        """

        self._icon_folder = icon_folder

    @property
    def sof_dna(self):
        """
        Gets the sof_dna of this GetUniverseGraphicsGraphicIdOk.
        sof_dna string

        :return: The sof_dna of this GetUniverseGraphicsGraphicIdOk.
        :rtype: str
        """
        return self._sof_dna

    @sof_dna.setter
    def sof_dna(self, sof_dna):
        """
        Sets the sof_dna of this GetUniverseGraphicsGraphicIdOk.
        sof_dna string

        :param sof_dna: The sof_dna of this GetUniverseGraphicsGraphicIdOk.
        :type: str
        """

        self._sof_dna = sof_dna

    @property
    def sof_fation_name(self):
        """
        Gets the sof_fation_name of this GetUniverseGraphicsGraphicIdOk.
        sof_fation_name string

        :return: The sof_fation_name of this GetUniverseGraphicsGraphicIdOk.
        :rtype: str
        """
        return self._sof_fation_name

    @sof_fation_name.setter
    def sof_fation_name(self, sof_fation_name):
        """
        Sets the sof_fation_name of this GetUniverseGraphicsGraphicIdOk.
        sof_fation_name string

        :param sof_fation_name: The sof_fation_name of this GetUniverseGraphicsGraphicIdOk.
        :type: str
        """

        self._sof_fation_name = sof_fation_name

    @property
    def sof_hull_name(self):
        """
        Gets the sof_hull_name of this GetUniverseGraphicsGraphicIdOk.
        sof_hull_name string

        :return: The sof_hull_name of this GetUniverseGraphicsGraphicIdOk.
        :rtype: str
        """
        return self._sof_hull_name

    @sof_hull_name.setter
    def sof_hull_name(self, sof_hull_name):
        """
        Sets the sof_hull_name of this GetUniverseGraphicsGraphicIdOk.
        sof_hull_name string

        :param sof_hull_name: The sof_hull_name of this GetUniverseGraphicsGraphicIdOk.
        :type: str
        """

        self._sof_hull_name = sof_hull_name

    @property
    def sof_race_name(self):
        """
        Gets the sof_race_name of this GetUniverseGraphicsGraphicIdOk.
        sof_race_name string

        :return: The sof_race_name of this GetUniverseGraphicsGraphicIdOk.
        :rtype: str
        """
        return self._sof_race_name

    @sof_race_name.setter
    def sof_race_name(self, sof_race_name):
        """
        Sets the sof_race_name of this GetUniverseGraphicsGraphicIdOk.
        sof_race_name string

        :param sof_race_name: The sof_race_name of this GetUniverseGraphicsGraphicIdOk.
        :type: str
        """

        self._sof_race_name = sof_race_name

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
        if not isinstance(other, GetUniverseGraphicsGraphicIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other