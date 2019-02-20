# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_notification_getnotificationsubscriptionservicedetails_output import TapiNotificationGetnotificationsubscriptionservicedetailsOutput  # noqa: F401,E501
from tapi_server import util


class TapiNotificationGetNotificationSubscriptionServiceDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output=None):  # noqa: E501
        """TapiNotificationGetNotificationSubscriptionServiceDetails - a model defined in OpenAPI

        :param output: The output of this TapiNotificationGetNotificationSubscriptionServiceDetails.  # noqa: E501
        :type output: TapiNotificationGetnotificationsubscriptionservicedetailsOutput
        """
        self.openapi_types = {
            'output': TapiNotificationGetnotificationsubscriptionservicedetailsOutput
        }

        self.attribute_map = {
            'output': 'output'
        }

        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'TapiNotificationGetNotificationSubscriptionServiceDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.notification.GetNotificationSubscriptionServiceDetails of this TapiNotificationGetNotificationSubscriptionServiceDetails.  # noqa: E501
        :rtype: TapiNotificationGetNotificationSubscriptionServiceDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self):
        """Gets the output of this TapiNotificationGetNotificationSubscriptionServiceDetails.


        :return: The output of this TapiNotificationGetNotificationSubscriptionServiceDetails.
        :rtype: TapiNotificationGetnotificationsubscriptionservicedetailsOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TapiNotificationGetNotificationSubscriptionServiceDetails.


        :param output: The output of this TapiNotificationGetNotificationSubscriptionServiceDetails.
        :type output: TapiNotificationGetnotificationsubscriptionservicedetailsOutput
        """

        self._output = output