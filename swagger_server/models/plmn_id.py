# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.mcc import Mcc  # noqa: F401,E501
from swagger_server.models.mnc import Mnc  # noqa: F401,E501
from swagger_server import util


class PlmnId(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, mcc: Mcc=None, mnc: Mnc=None):  # noqa: E501
        """PlmnId - a model defined in Swagger

        :param mcc: The mcc of this PlmnId.  # noqa: E501
        :type mcc: Mcc
        :param mnc: The mnc of this PlmnId.  # noqa: E501
        :type mnc: Mnc
        """
        self.swagger_types = {
            'mcc': Mcc,
            'mnc': Mnc
        }

        self.attribute_map = {
            'mcc': 'mcc',
            'mnc': 'mnc'
        }
        self._mcc = mcc
        self._mnc = mnc

    @classmethod
    def from_dict(cls, dikt) -> 'PlmnId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PlmnId of this PlmnId.  # noqa: E501
        :rtype: PlmnId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mcc(self) -> Mcc:
        """Gets the mcc of this PlmnId.


        :return: The mcc of this PlmnId.
        :rtype: Mcc
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc: Mcc):
        """Sets the mcc of this PlmnId.


        :param mcc: The mcc of this PlmnId.
        :type mcc: Mcc
        """
        if mcc is None:
            raise ValueError("Invalid value for `mcc`, must not be `None`")  # noqa: E501

        self._mcc = mcc

    @property
    def mnc(self) -> Mnc:
        """Gets the mnc of this PlmnId.


        :return: The mnc of this PlmnId.
        :rtype: Mnc
        """
        return self._mnc

    @mnc.setter
    def mnc(self, mnc: Mnc):
        """Sets the mnc of this PlmnId.


        :param mnc: The mnc of this PlmnId.
        :type mnc: Mnc
        """
        if mnc is None:
            raise ValueError("Invalid value for `mnc`, must not be `None`")  # noqa: E501

        self._mnc = mnc
