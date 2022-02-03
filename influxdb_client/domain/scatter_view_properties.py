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
from influxdb_client.domain.view_properties import ViewProperties


class ScatterViewProperties(ViewProperties):
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
        'time_format': 'str',
        'type': 'str',
        'queries': 'list[DashboardQuery]',
        'colors': 'list[str]',
        'shape': 'str',
        'note': 'str',
        'show_note_when_empty': 'bool',
        'x_column': 'str',
        'generate_x_axis_ticks': 'list[str]',
        'x_total_ticks': 'int',
        'x_tick_start': 'float',
        'x_tick_step': 'float',
        'y_column': 'str',
        'generate_y_axis_ticks': 'list[str]',
        'y_total_ticks': 'int',
        'y_tick_start': 'float',
        'y_tick_step': 'float',
        'fill_columns': 'list[str]',
        'symbol_columns': 'list[str]',
        'x_domain': 'list[float]',
        'y_domain': 'list[float]',
        'x_axis_label': 'str',
        'y_axis_label': 'str',
        'x_prefix': 'str',
        'x_suffix': 'str',
        'y_prefix': 'str',
        'y_suffix': 'str',
        'legend_colorize_rows': 'bool',
        'legend_hide': 'bool',
        'legend_opacity': 'float',
        'legend_orientation_threshold': 'int'
    }

    attribute_map = {
        'time_format': 'timeFormat',
        'type': 'type',
        'queries': 'queries',
        'colors': 'colors',
        'shape': 'shape',
        'note': 'note',
        'show_note_when_empty': 'showNoteWhenEmpty',
        'x_column': 'xColumn',
        'generate_x_axis_ticks': 'generateXAxisTicks',
        'x_total_ticks': 'xTotalTicks',
        'x_tick_start': 'xTickStart',
        'x_tick_step': 'xTickStep',
        'y_column': 'yColumn',
        'generate_y_axis_ticks': 'generateYAxisTicks',
        'y_total_ticks': 'yTotalTicks',
        'y_tick_start': 'yTickStart',
        'y_tick_step': 'yTickStep',
        'fill_columns': 'fillColumns',
        'symbol_columns': 'symbolColumns',
        'x_domain': 'xDomain',
        'y_domain': 'yDomain',
        'x_axis_label': 'xAxisLabel',
        'y_axis_label': 'yAxisLabel',
        'x_prefix': 'xPrefix',
        'x_suffix': 'xSuffix',
        'y_prefix': 'yPrefix',
        'y_suffix': 'ySuffix',
        'legend_colorize_rows': 'legendColorizeRows',
        'legend_hide': 'legendHide',
        'legend_opacity': 'legendOpacity',
        'legend_orientation_threshold': 'legendOrientationThreshold'
    }

    def __init__(self, time_format=None, type=None, queries=None, colors=None, shape=None, note=None, show_note_when_empty=None, x_column=None, generate_x_axis_ticks=None, x_total_ticks=None, x_tick_start=None, x_tick_step=None, y_column=None, generate_y_axis_ticks=None, y_total_ticks=None, y_tick_start=None, y_tick_step=None, fill_columns=None, symbol_columns=None, x_domain=None, y_domain=None, x_axis_label=None, y_axis_label=None, x_prefix=None, x_suffix=None, y_prefix=None, y_suffix=None, legend_colorize_rows=None, legend_hide=None, legend_opacity=None, legend_orientation_threshold=None):  # noqa: E501,D401,D403
        """ScatterViewProperties - a model defined in OpenAPI."""  # noqa: E501
        ViewProperties.__init__(self)  # noqa: E501

        self._time_format = None
        self._type = None
        self._queries = None
        self._colors = None
        self._shape = None
        self._note = None
        self._show_note_when_empty = None
        self._x_column = None
        self._generate_x_axis_ticks = None
        self._x_total_ticks = None
        self._x_tick_start = None
        self._x_tick_step = None
        self._y_column = None
        self._generate_y_axis_ticks = None
        self._y_total_ticks = None
        self._y_tick_start = None
        self._y_tick_step = None
        self._fill_columns = None
        self._symbol_columns = None
        self._x_domain = None
        self._y_domain = None
        self._x_axis_label = None
        self._y_axis_label = None
        self._x_prefix = None
        self._x_suffix = None
        self._y_prefix = None
        self._y_suffix = None
        self._legend_colorize_rows = None
        self._legend_hide = None
        self._legend_opacity = None
        self._legend_orientation_threshold = None
        self.discriminator = None

        if time_format is not None:
            self.time_format = time_format
        self.type = type
        self.queries = queries
        self.colors = colors
        self.shape = shape
        self.note = note
        self.show_note_when_empty = show_note_when_empty
        self.x_column = x_column
        if generate_x_axis_ticks is not None:
            self.generate_x_axis_ticks = generate_x_axis_ticks
        if x_total_ticks is not None:
            self.x_total_ticks = x_total_ticks
        if x_tick_start is not None:
            self.x_tick_start = x_tick_start
        if x_tick_step is not None:
            self.x_tick_step = x_tick_step
        self.y_column = y_column
        if generate_y_axis_ticks is not None:
            self.generate_y_axis_ticks = generate_y_axis_ticks
        if y_total_ticks is not None:
            self.y_total_ticks = y_total_ticks
        if y_tick_start is not None:
            self.y_tick_start = y_tick_start
        if y_tick_step is not None:
            self.y_tick_step = y_tick_step
        self.fill_columns = fill_columns
        self.symbol_columns = symbol_columns
        self.x_domain = x_domain
        self.y_domain = y_domain
        self.x_axis_label = x_axis_label
        self.y_axis_label = y_axis_label
        self.x_prefix = x_prefix
        self.x_suffix = x_suffix
        self.y_prefix = y_prefix
        self.y_suffix = y_suffix
        if legend_colorize_rows is not None:
            self.legend_colorize_rows = legend_colorize_rows
        if legend_hide is not None:
            self.legend_hide = legend_hide
        if legend_opacity is not None:
            self.legend_opacity = legend_opacity
        if legend_orientation_threshold is not None:
            self.legend_orientation_threshold = legend_orientation_threshold

    @property
    def time_format(self):
        """Get the time_format of this ScatterViewProperties.

        :return: The time_format of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Set the time_format of this ScatterViewProperties.

        :param time_format: The time_format of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        self._time_format = time_format

    @property
    def type(self):
        """Get the type of this ScatterViewProperties.

        :return: The type of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this ScatterViewProperties.

        :param type: The type of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def queries(self):
        """Get the queries of this ScatterViewProperties.

        :return: The queries of this ScatterViewProperties.
        :rtype: list[DashboardQuery]
        """  # noqa: E501
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Set the queries of this ScatterViewProperties.

        :param queries: The queries of this ScatterViewProperties.
        :type: list[DashboardQuery]
        """  # noqa: E501
        if queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501
        self._queries = queries

    @property
    def colors(self):
        """Get the colors of this ScatterViewProperties.

        Colors define color encoding of data into a visualization

        :return: The colors of this ScatterViewProperties.
        :rtype: list[str]
        """  # noqa: E501
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Set the colors of this ScatterViewProperties.

        Colors define color encoding of data into a visualization

        :param colors: The colors of this ScatterViewProperties.
        :type: list[str]
        """  # noqa: E501
        if colors is None:
            raise ValueError("Invalid value for `colors`, must not be `None`")  # noqa: E501
        self._colors = colors

    @property
    def shape(self):
        """Get the shape of this ScatterViewProperties.

        :return: The shape of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Set the shape of this ScatterViewProperties.

        :param shape: The shape of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501
        self._shape = shape

    @property
    def note(self):
        """Get the note of this ScatterViewProperties.

        :return: The note of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._note

    @note.setter
    def note(self, note):
        """Set the note of this ScatterViewProperties.

        :param note: The note of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501
        self._note = note

    @property
    def show_note_when_empty(self):
        """Get the show_note_when_empty of this ScatterViewProperties.

        If true, will display note when empty

        :return: The show_note_when_empty of this ScatterViewProperties.
        :rtype: bool
        """  # noqa: E501
        return self._show_note_when_empty

    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty):
        """Set the show_note_when_empty of this ScatterViewProperties.

        If true, will display note when empty

        :param show_note_when_empty: The show_note_when_empty of this ScatterViewProperties.
        :type: bool
        """  # noqa: E501
        if show_note_when_empty is None:
            raise ValueError("Invalid value for `show_note_when_empty`, must not be `None`")  # noqa: E501
        self._show_note_when_empty = show_note_when_empty

    @property
    def x_column(self):
        """Get the x_column of this ScatterViewProperties.

        :return: The x_column of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._x_column

    @x_column.setter
    def x_column(self, x_column):
        """Set the x_column of this ScatterViewProperties.

        :param x_column: The x_column of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if x_column is None:
            raise ValueError("Invalid value for `x_column`, must not be `None`")  # noqa: E501
        self._x_column = x_column

    @property
    def generate_x_axis_ticks(self):
        """Get the generate_x_axis_ticks of this ScatterViewProperties.

        :return: The generate_x_axis_ticks of this ScatterViewProperties.
        :rtype: list[str]
        """  # noqa: E501
        return self._generate_x_axis_ticks

    @generate_x_axis_ticks.setter
    def generate_x_axis_ticks(self, generate_x_axis_ticks):
        """Set the generate_x_axis_ticks of this ScatterViewProperties.

        :param generate_x_axis_ticks: The generate_x_axis_ticks of this ScatterViewProperties.
        :type: list[str]
        """  # noqa: E501
        self._generate_x_axis_ticks = generate_x_axis_ticks

    @property
    def x_total_ticks(self):
        """Get the x_total_ticks of this ScatterViewProperties.

        :return: The x_total_ticks of this ScatterViewProperties.
        :rtype: int
        """  # noqa: E501
        return self._x_total_ticks

    @x_total_ticks.setter
    def x_total_ticks(self, x_total_ticks):
        """Set the x_total_ticks of this ScatterViewProperties.

        :param x_total_ticks: The x_total_ticks of this ScatterViewProperties.
        :type: int
        """  # noqa: E501
        self._x_total_ticks = x_total_ticks

    @property
    def x_tick_start(self):
        """Get the x_tick_start of this ScatterViewProperties.

        :return: The x_tick_start of this ScatterViewProperties.
        :rtype: float
        """  # noqa: E501
        return self._x_tick_start

    @x_tick_start.setter
    def x_tick_start(self, x_tick_start):
        """Set the x_tick_start of this ScatterViewProperties.

        :param x_tick_start: The x_tick_start of this ScatterViewProperties.
        :type: float
        """  # noqa: E501
        self._x_tick_start = x_tick_start

    @property
    def x_tick_step(self):
        """Get the x_tick_step of this ScatterViewProperties.

        :return: The x_tick_step of this ScatterViewProperties.
        :rtype: float
        """  # noqa: E501
        return self._x_tick_step

    @x_tick_step.setter
    def x_tick_step(self, x_tick_step):
        """Set the x_tick_step of this ScatterViewProperties.

        :param x_tick_step: The x_tick_step of this ScatterViewProperties.
        :type: float
        """  # noqa: E501
        self._x_tick_step = x_tick_step

    @property
    def y_column(self):
        """Get the y_column of this ScatterViewProperties.

        :return: The y_column of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._y_column

    @y_column.setter
    def y_column(self, y_column):
        """Set the y_column of this ScatterViewProperties.

        :param y_column: The y_column of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if y_column is None:
            raise ValueError("Invalid value for `y_column`, must not be `None`")  # noqa: E501
        self._y_column = y_column

    @property
    def generate_y_axis_ticks(self):
        """Get the generate_y_axis_ticks of this ScatterViewProperties.

        :return: The generate_y_axis_ticks of this ScatterViewProperties.
        :rtype: list[str]
        """  # noqa: E501
        return self._generate_y_axis_ticks

    @generate_y_axis_ticks.setter
    def generate_y_axis_ticks(self, generate_y_axis_ticks):
        """Set the generate_y_axis_ticks of this ScatterViewProperties.

        :param generate_y_axis_ticks: The generate_y_axis_ticks of this ScatterViewProperties.
        :type: list[str]
        """  # noqa: E501
        self._generate_y_axis_ticks = generate_y_axis_ticks

    @property
    def y_total_ticks(self):
        """Get the y_total_ticks of this ScatterViewProperties.

        :return: The y_total_ticks of this ScatterViewProperties.
        :rtype: int
        """  # noqa: E501
        return self._y_total_ticks

    @y_total_ticks.setter
    def y_total_ticks(self, y_total_ticks):
        """Set the y_total_ticks of this ScatterViewProperties.

        :param y_total_ticks: The y_total_ticks of this ScatterViewProperties.
        :type: int
        """  # noqa: E501
        self._y_total_ticks = y_total_ticks

    @property
    def y_tick_start(self):
        """Get the y_tick_start of this ScatterViewProperties.

        :return: The y_tick_start of this ScatterViewProperties.
        :rtype: float
        """  # noqa: E501
        return self._y_tick_start

    @y_tick_start.setter
    def y_tick_start(self, y_tick_start):
        """Set the y_tick_start of this ScatterViewProperties.

        :param y_tick_start: The y_tick_start of this ScatterViewProperties.
        :type: float
        """  # noqa: E501
        self._y_tick_start = y_tick_start

    @property
    def y_tick_step(self):
        """Get the y_tick_step of this ScatterViewProperties.

        :return: The y_tick_step of this ScatterViewProperties.
        :rtype: float
        """  # noqa: E501
        return self._y_tick_step

    @y_tick_step.setter
    def y_tick_step(self, y_tick_step):
        """Set the y_tick_step of this ScatterViewProperties.

        :param y_tick_step: The y_tick_step of this ScatterViewProperties.
        :type: float
        """  # noqa: E501
        self._y_tick_step = y_tick_step

    @property
    def fill_columns(self):
        """Get the fill_columns of this ScatterViewProperties.

        :return: The fill_columns of this ScatterViewProperties.
        :rtype: list[str]
        """  # noqa: E501
        return self._fill_columns

    @fill_columns.setter
    def fill_columns(self, fill_columns):
        """Set the fill_columns of this ScatterViewProperties.

        :param fill_columns: The fill_columns of this ScatterViewProperties.
        :type: list[str]
        """  # noqa: E501
        if fill_columns is None:
            raise ValueError("Invalid value for `fill_columns`, must not be `None`")  # noqa: E501
        self._fill_columns = fill_columns

    @property
    def symbol_columns(self):
        """Get the symbol_columns of this ScatterViewProperties.

        :return: The symbol_columns of this ScatterViewProperties.
        :rtype: list[str]
        """  # noqa: E501
        return self._symbol_columns

    @symbol_columns.setter
    def symbol_columns(self, symbol_columns):
        """Set the symbol_columns of this ScatterViewProperties.

        :param symbol_columns: The symbol_columns of this ScatterViewProperties.
        :type: list[str]
        """  # noqa: E501
        if symbol_columns is None:
            raise ValueError("Invalid value for `symbol_columns`, must not be `None`")  # noqa: E501
        self._symbol_columns = symbol_columns

    @property
    def x_domain(self):
        """Get the x_domain of this ScatterViewProperties.

        :return: The x_domain of this ScatterViewProperties.
        :rtype: list[float]
        """  # noqa: E501
        return self._x_domain

    @x_domain.setter
    def x_domain(self, x_domain):
        """Set the x_domain of this ScatterViewProperties.

        :param x_domain: The x_domain of this ScatterViewProperties.
        :type: list[float]
        """  # noqa: E501
        if x_domain is None:
            raise ValueError("Invalid value for `x_domain`, must not be `None`")  # noqa: E501
        self._x_domain = x_domain

    @property
    def y_domain(self):
        """Get the y_domain of this ScatterViewProperties.

        :return: The y_domain of this ScatterViewProperties.
        :rtype: list[float]
        """  # noqa: E501
        return self._y_domain

    @y_domain.setter
    def y_domain(self, y_domain):
        """Set the y_domain of this ScatterViewProperties.

        :param y_domain: The y_domain of this ScatterViewProperties.
        :type: list[float]
        """  # noqa: E501
        if y_domain is None:
            raise ValueError("Invalid value for `y_domain`, must not be `None`")  # noqa: E501
        self._y_domain = y_domain

    @property
    def x_axis_label(self):
        """Get the x_axis_label of this ScatterViewProperties.

        :return: The x_axis_label of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._x_axis_label

    @x_axis_label.setter
    def x_axis_label(self, x_axis_label):
        """Set the x_axis_label of this ScatterViewProperties.

        :param x_axis_label: The x_axis_label of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if x_axis_label is None:
            raise ValueError("Invalid value for `x_axis_label`, must not be `None`")  # noqa: E501
        self._x_axis_label = x_axis_label

    @property
    def y_axis_label(self):
        """Get the y_axis_label of this ScatterViewProperties.

        :return: The y_axis_label of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._y_axis_label

    @y_axis_label.setter
    def y_axis_label(self, y_axis_label):
        """Set the y_axis_label of this ScatterViewProperties.

        :param y_axis_label: The y_axis_label of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if y_axis_label is None:
            raise ValueError("Invalid value for `y_axis_label`, must not be `None`")  # noqa: E501
        self._y_axis_label = y_axis_label

    @property
    def x_prefix(self):
        """Get the x_prefix of this ScatterViewProperties.

        :return: The x_prefix of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._x_prefix

    @x_prefix.setter
    def x_prefix(self, x_prefix):
        """Set the x_prefix of this ScatterViewProperties.

        :param x_prefix: The x_prefix of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if x_prefix is None:
            raise ValueError("Invalid value for `x_prefix`, must not be `None`")  # noqa: E501
        self._x_prefix = x_prefix

    @property
    def x_suffix(self):
        """Get the x_suffix of this ScatterViewProperties.

        :return: The x_suffix of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._x_suffix

    @x_suffix.setter
    def x_suffix(self, x_suffix):
        """Set the x_suffix of this ScatterViewProperties.

        :param x_suffix: The x_suffix of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if x_suffix is None:
            raise ValueError("Invalid value for `x_suffix`, must not be `None`")  # noqa: E501
        self._x_suffix = x_suffix

    @property
    def y_prefix(self):
        """Get the y_prefix of this ScatterViewProperties.

        :return: The y_prefix of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._y_prefix

    @y_prefix.setter
    def y_prefix(self, y_prefix):
        """Set the y_prefix of this ScatterViewProperties.

        :param y_prefix: The y_prefix of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if y_prefix is None:
            raise ValueError("Invalid value for `y_prefix`, must not be `None`")  # noqa: E501
        self._y_prefix = y_prefix

    @property
    def y_suffix(self):
        """Get the y_suffix of this ScatterViewProperties.

        :return: The y_suffix of this ScatterViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._y_suffix

    @y_suffix.setter
    def y_suffix(self, y_suffix):
        """Set the y_suffix of this ScatterViewProperties.

        :param y_suffix: The y_suffix of this ScatterViewProperties.
        :type: str
        """  # noqa: E501
        if y_suffix is None:
            raise ValueError("Invalid value for `y_suffix`, must not be `None`")  # noqa: E501
        self._y_suffix = y_suffix

    @property
    def legend_colorize_rows(self):
        """Get the legend_colorize_rows of this ScatterViewProperties.

        :return: The legend_colorize_rows of this ScatterViewProperties.
        :rtype: bool
        """  # noqa: E501
        return self._legend_colorize_rows

    @legend_colorize_rows.setter
    def legend_colorize_rows(self, legend_colorize_rows):
        """Set the legend_colorize_rows of this ScatterViewProperties.

        :param legend_colorize_rows: The legend_colorize_rows of this ScatterViewProperties.
        :type: bool
        """  # noqa: E501
        self._legend_colorize_rows = legend_colorize_rows

    @property
    def legend_hide(self):
        """Get the legend_hide of this ScatterViewProperties.

        :return: The legend_hide of this ScatterViewProperties.
        :rtype: bool
        """  # noqa: E501
        return self._legend_hide

    @legend_hide.setter
    def legend_hide(self, legend_hide):
        """Set the legend_hide of this ScatterViewProperties.

        :param legend_hide: The legend_hide of this ScatterViewProperties.
        :type: bool
        """  # noqa: E501
        self._legend_hide = legend_hide

    @property
    def legend_opacity(self):
        """Get the legend_opacity of this ScatterViewProperties.

        :return: The legend_opacity of this ScatterViewProperties.
        :rtype: float
        """  # noqa: E501
        return self._legend_opacity

    @legend_opacity.setter
    def legend_opacity(self, legend_opacity):
        """Set the legend_opacity of this ScatterViewProperties.

        :param legend_opacity: The legend_opacity of this ScatterViewProperties.
        :type: float
        """  # noqa: E501
        self._legend_opacity = legend_opacity

    @property
    def legend_orientation_threshold(self):
        """Get the legend_orientation_threshold of this ScatterViewProperties.

        :return: The legend_orientation_threshold of this ScatterViewProperties.
        :rtype: int
        """  # noqa: E501
        return self._legend_orientation_threshold

    @legend_orientation_threshold.setter
    def legend_orientation_threshold(self, legend_orientation_threshold):
        """Set the legend_orientation_threshold of this ScatterViewProperties.

        :param legend_orientation_threshold: The legend_orientation_threshold of this ScatterViewProperties.
        :type: int
        """  # noqa: E501
        self._legend_orientation_threshold = legend_orientation_threshold

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
        if not isinstance(other, ScatterViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
