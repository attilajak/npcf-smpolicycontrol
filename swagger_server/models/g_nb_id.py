# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class GNbId(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, bit_length: int=None, g_nb_value: str=None):  # noqa: E501
        """GNbId - a model defined in Swagger

        :param bit_length: The bit_length of this GNbId.  # noqa: E501
        :type bit_length: int
        :param g_nb_value: The g_nb_value of this GNbId.  # noqa: E501
        :type g_nb_value: str
        """
        self.swagger_types = {
            'bit_length': int,
            'g_nb_value': str
        }

        self.attribute_map = {
            'bit_length': 'bitLength',
            'g_nb_value': 'gNBValue'
        }
        self._bit_length = bit_length
        self._g_nb_value = g_nb_value

    @classmethod
    def from_dict(cls, dikt) -> 'GNbId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GNbId of this GNbId.  # noqa: E501
        :rtype: GNbId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bit_length(self) -> int:
        """Gets the bit_length of this GNbId.


        :return: The bit_length of this GNbId.
        :rtype: int
        """
        return self._bit_length

    @bit_length.setter
    def bit_length(self, bit_length: int):
        """Sets the bit_length of this GNbId.


        :param bit_length: The bit_length of this GNbId.
        :type bit_length: int
        """
        if bit_length is None:
            raise ValueError("Invalid value for `bit_length`, must not be `None`")  # noqa: E501

        self._bit_length = bit_length

    @property
    def g_nb_value(self) -> str:
        """Gets the g_nb_value of this GNbId.


        :return: The g_nb_value of this GNbId.
        :rtype: str
        """
        return self._g_nb_value

    @g_nb_value.setter
    def g_nb_value(self, g_nb_value: str):
        """Sets the g_nb_value of this GNbId.


        :param g_nb_value: The g_nb_value of this GNbId.
        :type g_nb_value: str
        """
        if g_nb_value is None:
            raise ValueError("Invalid value for `g_nb_value`, must not be `None`")  # noqa: E501

        self._g_nb_value = g_nb_value
