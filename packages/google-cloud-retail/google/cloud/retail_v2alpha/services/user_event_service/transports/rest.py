# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import dataclasses
import json  # type: ignore
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

from google.api import httpbody_pb2  # type: ignore
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.retail_v2alpha.types import (
    export_config,
    import_config,
    purge_config,
    user_event,
    user_event_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseUserEventServiceRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)


class UserEventServiceRestInterceptor:
    """Interceptor for UserEventService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the UserEventServiceRestTransport.

    .. code-block:: python
        class MyCustomUserEventServiceInterceptor(UserEventServiceRestInterceptor):
            def pre_collect_user_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_collect_user_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_user_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_user_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_user_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_user_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_purge_user_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_purge_user_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rejoin_user_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rejoin_user_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_write_user_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_write_user_event(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = UserEventServiceRestTransport(interceptor=MyCustomUserEventServiceInterceptor())
        client = UserEventServiceClient(transport=transport)


    """

    def pre_collect_user_event(
        self,
        request: user_event_service.CollectUserEventRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[user_event_service.CollectUserEventRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for collect_user_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserEventService server.
        """
        return request, metadata

    def post_collect_user_event(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for collect_user_event

        Override in a subclass to manipulate the response
        after it is returned by the UserEventService server but before
        it is returned to user code.
        """
        return response

    def pre_export_user_events(
        self,
        request: export_config.ExportUserEventsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[export_config.ExportUserEventsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for export_user_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserEventService server.
        """
        return request, metadata

    def post_export_user_events(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_user_events

        Override in a subclass to manipulate the response
        after it is returned by the UserEventService server but before
        it is returned to user code.
        """
        return response

    def pre_import_user_events(
        self,
        request: import_config.ImportUserEventsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[import_config.ImportUserEventsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for import_user_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserEventService server.
        """
        return request, metadata

    def post_import_user_events(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_user_events

        Override in a subclass to manipulate the response
        after it is returned by the UserEventService server but before
        it is returned to user code.
        """
        return response

    def pre_purge_user_events(
        self,
        request: purge_config.PurgeUserEventsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[purge_config.PurgeUserEventsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for purge_user_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserEventService server.
        """
        return request, metadata

    def post_purge_user_events(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for purge_user_events

        Override in a subclass to manipulate the response
        after it is returned by the UserEventService server but before
        it is returned to user code.
        """
        return response

    def pre_rejoin_user_events(
        self,
        request: user_event_service.RejoinUserEventsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[user_event_service.RejoinUserEventsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for rejoin_user_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserEventService server.
        """
        return request, metadata

    def post_rejoin_user_events(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for rejoin_user_events

        Override in a subclass to manipulate the response
        after it is returned by the UserEventService server but before
        it is returned to user code.
        """
        return response

    def pre_write_user_event(
        self,
        request: user_event_service.WriteUserEventRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[user_event_service.WriteUserEventRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for write_user_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserEventService server.
        """
        return request, metadata

    def post_write_user_event(
        self, response: user_event.UserEvent
    ) -> user_event.UserEvent:
        """Post-rpc interceptor for write_user_event

        Override in a subclass to manipulate the response
        after it is returned by the UserEventService server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserEventService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the UserEventService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserEventService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the UserEventService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class UserEventServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: UserEventServiceRestInterceptor


class UserEventServiceRestTransport(_BaseUserEventServiceRestTransport):
    """REST backend synchronous transport for UserEventService.

    Service for ingesting end user actions on the customer
    website.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "retail.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[UserEventServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'retail.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or UserEventServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/places/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*/catalogs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*/catalogs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v2alpha",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CollectUserEvent(
        _BaseUserEventServiceRestTransport._BaseCollectUserEvent,
        UserEventServiceRestStub,
    ):
        def __hash__(self):
            return hash("UserEventServiceRestTransport.CollectUserEvent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: user_event_service.CollectUserEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the collect user event method over HTTP.

            Args:
                request (~.user_event_service.CollectUserEventRequest):
                    The request object. Request message for CollectUserEvent
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = (
                _BaseUserEventServiceRestTransport._BaseCollectUserEvent._get_http_options()
            )
            request, metadata = self._interceptor.pre_collect_user_event(
                request, metadata
            )
            transcoded_request = _BaseUserEventServiceRestTransport._BaseCollectUserEvent._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseUserEventServiceRestTransport._BaseCollectUserEvent._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = UserEventServiceRestTransport._CollectUserEvent._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_collect_user_event(resp)
            return resp

    class _ExportUserEvents(
        _BaseUserEventServiceRestTransport._BaseExportUserEvents,
        UserEventServiceRestStub,
    ):
        def __hash__(self):
            return hash("UserEventServiceRestTransport.ExportUserEvents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: export_config.ExportUserEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export user events method over HTTP.

            Args:
                request (~.export_config.ExportUserEventsRequest):
                    The request object. Request message for the ``ExportUserEvents`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseUserEventServiceRestTransport._BaseExportUserEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_user_events(
                request, metadata
            )
            transcoded_request = _BaseUserEventServiceRestTransport._BaseExportUserEvents._get_transcoded_request(
                http_options, request
            )

            body = _BaseUserEventServiceRestTransport._BaseExportUserEvents._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseUserEventServiceRestTransport._BaseExportUserEvents._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = UserEventServiceRestTransport._ExportUserEvents._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_export_user_events(resp)
            return resp

    class _ImportUserEvents(
        _BaseUserEventServiceRestTransport._BaseImportUserEvents,
        UserEventServiceRestStub,
    ):
        def __hash__(self):
            return hash("UserEventServiceRestTransport.ImportUserEvents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: import_config.ImportUserEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import user events method over HTTP.

            Args:
                request (~.import_config.ImportUserEventsRequest):
                    The request object. Request message for the
                ImportUserEvents request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseUserEventServiceRestTransport._BaseImportUserEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_import_user_events(
                request, metadata
            )
            transcoded_request = _BaseUserEventServiceRestTransport._BaseImportUserEvents._get_transcoded_request(
                http_options, request
            )

            body = _BaseUserEventServiceRestTransport._BaseImportUserEvents._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseUserEventServiceRestTransport._BaseImportUserEvents._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = UserEventServiceRestTransport._ImportUserEvents._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_import_user_events(resp)
            return resp

    class _PurgeUserEvents(
        _BaseUserEventServiceRestTransport._BasePurgeUserEvents,
        UserEventServiceRestStub,
    ):
        def __hash__(self):
            return hash("UserEventServiceRestTransport.PurgeUserEvents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: purge_config.PurgeUserEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the purge user events method over HTTP.

            Args:
                request (~.purge_config.PurgeUserEventsRequest):
                    The request object. Request message for PurgeUserEvents
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseUserEventServiceRestTransport._BasePurgeUserEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_purge_user_events(
                request, metadata
            )
            transcoded_request = _BaseUserEventServiceRestTransport._BasePurgeUserEvents._get_transcoded_request(
                http_options, request
            )

            body = _BaseUserEventServiceRestTransport._BasePurgeUserEvents._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseUserEventServiceRestTransport._BasePurgeUserEvents._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = UserEventServiceRestTransport._PurgeUserEvents._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_purge_user_events(resp)
            return resp

    class _RejoinUserEvents(
        _BaseUserEventServiceRestTransport._BaseRejoinUserEvents,
        UserEventServiceRestStub,
    ):
        def __hash__(self):
            return hash("UserEventServiceRestTransport.RejoinUserEvents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: user_event_service.RejoinUserEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the rejoin user events method over HTTP.

            Args:
                request (~.user_event_service.RejoinUserEventsRequest):
                    The request object. Request message for RejoinUserEvents
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseUserEventServiceRestTransport._BaseRejoinUserEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_rejoin_user_events(
                request, metadata
            )
            transcoded_request = _BaseUserEventServiceRestTransport._BaseRejoinUserEvents._get_transcoded_request(
                http_options, request
            )

            body = _BaseUserEventServiceRestTransport._BaseRejoinUserEvents._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseUserEventServiceRestTransport._BaseRejoinUserEvents._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = UserEventServiceRestTransport._RejoinUserEvents._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_rejoin_user_events(resp)
            return resp

    class _WriteUserEvent(
        _BaseUserEventServiceRestTransport._BaseWriteUserEvent, UserEventServiceRestStub
    ):
        def __hash__(self):
            return hash("UserEventServiceRestTransport.WriteUserEvent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: user_event_service.WriteUserEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> user_event.UserEvent:
            r"""Call the write user event method over HTTP.

            Args:
                request (~.user_event_service.WriteUserEventRequest):
                    The request object. Request message for WriteUserEvent
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.user_event.UserEvent:
                    UserEvent captures all metadata
                information Retail API needs to know
                about how end users interact with
                customers' website.

            """

            http_options = (
                _BaseUserEventServiceRestTransport._BaseWriteUserEvent._get_http_options()
            )
            request, metadata = self._interceptor.pre_write_user_event(
                request, metadata
            )
            transcoded_request = _BaseUserEventServiceRestTransport._BaseWriteUserEvent._get_transcoded_request(
                http_options, request
            )

            body = _BaseUserEventServiceRestTransport._BaseWriteUserEvent._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseUserEventServiceRestTransport._BaseWriteUserEvent._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = UserEventServiceRestTransport._WriteUserEvent._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = user_event.UserEvent()
            pb_resp = user_event.UserEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_write_user_event(resp)
            return resp

    @property
    def collect_user_event(
        self,
    ) -> Callable[[user_event_service.CollectUserEventRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CollectUserEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_user_events(
        self,
    ) -> Callable[[export_config.ExportUserEventsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportUserEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_user_events(
        self,
    ) -> Callable[[import_config.ImportUserEventsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportUserEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def purge_user_events(
        self,
    ) -> Callable[[purge_config.PurgeUserEventsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PurgeUserEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rejoin_user_events(
        self,
    ) -> Callable[
        [user_event_service.RejoinUserEventsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RejoinUserEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def write_user_event(
        self,
    ) -> Callable[[user_event_service.WriteUserEventRequest], user_event.UserEvent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._WriteUserEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseUserEventServiceRestTransport._BaseGetOperation, UserEventServiceRestStub
    ):
        def __hash__(self):
            return hash("UserEventServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = (
                _BaseUserEventServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request = _BaseUserEventServiceRestTransport._BaseGetOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseUserEventServiceRestTransport._BaseGetOperation._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = UserEventServiceRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseUserEventServiceRestTransport._BaseListOperations, UserEventServiceRestStub
    ):
        def __hash__(self):
            return hash("UserEventServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = (
                _BaseUserEventServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request = _BaseUserEventServiceRestTransport._BaseListOperations._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseUserEventServiceRestTransport._BaseListOperations._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = UserEventServiceRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("UserEventServiceRestTransport",)
