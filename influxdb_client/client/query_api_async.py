"""
Querying InfluxDB by FluxLang.

Flux is InfluxData’s functional data scripting language designed for querying, analyzing, and acting on data.
"""
from typing import List

from influxdb_client import QueryService
from influxdb_client.client._base import _BaseQueryApi, _CSV_ENCODING
from influxdb_client.client.flux_table import FluxTable
from influxdb_client.client.query_api import QueryOptions


class QueryApiAsync(_BaseQueryApi):
    """Asynchronous implementation for '/api/v2/query' endpoint."""

    def __init__(self, influxdb_client, query_options=QueryOptions()):
        """
        Initialize query client.

        :param influxdb_client: influxdb client
        """
        super().__init__(influxdb_client=influxdb_client)

        self._query_options = query_options
        self._query_api = QueryService(influxdb_client.api_client)

    async def query(self, query: str, org=None, params: dict = None) -> List['FluxTable']:
        """
        Execute asynchronous Flux query and return result as a List['FluxTable'].

        :param query: the Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :param params: bind parameters
        :return:
        """
        org = self._org_param(org)

        response = await self._query_api.post_query_async(org=org,
                                                          query=self._create_query(query, self.default_dialect, params),
                                                          async_req=False, _preload_content=False,
                                                          _return_http_data_only=True)

        return await self._to_tables_async(response, query_options=self._get_query_options())

    async def query_raw(self, query: str, org=None, dialect=_BaseQueryApi.default_dialect, params: dict = None):
        """
        Execute asynchronous Flux query and return result as raw unprocessed result as a str.

        :param query: a Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :param dialect: csv dialect format
        :param params: bind parameters
        :return: str
        """
        org = self._org_param(org)
        result = await self._query_api.post_query_async(org=org, query=self._create_query(query, dialect, params),
                                                        async_req=False, _preload_content=False,
                                                        _return_http_data_only=True)
        raw_bytes = await result.read()
        return raw_bytes.decode(_CSV_ENCODING)
