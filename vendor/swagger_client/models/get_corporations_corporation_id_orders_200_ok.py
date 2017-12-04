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


class GetCorporationsCorporationIdOrders200Ok(object):
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
        'order_id': 'int',
        'type_id': 'int',
        'region_id': 'int',
        'location_id': 'int',
        'range': 'str',
        'is_buy_order': 'bool',
        'price': 'float',
        'volume_total': 'int',
        'volume_remain': 'int',
        'issued': 'datetime',
        'state': 'str',
        'min_volume': 'int',
        'wallet_division': 'int',
        'duration': 'int',
        'escrow': 'float'
    }

    attribute_map = {
        'order_id': 'order_id',
        'type_id': 'type_id',
        'region_id': 'region_id',
        'location_id': 'location_id',
        'range': 'range',
        'is_buy_order': 'is_buy_order',
        'price': 'price',
        'volume_total': 'volume_total',
        'volume_remain': 'volume_remain',
        'issued': 'issued',
        'state': 'state',
        'min_volume': 'min_volume',
        'wallet_division': 'wallet_division',
        'duration': 'duration',
        'escrow': 'escrow'
    }

    def __init__(self, order_id=None, type_id=None, region_id=None, location_id=None, range=None, is_buy_order=None, price=None, volume_total=None, volume_remain=None, issued=None, state=None, min_volume=None, wallet_division=None, duration=None, escrow=None):
        """
        GetCorporationsCorporationIdOrders200Ok - a model defined in Swagger
        """

        self._order_id = None
        self._type_id = None
        self._region_id = None
        self._location_id = None
        self._range = None
        self._is_buy_order = None
        self._price = None
        self._volume_total = None
        self._volume_remain = None
        self._issued = None
        self._state = None
        self._min_volume = None
        self._wallet_division = None
        self._duration = None
        self._escrow = None
        self.discriminator = None

        self.order_id = order_id
        self.type_id = type_id
        self.region_id = region_id
        self.location_id = location_id
        self.range = range
        self.is_buy_order = is_buy_order
        self.price = price
        self.volume_total = volume_total
        self.volume_remain = volume_remain
        self.issued = issued
        self.state = state
        self.min_volume = min_volume
        self.wallet_division = wallet_division
        self.duration = duration
        self.escrow = escrow

    @property
    def order_id(self):
        """
        Gets the order_id of this GetCorporationsCorporationIdOrders200Ok.
        Unique order ID

        :return: The order_id of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        Sets the order_id of this GetCorporationsCorporationIdOrders200Ok.
        Unique order ID

        :param order_id: The order_id of this GetCorporationsCorporationIdOrders200Ok.
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")

        self._order_id = order_id

    @property
    def type_id(self):
        """
        Gets the type_id of this GetCorporationsCorporationIdOrders200Ok.
        The type ID of the item transacted in this order

        :return: The type_id of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetCorporationsCorporationIdOrders200Ok.
        The type ID of the item transacted in this order

        :param type_id: The type_id of this GetCorporationsCorporationIdOrders200Ok.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

    @property
    def region_id(self):
        """
        Gets the region_id of this GetCorporationsCorporationIdOrders200Ok.
        ID of the region where order was placed

        :return: The region_id of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this GetCorporationsCorporationIdOrders200Ok.
        ID of the region where order was placed

        :param region_id: The region_id of this GetCorporationsCorporationIdOrders200Ok.
        :type: int
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")

        self._region_id = region_id

    @property
    def location_id(self):
        """
        Gets the location_id of this GetCorporationsCorporationIdOrders200Ok.
        ID of the location where order was placed

        :return: The location_id of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this GetCorporationsCorporationIdOrders200Ok.
        ID of the location where order was placed

        :param location_id: The location_id of this GetCorporationsCorporationIdOrders200Ok.
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")

        self._location_id = location_id

    @property
    def range(self):
        """
        Gets the range of this GetCorporationsCorporationIdOrders200Ok.
        Valid order range, numbers are ranges in jumps

        :return: The range of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """
        Sets the range of this GetCorporationsCorporationIdOrders200Ok.
        Valid order range, numbers are ranges in jumps

        :param range: The range of this GetCorporationsCorporationIdOrders200Ok.
        :type: str
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")
        allowed_values = ["1", "10", "2", "20", "3", "30", "4", "40", "5", "region", "solarsystem", "station"]
        if range not in allowed_values:
            raise ValueError(
                "Invalid value for `range` ({0}), must be one of {1}"
                .format(range, allowed_values)
            )

        self._range = range

    @property
    def is_buy_order(self):
        """
        Gets the is_buy_order of this GetCorporationsCorporationIdOrders200Ok.
        True for a bid (buy) order. False for an offer (sell) order

        :return: The is_buy_order of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: bool
        """
        return self._is_buy_order

    @is_buy_order.setter
    def is_buy_order(self, is_buy_order):
        """
        Sets the is_buy_order of this GetCorporationsCorporationIdOrders200Ok.
        True for a bid (buy) order. False for an offer (sell) order

        :param is_buy_order: The is_buy_order of this GetCorporationsCorporationIdOrders200Ok.
        :type: bool
        """
        if is_buy_order is None:
            raise ValueError("Invalid value for `is_buy_order`, must not be `None`")

        self._is_buy_order = is_buy_order

    @property
    def price(self):
        """
        Gets the price of this GetCorporationsCorporationIdOrders200Ok.
        Cost per unit for this order

        :return: The price of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this GetCorporationsCorporationIdOrders200Ok.
        Cost per unit for this order

        :param price: The price of this GetCorporationsCorporationIdOrders200Ok.
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")

        self._price = price

    @property
    def volume_total(self):
        """
        Gets the volume_total of this GetCorporationsCorporationIdOrders200Ok.
        Quantity of items required or offered at time order was placed

        :return: The volume_total of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: int
        """
        return self._volume_total

    @volume_total.setter
    def volume_total(self, volume_total):
        """
        Sets the volume_total of this GetCorporationsCorporationIdOrders200Ok.
        Quantity of items required or offered at time order was placed

        :param volume_total: The volume_total of this GetCorporationsCorporationIdOrders200Ok.
        :type: int
        """
        if volume_total is None:
            raise ValueError("Invalid value for `volume_total`, must not be `None`")

        self._volume_total = volume_total

    @property
    def volume_remain(self):
        """
        Gets the volume_remain of this GetCorporationsCorporationIdOrders200Ok.
        Quantity of items still required or offered

        :return: The volume_remain of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: int
        """
        return self._volume_remain

    @volume_remain.setter
    def volume_remain(self, volume_remain):
        """
        Sets the volume_remain of this GetCorporationsCorporationIdOrders200Ok.
        Quantity of items still required or offered

        :param volume_remain: The volume_remain of this GetCorporationsCorporationIdOrders200Ok.
        :type: int
        """
        if volume_remain is None:
            raise ValueError("Invalid value for `volume_remain`, must not be `None`")

        self._volume_remain = volume_remain

    @property
    def issued(self):
        """
        Gets the issued of this GetCorporationsCorporationIdOrders200Ok.
        Date and time when this order was issued

        :return: The issued of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: datetime
        """
        return self._issued

    @issued.setter
    def issued(self, issued):
        """
        Sets the issued of this GetCorporationsCorporationIdOrders200Ok.
        Date and time when this order was issued

        :param issued: The issued of this GetCorporationsCorporationIdOrders200Ok.
        :type: datetime
        """
        if issued is None:
            raise ValueError("Invalid value for `issued`, must not be `None`")

        self._issued = issued

    @property
    def state(self):
        """
        Gets the state of this GetCorporationsCorporationIdOrders200Ok.
        Current order state

        :return: The state of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this GetCorporationsCorporationIdOrders200Ok.
        Current order state

        :param state: The state of this GetCorporationsCorporationIdOrders200Ok.
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")
        allowed_values = ["cancelled", "character_deleted", "closed", "expired", "open", "pending"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def min_volume(self):
        """
        Gets the min_volume of this GetCorporationsCorporationIdOrders200Ok.
        For bids (buy orders), the minimum quantity that will be accepted in a matching offer (sell order)

        :return: The min_volume of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: int
        """
        return self._min_volume

    @min_volume.setter
    def min_volume(self, min_volume):
        """
        Sets the min_volume of this GetCorporationsCorporationIdOrders200Ok.
        For bids (buy orders), the minimum quantity that will be accepted in a matching offer (sell order)

        :param min_volume: The min_volume of this GetCorporationsCorporationIdOrders200Ok.
        :type: int
        """
        if min_volume is None:
            raise ValueError("Invalid value for `min_volume`, must not be `None`")

        self._min_volume = min_volume

    @property
    def wallet_division(self):
        """
        Gets the wallet_division of this GetCorporationsCorporationIdOrders200Ok.
        Wallet division of which this order used

        :return: The wallet_division of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: int
        """
        return self._wallet_division

    @wallet_division.setter
    def wallet_division(self, wallet_division):
        """
        Sets the wallet_division of this GetCorporationsCorporationIdOrders200Ok.
        Wallet division of which this order used

        :param wallet_division: The wallet_division of this GetCorporationsCorporationIdOrders200Ok.
        :type: int
        """
        if wallet_division is None:
            raise ValueError("Invalid value for `wallet_division`, must not be `None`")
        if wallet_division is not None and wallet_division > 7:
            raise ValueError("Invalid value for `wallet_division`, must be a value less than or equal to `7`")
        if wallet_division is not None and wallet_division < 1:
            raise ValueError("Invalid value for `wallet_division`, must be a value greater than or equal to `1`")

        self._wallet_division = wallet_division

    @property
    def duration(self):
        """
        Gets the duration of this GetCorporationsCorporationIdOrders200Ok.
        Numer of days for which order is valid (starting from the issued date). An order expires at time issued + duration

        :return: The duration of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this GetCorporationsCorporationIdOrders200Ok.
        Numer of days for which order is valid (starting from the issued date). An order expires at time issued + duration

        :param duration: The duration of this GetCorporationsCorporationIdOrders200Ok.
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")

        self._duration = duration

    @property
    def escrow(self):
        """
        Gets the escrow of this GetCorporationsCorporationIdOrders200Ok.
        For buy orders, the amount of ISK in escrow

        :return: The escrow of this GetCorporationsCorporationIdOrders200Ok.
        :rtype: float
        """
        return self._escrow

    @escrow.setter
    def escrow(self, escrow):
        """
        Sets the escrow of this GetCorporationsCorporationIdOrders200Ok.
        For buy orders, the amount of ISK in escrow

        :param escrow: The escrow of this GetCorporationsCorporationIdOrders200Ok.
        :type: float
        """
        if escrow is None:
            raise ValueError("Invalid value for `escrow`, must not be `None`")

        self._escrow = escrow

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
        if not isinstance(other, GetCorporationsCorporationIdOrders200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
