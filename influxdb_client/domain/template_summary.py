# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TemplateSummary(object):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'sources': 'list[str]',
        'stack_id': 'str',
        'summary': 'TemplateSummarySummary',
        'diff': 'TemplateSummaryDiff',
        'errors': 'list[TemplateSummaryErrors]'
    }

    attribute_map = {
        'sources': 'sources',
        'stack_id': 'stackID',
        'summary': 'summary',
        'diff': 'diff',
        'errors': 'errors'
    }

    def __init__(self, sources=None, stack_id=None, summary=None, diff=None, errors=None):  # noqa: E501,D401,D403
        """TemplateSummary - a model defined in OpenAPI."""  # noqa: E501
        self._sources = None
        self._stack_id = None
        self._summary = None
        self._diff = None
        self._errors = None
        self.discriminator = None

        if sources is not None:
            self.sources = sources
        if stack_id is not None:
            self.stack_id = stack_id
        if summary is not None:
            self.summary = summary
        if diff is not None:
            self.diff = diff
        if errors is not None:
            self.errors = errors

    @property
    def sources(self):
        """Get the sources of this TemplateSummary.

        :return: The sources of this TemplateSummary.
        :rtype: list[str]
        """  # noqa: E501
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Set the sources of this TemplateSummary.

        :param sources: The sources of this TemplateSummary.
        :type: list[str]
        """  # noqa: E501
        self._sources = sources

    @property
    def stack_id(self):
        """Get the stack_id of this TemplateSummary.

        :return: The stack_id of this TemplateSummary.
        :rtype: str
        """  # noqa: E501
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Set the stack_id of this TemplateSummary.

        :param stack_id: The stack_id of this TemplateSummary.
        :type: str
        """  # noqa: E501
        self._stack_id = stack_id

    @property
    def summary(self):
        """Get the summary of this TemplateSummary.

        :return: The summary of this TemplateSummary.
        :rtype: TemplateSummarySummary
        """  # noqa: E501
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Set the summary of this TemplateSummary.

        :param summary: The summary of this TemplateSummary.
        :type: TemplateSummarySummary
        """  # noqa: E501
        self._summary = summary

    @property
    def diff(self):
        """Get the diff of this TemplateSummary.

        :return: The diff of this TemplateSummary.
        :rtype: TemplateSummaryDiff
        """  # noqa: E501
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Set the diff of this TemplateSummary.

        :param diff: The diff of this TemplateSummary.
        :type: TemplateSummaryDiff
        """  # noqa: E501
        self._diff = diff

    @property
    def errors(self):
        """Get the errors of this TemplateSummary.

        :return: The errors of this TemplateSummary.
        :rtype: list[TemplateSummaryErrors]
        """  # noqa: E501
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Set the errors of this TemplateSummary.

        :param errors: The errors of this TemplateSummary.
        :type: list[TemplateSummaryErrors]
        """  # noqa: E501
        self._errors = errors

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, TemplateSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
