# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FlowDirection2(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """FlowDirection2 - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'FlowDirection2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FlowDirection_2 of this FlowDirection2.  # noqa: E501
        :rtype: FlowDirection2
        """
        return util.deserialize_model(dikt, cls)
