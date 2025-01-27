# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.186
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ReportTemplate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'name': 'str',
        'description': 'str',
        'time_filter_supported': 'bool',
        'computer_filter_supported': 'bool',
        'tag_filter_supported': 'bool',
        'supported_formats': 'list[str]',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'time_filter_supported': 'timeFilterSupported',
        'computer_filter_supported': 'computerFilterSupported',
        'tag_filter_supported': 'tagFilterSupported',
        'supported_formats': 'supportedFormats',
        'id': 'ID'
    }

    def __init__(self, name=None, description=None, time_filter_supported=None, computer_filter_supported=None, tag_filter_supported=None, supported_formats=None, id=None):  # noqa: E501
        """ReportTemplate - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._time_filter_supported = None
        self._computer_filter_supported = None
        self._tag_filter_supported = None
        self._supported_formats = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if time_filter_supported is not None:
            self.time_filter_supported = time_filter_supported
        if computer_filter_supported is not None:
            self.computer_filter_supported = computer_filter_supported
        if tag_filter_supported is not None:
            self.tag_filter_supported = tag_filter_supported
        if supported_formats is not None:
            self.supported_formats = supported_formats
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this ReportTemplate.  # noqa: E501

        Name of the report template.  # noqa: E501

        :return: The name of this ReportTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportTemplate.

        Name of the report template.  # noqa: E501

        :param name: The name of this ReportTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ReportTemplate.  # noqa: E501

        Description of the report template.  # noqa: E501

        :return: The description of this ReportTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReportTemplate.

        Description of the report template.  # noqa: E501

        :param description: The description of this ReportTemplate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def time_filter_supported(self):
        """Gets the time_filter_supported of this ReportTemplate.  # noqa: E501

        Flag indicating whether or not the report template supports a time filter. Searchable as Boolean.  # noqa: E501

        :return: The time_filter_supported of this ReportTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._time_filter_supported

    @time_filter_supported.setter
    def time_filter_supported(self, time_filter_supported):
        """Sets the time_filter_supported of this ReportTemplate.

        Flag indicating whether or not the report template supports a time filter. Searchable as Boolean.  # noqa: E501

        :param time_filter_supported: The time_filter_supported of this ReportTemplate.  # noqa: E501
        :type: bool
        """

        self._time_filter_supported = time_filter_supported

    @property
    def computer_filter_supported(self):
        """Gets the computer_filter_supported of this ReportTemplate.  # noqa: E501

        Flag indicating whether or not the report template supports a computer filter. Searchable as Boolean.  # noqa: E501

        :return: The computer_filter_supported of this ReportTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._computer_filter_supported

    @computer_filter_supported.setter
    def computer_filter_supported(self, computer_filter_supported):
        """Sets the computer_filter_supported of this ReportTemplate.

        Flag indicating whether or not the report template supports a computer filter. Searchable as Boolean.  # noqa: E501

        :param computer_filter_supported: The computer_filter_supported of this ReportTemplate.  # noqa: E501
        :type: bool
        """

        self._computer_filter_supported = computer_filter_supported

    @property
    def tag_filter_supported(self):
        """Gets the tag_filter_supported of this ReportTemplate.  # noqa: E501

        Flag indicating whether or not the report template supports a tag filter. Searchable as Boolean.  # noqa: E501

        :return: The tag_filter_supported of this ReportTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._tag_filter_supported

    @tag_filter_supported.setter
    def tag_filter_supported(self, tag_filter_supported):
        """Sets the tag_filter_supported of this ReportTemplate.

        Flag indicating whether or not the report template supports a tag filter. Searchable as Boolean.  # noqa: E501

        :param tag_filter_supported: The tag_filter_supported of this ReportTemplate.  # noqa: E501
        :type: bool
        """

        self._tag_filter_supported = tag_filter_supported

    @property
    def supported_formats(self):
        """Gets the supported_formats of this ReportTemplate.  # noqa: E501

        List of supported report formats.  # noqa: E501

        :return: The supported_formats of this ReportTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_formats

    @supported_formats.setter
    def supported_formats(self, supported_formats):
        """Sets the supported_formats of this ReportTemplate.

        List of supported report formats.  # noqa: E501

        :param supported_formats: The supported_formats of this ReportTemplate.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["pdf", "csv", "html", "plaintext", "rtf", "xls", "xml"]  # noqa: E501
        if not set(supported_formats).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `supported_formats` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(supported_formats) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._supported_formats = supported_formats

    @property
    def id(self):
        """Gets the id of this ReportTemplate.  # noqa: E501

        ID of the report template. Searchable as ID.  # noqa: E501

        :return: The id of this ReportTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportTemplate.

        ID of the report template. Searchable as ID.  # noqa: E501

        :param id: The id of this ReportTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ReportTemplate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReportTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

