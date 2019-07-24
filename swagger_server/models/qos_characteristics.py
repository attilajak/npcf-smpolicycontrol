# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.aver_window import AverWindow  # noqa: F401,E501
from swagger_server.models.max_data_burst_vol import MaxDataBurstVol  # noqa: F401,E501
from swagger_server.models.model5_qi import Model5Qi  # noqa: F401,E501
from swagger_server.models.model5_qi_priority_level import Model5QiPriorityLevel  # noqa: F401,E501
from swagger_server.models.packet_del_budget import PacketDelBudget  # noqa: F401,E501
from swagger_server.models.packet_err_rate import PacketErrRate  # noqa: F401,E501
from swagger_server.models.qos_resource_type import QosResourceType  # noqa: F401,E501
from swagger_server import util


class QosCharacteristics(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, _5qi: Model5Qi=None, resource_type: QosResourceType=None, priority_level: Model5QiPriorityLevel=None, packet_delay_budget: PacketDelBudget=None, packet_error_rate: PacketErrRate=None, averaging_window: AverWindow=None, max_data_burst_vol: MaxDataBurstVol=None):  # noqa: E501
        """QosCharacteristics - a model defined in Swagger

        :param _5qi: The _5qi of this QosCharacteristics.  # noqa: E501
        :type _5qi: Model5Qi
        :param resource_type: The resource_type of this QosCharacteristics.  # noqa: E501
        :type resource_type: QosResourceType
        :param priority_level: The priority_level of this QosCharacteristics.  # noqa: E501
        :type priority_level: Model5QiPriorityLevel
        :param packet_delay_budget: The packet_delay_budget of this QosCharacteristics.  # noqa: E501
        :type packet_delay_budget: PacketDelBudget
        :param packet_error_rate: The packet_error_rate of this QosCharacteristics.  # noqa: E501
        :type packet_error_rate: PacketErrRate
        :param averaging_window: The averaging_window of this QosCharacteristics.  # noqa: E501
        :type averaging_window: AverWindow
        :param max_data_burst_vol: The max_data_burst_vol of this QosCharacteristics.  # noqa: E501
        :type max_data_burst_vol: MaxDataBurstVol
        """
        self.swagger_types = {
            '_5qi': Model5Qi,
            'resource_type': QosResourceType,
            'priority_level': Model5QiPriorityLevel,
            'packet_delay_budget': PacketDelBudget,
            'packet_error_rate': PacketErrRate,
            'averaging_window': AverWindow,
            'max_data_burst_vol': MaxDataBurstVol
        }

        self.attribute_map = {
            '_5qi': '5qi',
            'resource_type': 'resourceType',
            'priority_level': 'priorityLevel',
            'packet_delay_budget': 'packetDelayBudget',
            'packet_error_rate': 'packetErrorRate',
            'averaging_window': 'averagingWindow',
            'max_data_burst_vol': 'maxDataBurstVol'
        }
        self.__5qi = _5qi
        self._resource_type = resource_type
        self._priority_level = priority_level
        self._packet_delay_budget = packet_delay_budget
        self._packet_error_rate = packet_error_rate
        self._averaging_window = averaging_window
        self._max_data_burst_vol = max_data_burst_vol

    @classmethod
    def from_dict(cls, dikt) -> 'QosCharacteristics':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QosCharacteristics of this QosCharacteristics.  # noqa: E501
        :rtype: QosCharacteristics
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _5qi(self) -> Model5Qi:
        """Gets the _5qi of this QosCharacteristics.


        :return: The _5qi of this QosCharacteristics.
        :rtype: Model5Qi
        """
        return self.__5qi

    @_5qi.setter
    def _5qi(self, _5qi: Model5Qi):
        """Sets the _5qi of this QosCharacteristics.


        :param _5qi: The _5qi of this QosCharacteristics.
        :type _5qi: Model5Qi
        """
        if _5qi is None:
            raise ValueError("Invalid value for `_5qi`, must not be `None`")  # noqa: E501

        self.__5qi = _5qi

    @property
    def resource_type(self) -> QosResourceType:
        """Gets the resource_type of this QosCharacteristics.


        :return: The resource_type of this QosCharacteristics.
        :rtype: QosResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type: QosResourceType):
        """Sets the resource_type of this QosCharacteristics.


        :param resource_type: The resource_type of this QosCharacteristics.
        :type resource_type: QosResourceType
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def priority_level(self) -> Model5QiPriorityLevel:
        """Gets the priority_level of this QosCharacteristics.


        :return: The priority_level of this QosCharacteristics.
        :rtype: Model5QiPriorityLevel
        """
        return self._priority_level

    @priority_level.setter
    def priority_level(self, priority_level: Model5QiPriorityLevel):
        """Sets the priority_level of this QosCharacteristics.


        :param priority_level: The priority_level of this QosCharacteristics.
        :type priority_level: Model5QiPriorityLevel
        """
        if priority_level is None:
            raise ValueError("Invalid value for `priority_level`, must not be `None`")  # noqa: E501

        self._priority_level = priority_level

    @property
    def packet_delay_budget(self) -> PacketDelBudget:
        """Gets the packet_delay_budget of this QosCharacteristics.


        :return: The packet_delay_budget of this QosCharacteristics.
        :rtype: PacketDelBudget
        """
        return self._packet_delay_budget

    @packet_delay_budget.setter
    def packet_delay_budget(self, packet_delay_budget: PacketDelBudget):
        """Sets the packet_delay_budget of this QosCharacteristics.


        :param packet_delay_budget: The packet_delay_budget of this QosCharacteristics.
        :type packet_delay_budget: PacketDelBudget
        """
        if packet_delay_budget is None:
            raise ValueError("Invalid value for `packet_delay_budget`, must not be `None`")  # noqa: E501

        self._packet_delay_budget = packet_delay_budget

    @property
    def packet_error_rate(self) -> PacketErrRate:
        """Gets the packet_error_rate of this QosCharacteristics.


        :return: The packet_error_rate of this QosCharacteristics.
        :rtype: PacketErrRate
        """
        return self._packet_error_rate

    @packet_error_rate.setter
    def packet_error_rate(self, packet_error_rate: PacketErrRate):
        """Sets the packet_error_rate of this QosCharacteristics.


        :param packet_error_rate: The packet_error_rate of this QosCharacteristics.
        :type packet_error_rate: PacketErrRate
        """
        if packet_error_rate is None:
            raise ValueError("Invalid value for `packet_error_rate`, must not be `None`")  # noqa: E501

        self._packet_error_rate = packet_error_rate

    @property
    def averaging_window(self) -> AverWindow:
        """Gets the averaging_window of this QosCharacteristics.


        :return: The averaging_window of this QosCharacteristics.
        :rtype: AverWindow
        """
        return self._averaging_window

    @averaging_window.setter
    def averaging_window(self, averaging_window: AverWindow):
        """Sets the averaging_window of this QosCharacteristics.


        :param averaging_window: The averaging_window of this QosCharacteristics.
        :type averaging_window: AverWindow
        """

        self._averaging_window = averaging_window

    @property
    def max_data_burst_vol(self) -> MaxDataBurstVol:
        """Gets the max_data_burst_vol of this QosCharacteristics.


        :return: The max_data_burst_vol of this QosCharacteristics.
        :rtype: MaxDataBurstVol
        """
        return self._max_data_burst_vol

    @max_data_burst_vol.setter
    def max_data_burst_vol(self, max_data_burst_vol: MaxDataBurstVol):
        """Sets the max_data_burst_vol of this QosCharacteristics.


        :param max_data_burst_vol: The max_data_burst_vol of this QosCharacteristics.
        :type max_data_burst_vol: MaxDataBurstVol
        """

        self._max_data_burst_vol = max_data_burst_vol
