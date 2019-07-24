# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.eth_flow_description import EthFlowDescription  # noqa: F401,E501
from swagger_server.models.flow_description import FlowDescription  # noqa: F401,E501
from swagger_server.models.flow_direction_rm import FlowDirectionRm  # noqa: F401,E501
from swagger_server import util


class FlowInformation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, flow_description: FlowDescription=None, eth_flow_description: EthFlowDescription=None, pack_filt_id: str=None, packet_filter_usage: bool=None, tos_traffic_class: str=None, spi: str=None, flow_label: str=None, flow_direction: FlowDirectionRm=None):  # noqa: E501
        """FlowInformation - a model defined in Swagger

        :param flow_description: The flow_description of this FlowInformation.  # noqa: E501
        :type flow_description: FlowDescription
        :param eth_flow_description: The eth_flow_description of this FlowInformation.  # noqa: E501
        :type eth_flow_description: EthFlowDescription
        :param pack_filt_id: The pack_filt_id of this FlowInformation.  # noqa: E501
        :type pack_filt_id: str
        :param packet_filter_usage: The packet_filter_usage of this FlowInformation.  # noqa: E501
        :type packet_filter_usage: bool
        :param tos_traffic_class: The tos_traffic_class of this FlowInformation.  # noqa: E501
        :type tos_traffic_class: str
        :param spi: The spi of this FlowInformation.  # noqa: E501
        :type spi: str
        :param flow_label: The flow_label of this FlowInformation.  # noqa: E501
        :type flow_label: str
        :param flow_direction: The flow_direction of this FlowInformation.  # noqa: E501
        :type flow_direction: FlowDirectionRm
        """
        self.swagger_types = {
            'flow_description': FlowDescription,
            'eth_flow_description': EthFlowDescription,
            'pack_filt_id': str,
            'packet_filter_usage': bool,
            'tos_traffic_class': str,
            'spi': str,
            'flow_label': str,
            'flow_direction': FlowDirectionRm
        }

        self.attribute_map = {
            'flow_description': 'flowDescription',
            'eth_flow_description': 'ethFlowDescription',
            'pack_filt_id': 'packFiltId',
            'packet_filter_usage': 'packetFilterUsage',
            'tos_traffic_class': 'tosTrafficClass',
            'spi': 'spi',
            'flow_label': 'flowLabel',
            'flow_direction': 'flowDirection'
        }
        self._flow_description = flow_description
        self._eth_flow_description = eth_flow_description
        self._pack_filt_id = pack_filt_id
        self._packet_filter_usage = packet_filter_usage
        self._tos_traffic_class = tos_traffic_class
        self._spi = spi
        self._flow_label = flow_label
        self._flow_direction = flow_direction

    @classmethod
    def from_dict(cls, dikt) -> 'FlowInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FlowInformation of this FlowInformation.  # noqa: E501
        :rtype: FlowInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def flow_description(self) -> FlowDescription:
        """Gets the flow_description of this FlowInformation.


        :return: The flow_description of this FlowInformation.
        :rtype: FlowDescription
        """
        return self._flow_description

    @flow_description.setter
    def flow_description(self, flow_description: FlowDescription):
        """Sets the flow_description of this FlowInformation.


        :param flow_description: The flow_description of this FlowInformation.
        :type flow_description: FlowDescription
        """

        self._flow_description = flow_description

    @property
    def eth_flow_description(self) -> EthFlowDescription:
        """Gets the eth_flow_description of this FlowInformation.


        :return: The eth_flow_description of this FlowInformation.
        :rtype: EthFlowDescription
        """
        return self._eth_flow_description

    @eth_flow_description.setter
    def eth_flow_description(self, eth_flow_description: EthFlowDescription):
        """Sets the eth_flow_description of this FlowInformation.


        :param eth_flow_description: The eth_flow_description of this FlowInformation.
        :type eth_flow_description: EthFlowDescription
        """

        self._eth_flow_description = eth_flow_description

    @property
    def pack_filt_id(self) -> str:
        """Gets the pack_filt_id of this FlowInformation.

        An identifier of packet filter.  # noqa: E501

        :return: The pack_filt_id of this FlowInformation.
        :rtype: str
        """
        return self._pack_filt_id

    @pack_filt_id.setter
    def pack_filt_id(self, pack_filt_id: str):
        """Sets the pack_filt_id of this FlowInformation.

        An identifier of packet filter.  # noqa: E501

        :param pack_filt_id: The pack_filt_id of this FlowInformation.
        :type pack_filt_id: str
        """

        self._pack_filt_id = pack_filt_id

    @property
    def packet_filter_usage(self) -> bool:
        """Gets the packet_filter_usage of this FlowInformation.

        The packet shall be sent to the UE.  # noqa: E501

        :return: The packet_filter_usage of this FlowInformation.
        :rtype: bool
        """
        return self._packet_filter_usage

    @packet_filter_usage.setter
    def packet_filter_usage(self, packet_filter_usage: bool):
        """Sets the packet_filter_usage of this FlowInformation.

        The packet shall be sent to the UE.  # noqa: E501

        :param packet_filter_usage: The packet_filter_usage of this FlowInformation.
        :type packet_filter_usage: bool
        """

        self._packet_filter_usage = packet_filter_usage

    @property
    def tos_traffic_class(self) -> str:
        """Gets the tos_traffic_class of this FlowInformation.

        Contains the Ipv4 Type-of-Service and mask field or the Ipv6 Traffic-Class field and mask field.  # noqa: E501

        :return: The tos_traffic_class of this FlowInformation.
        :rtype: str
        """
        return self._tos_traffic_class

    @tos_traffic_class.setter
    def tos_traffic_class(self, tos_traffic_class: str):
        """Sets the tos_traffic_class of this FlowInformation.

        Contains the Ipv4 Type-of-Service and mask field or the Ipv6 Traffic-Class field and mask field.  # noqa: E501

        :param tos_traffic_class: The tos_traffic_class of this FlowInformation.
        :type tos_traffic_class: str
        """

        self._tos_traffic_class = tos_traffic_class

    @property
    def spi(self) -> str:
        """Gets the spi of this FlowInformation.

        the security parameter index of the IPSec packet.  # noqa: E501

        :return: The spi of this FlowInformation.
        :rtype: str
        """
        return self._spi

    @spi.setter
    def spi(self, spi: str):
        """Sets the spi of this FlowInformation.

        the security parameter index of the IPSec packet.  # noqa: E501

        :param spi: The spi of this FlowInformation.
        :type spi: str
        """

        self._spi = spi

    @property
    def flow_label(self) -> str:
        """Gets the flow_label of this FlowInformation.

        the Ipv6 flow label header field.  # noqa: E501

        :return: The flow_label of this FlowInformation.
        :rtype: str
        """
        return self._flow_label

    @flow_label.setter
    def flow_label(self, flow_label: str):
        """Sets the flow_label of this FlowInformation.

        the Ipv6 flow label header field.  # noqa: E501

        :param flow_label: The flow_label of this FlowInformation.
        :type flow_label: str
        """

        self._flow_label = flow_label

    @property
    def flow_direction(self) -> FlowDirectionRm:
        """Gets the flow_direction of this FlowInformation.


        :return: The flow_direction of this FlowInformation.
        :rtype: FlowDirectionRm
        """
        return self._flow_direction

    @flow_direction.setter
    def flow_direction(self, flow_direction: FlowDirectionRm):
        """Sets the flow_direction of this FlowInformation.


        :param flow_direction: The flow_direction of this FlowInformation.
        :type flow_direction: FlowDirectionRm
        """

        self._flow_direction = flow_direction