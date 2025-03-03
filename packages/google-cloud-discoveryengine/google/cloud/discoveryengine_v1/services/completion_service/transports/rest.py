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

from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.discoveryengine_v1.types import (
    completion_service,
    import_config,
    purge_config,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCompletionServiceRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)


class CompletionServiceRestInterceptor:
    """Interceptor for CompletionService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CompletionServiceRestTransport.

    .. code-block:: python
        class MyCustomCompletionServiceInterceptor(CompletionServiceRestInterceptor):
            def pre_complete_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_complete_query(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_completion_suggestions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_completion_suggestions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_suggestion_deny_list_entries(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_suggestion_deny_list_entries(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_purge_completion_suggestions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_purge_completion_suggestions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_purge_suggestion_deny_list_entries(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_purge_suggestion_deny_list_entries(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CompletionServiceRestTransport(interceptor=MyCustomCompletionServiceInterceptor())
        client = CompletionServiceClient(transport=transport)


    """

    def pre_complete_query(
        self,
        request: completion_service.CompleteQueryRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[completion_service.CompleteQueryRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for complete_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompletionService server.
        """
        return request, metadata

    def post_complete_query(
        self, response: completion_service.CompleteQueryResponse
    ) -> completion_service.CompleteQueryResponse:
        """Post-rpc interceptor for complete_query

        Override in a subclass to manipulate the response
        after it is returned by the CompletionService server but before
        it is returned to user code.
        """
        return response

    def pre_import_completion_suggestions(
        self,
        request: import_config.ImportCompletionSuggestionsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        import_config.ImportCompletionSuggestionsRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for import_completion_suggestions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompletionService server.
        """
        return request, metadata

    def post_import_completion_suggestions(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_completion_suggestions

        Override in a subclass to manipulate the response
        after it is returned by the CompletionService server but before
        it is returned to user code.
        """
        return response

    def pre_import_suggestion_deny_list_entries(
        self,
        request: import_config.ImportSuggestionDenyListEntriesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        import_config.ImportSuggestionDenyListEntriesRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for import_suggestion_deny_list_entries

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompletionService server.
        """
        return request, metadata

    def post_import_suggestion_deny_list_entries(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_suggestion_deny_list_entries

        Override in a subclass to manipulate the response
        after it is returned by the CompletionService server but before
        it is returned to user code.
        """
        return response

    def pre_purge_completion_suggestions(
        self,
        request: purge_config.PurgeCompletionSuggestionsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        purge_config.PurgeCompletionSuggestionsRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for purge_completion_suggestions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompletionService server.
        """
        return request, metadata

    def post_purge_completion_suggestions(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for purge_completion_suggestions

        Override in a subclass to manipulate the response
        after it is returned by the CompletionService server but before
        it is returned to user code.
        """
        return response

    def pre_purge_suggestion_deny_list_entries(
        self,
        request: purge_config.PurgeSuggestionDenyListEntriesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        purge_config.PurgeSuggestionDenyListEntriesRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for purge_suggestion_deny_list_entries

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompletionService server.
        """
        return request, metadata

    def post_purge_suggestion_deny_list_entries(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for purge_suggestion_deny_list_entries

        Override in a subclass to manipulate the response
        after it is returned by the CompletionService server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CompletionService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CompletionService server but before
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
        before they are sent to the CompletionService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CompletionService server but before
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
        before they are sent to the CompletionService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the CompletionService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CompletionServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CompletionServiceRestInterceptor


class CompletionServiceRestTransport(_BaseCompletionServiceRestTransport):
    """REST backend synchronous transport for CompletionService.

    Service for Auto-Completion.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "discoveryengine.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CompletionServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'discoveryengine.googleapis.com').
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
        self._interceptor = interceptor or CompletionServiceRestInterceptor()
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
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/operations/*}:cancel",
                        "body": "*",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/operations/*}:cancel",
                        "body": "*",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/dataStores/*/branches/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataConnector/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/models/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/engines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/dataStores/*/branches/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/dataStores/*/models/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/dataStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/identityMappingStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataConnector}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/models/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/dataStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*/engines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/collections/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/dataStores/*/branches/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/dataStores/*/models/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/dataStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/identityMappingStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CompleteQuery(
        _BaseCompletionServiceRestTransport._BaseCompleteQuery,
        CompletionServiceRestStub,
    ):
        def __hash__(self):
            return hash("CompletionServiceRestTransport.CompleteQuery")

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
            request: completion_service.CompleteQueryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> completion_service.CompleteQueryResponse:
            r"""Call the complete query method over HTTP.

            Args:
                request (~.completion_service.CompleteQueryRequest):
                    The request object. Request message for
                [CompletionService.CompleteQuery][google.cloud.discoveryengine.v1.CompletionService.CompleteQuery]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.completion_service.CompleteQueryResponse:
                    Response message for
                [CompletionService.CompleteQuery][google.cloud.discoveryengine.v1.CompletionService.CompleteQuery]
                method.

            """

            http_options = (
                _BaseCompletionServiceRestTransport._BaseCompleteQuery._get_http_options()
            )
            request, metadata = self._interceptor.pre_complete_query(request, metadata)
            transcoded_request = _BaseCompletionServiceRestTransport._BaseCompleteQuery._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseCompletionServiceRestTransport._BaseCompleteQuery._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = CompletionServiceRestTransport._CompleteQuery._get_response(
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
            resp = completion_service.CompleteQueryResponse()
            pb_resp = completion_service.CompleteQueryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_complete_query(resp)
            return resp

    class _ImportCompletionSuggestions(
        _BaseCompletionServiceRestTransport._BaseImportCompletionSuggestions,
        CompletionServiceRestStub,
    ):
        def __hash__(self):
            return hash("CompletionServiceRestTransport.ImportCompletionSuggestions")

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
            request: import_config.ImportCompletionSuggestionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import completion
            suggestions method over HTTP.

                Args:
                    request (~.import_config.ImportCompletionSuggestionsRequest):
                        The request object. Request message for
                    [CompletionService.ImportCompletionSuggestions][google.cloud.discoveryengine.v1.CompletionService.ImportCompletionSuggestions]
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
                _BaseCompletionServiceRestTransport._BaseImportCompletionSuggestions._get_http_options()
            )
            request, metadata = self._interceptor.pre_import_completion_suggestions(
                request, metadata
            )
            transcoded_request = _BaseCompletionServiceRestTransport._BaseImportCompletionSuggestions._get_transcoded_request(
                http_options, request
            )

            body = _BaseCompletionServiceRestTransport._BaseImportCompletionSuggestions._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseCompletionServiceRestTransport._BaseImportCompletionSuggestions._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = CompletionServiceRestTransport._ImportCompletionSuggestions._get_response(
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
            resp = self._interceptor.post_import_completion_suggestions(resp)
            return resp

    class _ImportSuggestionDenyListEntries(
        _BaseCompletionServiceRestTransport._BaseImportSuggestionDenyListEntries,
        CompletionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CompletionServiceRestTransport.ImportSuggestionDenyListEntries"
            )

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
            request: import_config.ImportSuggestionDenyListEntriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import suggestion deny
            list entries method over HTTP.

                Args:
                    request (~.import_config.ImportSuggestionDenyListEntriesRequest):
                        The request object. Request message for
                    [CompletionService.ImportSuggestionDenyListEntries][google.cloud.discoveryengine.v1.CompletionService.ImportSuggestionDenyListEntries]
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
                _BaseCompletionServiceRestTransport._BaseImportSuggestionDenyListEntries._get_http_options()
            )
            (
                request,
                metadata,
            ) = self._interceptor.pre_import_suggestion_deny_list_entries(
                request, metadata
            )
            transcoded_request = _BaseCompletionServiceRestTransport._BaseImportSuggestionDenyListEntries._get_transcoded_request(
                http_options, request
            )

            body = _BaseCompletionServiceRestTransport._BaseImportSuggestionDenyListEntries._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseCompletionServiceRestTransport._BaseImportSuggestionDenyListEntries._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = CompletionServiceRestTransport._ImportSuggestionDenyListEntries._get_response(
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
            resp = self._interceptor.post_import_suggestion_deny_list_entries(resp)
            return resp

    class _PurgeCompletionSuggestions(
        _BaseCompletionServiceRestTransport._BasePurgeCompletionSuggestions,
        CompletionServiceRestStub,
    ):
        def __hash__(self):
            return hash("CompletionServiceRestTransport.PurgeCompletionSuggestions")

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
            request: purge_config.PurgeCompletionSuggestionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the purge completion
            suggestions method over HTTP.

                Args:
                    request (~.purge_config.PurgeCompletionSuggestionsRequest):
                        The request object. Request message for
                    [CompletionService.PurgeCompletionSuggestions][google.cloud.discoveryengine.v1.CompletionService.PurgeCompletionSuggestions]
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
                _BaseCompletionServiceRestTransport._BasePurgeCompletionSuggestions._get_http_options()
            )
            request, metadata = self._interceptor.pre_purge_completion_suggestions(
                request, metadata
            )
            transcoded_request = _BaseCompletionServiceRestTransport._BasePurgeCompletionSuggestions._get_transcoded_request(
                http_options, request
            )

            body = _BaseCompletionServiceRestTransport._BasePurgeCompletionSuggestions._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseCompletionServiceRestTransport._BasePurgeCompletionSuggestions._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = CompletionServiceRestTransport._PurgeCompletionSuggestions._get_response(
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
            resp = self._interceptor.post_purge_completion_suggestions(resp)
            return resp

    class _PurgeSuggestionDenyListEntries(
        _BaseCompletionServiceRestTransport._BasePurgeSuggestionDenyListEntries,
        CompletionServiceRestStub,
    ):
        def __hash__(self):
            return hash("CompletionServiceRestTransport.PurgeSuggestionDenyListEntries")

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
            request: purge_config.PurgeSuggestionDenyListEntriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the purge suggestion deny
            list entries method over HTTP.

                Args:
                    request (~.purge_config.PurgeSuggestionDenyListEntriesRequest):
                        The request object. Request message for
                    [CompletionService.PurgeSuggestionDenyListEntries][google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestionDenyListEntries]
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
                _BaseCompletionServiceRestTransport._BasePurgeSuggestionDenyListEntries._get_http_options()
            )
            (
                request,
                metadata,
            ) = self._interceptor.pre_purge_suggestion_deny_list_entries(
                request, metadata
            )
            transcoded_request = _BaseCompletionServiceRestTransport._BasePurgeSuggestionDenyListEntries._get_transcoded_request(
                http_options, request
            )

            body = _BaseCompletionServiceRestTransport._BasePurgeSuggestionDenyListEntries._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseCompletionServiceRestTransport._BasePurgeSuggestionDenyListEntries._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = CompletionServiceRestTransport._PurgeSuggestionDenyListEntries._get_response(
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
            resp = self._interceptor.post_purge_suggestion_deny_list_entries(resp)
            return resp

    @property
    def complete_query(
        self,
    ) -> Callable[
        [completion_service.CompleteQueryRequest],
        completion_service.CompleteQueryResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CompleteQuery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_completion_suggestions(
        self,
    ) -> Callable[
        [import_config.ImportCompletionSuggestionsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportCompletionSuggestions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_suggestion_deny_list_entries(
        self,
    ) -> Callable[
        [import_config.ImportSuggestionDenyListEntriesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportSuggestionDenyListEntries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def purge_completion_suggestions(
        self,
    ) -> Callable[
        [purge_config.PurgeCompletionSuggestionsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PurgeCompletionSuggestions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def purge_suggestion_deny_list_entries(
        self,
    ) -> Callable[
        [purge_config.PurgeSuggestionDenyListEntriesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PurgeSuggestionDenyListEntries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseCompletionServiceRestTransport._BaseCancelOperation,
        CompletionServiceRestStub,
    ):
        def __hash__(self):
            return hash("CompletionServiceRestTransport.CancelOperation")

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
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = (
                _BaseCompletionServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request = _BaseCompletionServiceRestTransport._BaseCancelOperation._get_transcoded_request(
                http_options, request
            )

            body = _BaseCompletionServiceRestTransport._BaseCancelOperation._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseCompletionServiceRestTransport._BaseCancelOperation._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = CompletionServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseCompletionServiceRestTransport._BaseGetOperation, CompletionServiceRestStub
    ):
        def __hash__(self):
            return hash("CompletionServiceRestTransport.GetOperation")

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
                _BaseCompletionServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request = _BaseCompletionServiceRestTransport._BaseGetOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseCompletionServiceRestTransport._BaseGetOperation._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = CompletionServiceRestTransport._GetOperation._get_response(
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
        _BaseCompletionServiceRestTransport._BaseListOperations,
        CompletionServiceRestStub,
    ):
        def __hash__(self):
            return hash("CompletionServiceRestTransport.ListOperations")

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
                _BaseCompletionServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request = _BaseCompletionServiceRestTransport._BaseListOperations._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseCompletionServiceRestTransport._BaseListOperations._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = CompletionServiceRestTransport._ListOperations._get_response(
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


__all__ = ("CompletionServiceRestTransport",)
