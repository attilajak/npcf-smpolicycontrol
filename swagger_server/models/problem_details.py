# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.invalid_param import InvalidParam  # noqa: F401,E501
from swagger_server.models.supported_features import SupportedFeatures  # noqa: F401,E501
from swagger_server.models.uri import Uri  # noqa: F401,E501
from swagger_server import util


class ProblemDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: Uri=None, title: str=None, status: int=None, detail: str=None, instance: Uri=None, cause: str=None, invalid_params: List[InvalidParam]=None, supported_features: SupportedFeatures=None):  # noqa: E501
        """ProblemDetails - a model defined in Swagger

        :param type: The type of this ProblemDetails.  # noqa: E501
        :type type: Uri
        :param title: The title of this ProblemDetails.  # noqa: E501
        :type title: str
        :param status: The status of this ProblemDetails.  # noqa: E501
        :type status: int
        :param detail: The detail of this ProblemDetails.  # noqa: E501
        :type detail: str
        :param instance: The instance of this ProblemDetails.  # noqa: E501
        :type instance: Uri
        :param cause: The cause of this ProblemDetails.  # noqa: E501
        :type cause: str
        :param invalid_params: The invalid_params of this ProblemDetails.  # noqa: E501
        :type invalid_params: List[InvalidParam]
        :param supported_features: The supported_features of this ProblemDetails.  # noqa: E501
        :type supported_features: SupportedFeatures
        """
        self.swagger_types = {
            'type': Uri,
            'title': str,
            'status': int,
            'detail': str,
            'instance': Uri,
            'cause': str,
            'invalid_params': List[InvalidParam],
            'supported_features': SupportedFeatures
        }

        self.attribute_map = {
            'type': 'type',
            'title': 'title',
            'status': 'status',
            'detail': 'detail',
            'instance': 'instance',
            'cause': 'cause',
            'invalid_params': 'invalidParams',
            'supported_features': 'supportedFeatures'
        }
        self._type = type
        self._title = title
        self._status = status
        self._detail = detail
        self._instance = instance
        self._cause = cause
        self._invalid_params = invalid_params
        self._supported_features = supported_features

    @classmethod
    def from_dict(cls, dikt) -> 'ProblemDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProblemDetails of this ProblemDetails.  # noqa: E501
        :rtype: ProblemDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> Uri:
        """Gets the type of this ProblemDetails.


        :return: The type of this ProblemDetails.
        :rtype: Uri
        """
        return self._type

    @type.setter
    def type(self, type: Uri):
        """Sets the type of this ProblemDetails.


        :param type: The type of this ProblemDetails.
        :type type: Uri
        """

        self._type = type

    @property
    def title(self) -> str:
        """Gets the title of this ProblemDetails.


        :return: The title of this ProblemDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this ProblemDetails.


        :param title: The title of this ProblemDetails.
        :type title: str
        """

        self._title = title

    @property
    def status(self) -> int:
        """Gets the status of this ProblemDetails.


        :return: The status of this ProblemDetails.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this ProblemDetails.


        :param status: The status of this ProblemDetails.
        :type status: int
        """

        self._status = status

    @property
    def detail(self) -> str:
        """Gets the detail of this ProblemDetails.


        :return: The detail of this ProblemDetails.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """Sets the detail of this ProblemDetails.


        :param detail: The detail of this ProblemDetails.
        :type detail: str
        """

        self._detail = detail

    @property
    def instance(self) -> Uri:
        """Gets the instance of this ProblemDetails.


        :return: The instance of this ProblemDetails.
        :rtype: Uri
        """
        return self._instance

    @instance.setter
    def instance(self, instance: Uri):
        """Sets the instance of this ProblemDetails.


        :param instance: The instance of this ProblemDetails.
        :type instance: Uri
        """

        self._instance = instance

    @property
    def cause(self) -> str:
        """Gets the cause of this ProblemDetails.


        :return: The cause of this ProblemDetails.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause: str):
        """Sets the cause of this ProblemDetails.


        :param cause: The cause of this ProblemDetails.
        :type cause: str
        """

        self._cause = cause

    @property
    def invalid_params(self) -> List[InvalidParam]:
        """Gets the invalid_params of this ProblemDetails.


        :return: The invalid_params of this ProblemDetails.
        :rtype: List[InvalidParam]
        """
        return self._invalid_params

    @invalid_params.setter
    def invalid_params(self, invalid_params: List[InvalidParam]):
        """Sets the invalid_params of this ProblemDetails.


        :param invalid_params: The invalid_params of this ProblemDetails.
        :type invalid_params: List[InvalidParam]
        """

        self._invalid_params = invalid_params

    @property
    def supported_features(self) -> SupportedFeatures:
        """Gets the supported_features of this ProblemDetails.


        :return: The supported_features of this ProblemDetails.
        :rtype: SupportedFeatures
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features: SupportedFeatures):
        """Sets the supported_features of this ProblemDetails.


        :param supported_features: The supported_features of this ProblemDetails.
        :type supported_features: SupportedFeatures
        """

        self._supported_features = supported_features
