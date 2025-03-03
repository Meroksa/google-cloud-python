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
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.dialogflowcx_v3beta1.types import (
    generative_settings as gcdc_generative_settings,
)
from google.cloud.dialogflowcx_v3beta1.types import agent
from google.cloud.dialogflowcx_v3beta1.types import agent as gcdc_agent
from google.cloud.dialogflowcx_v3beta1.types import generative_settings

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAgentsRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)


class AgentsRestInterceptor:
    """Interceptor for Agents.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AgentsRestTransport.

    .. code-block:: python
        class MyCustomAgentsInterceptor(AgentsRestInterceptor):
            def pre_create_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_export_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_agent_validation_result(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_agent_validation_result(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_generative_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_generative_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_agents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_agents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_generative_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_generative_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_validate_agent(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_validate_agent(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AgentsRestTransport(interceptor=MyCustomAgentsInterceptor())
        client = AgentsClient(transport=transport)


    """

    def pre_create_agent(
        self,
        request: gcdc_agent.CreateAgentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[gcdc_agent.CreateAgentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_create_agent(self, response: gcdc_agent.Agent) -> gcdc_agent.Agent:
        """Post-rpc interceptor for create_agent

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_delete_agent(
        self, request: agent.DeleteAgentRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[agent.DeleteAgentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def pre_export_agent(
        self, request: agent.ExportAgentRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[agent.ExportAgentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for export_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_export_agent(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_agent

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_get_agent(
        self, request: agent.GetAgentRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[agent.GetAgentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_agent(self, response: agent.Agent) -> agent.Agent:
        """Post-rpc interceptor for get_agent

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_get_agent_validation_result(
        self,
        request: agent.GetAgentValidationResultRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[agent.GetAgentValidationResultRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_agent_validation_result

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_agent_validation_result(
        self, response: agent.AgentValidationResult
    ) -> agent.AgentValidationResult:
        """Post-rpc interceptor for get_agent_validation_result

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_get_generative_settings(
        self,
        request: agent.GetGenerativeSettingsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[agent.GetGenerativeSettingsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_generative_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_generative_settings(
        self, response: generative_settings.GenerativeSettings
    ) -> generative_settings.GenerativeSettings:
        """Post-rpc interceptor for get_generative_settings

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_list_agents(
        self, request: agent.ListAgentsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[agent.ListAgentsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_agents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_list_agents(
        self, response: agent.ListAgentsResponse
    ) -> agent.ListAgentsResponse:
        """Post-rpc interceptor for list_agents

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_restore_agent(
        self, request: agent.RestoreAgentRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[agent.RestoreAgentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for restore_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_restore_agent(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for restore_agent

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_update_agent(
        self,
        request: gcdc_agent.UpdateAgentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[gcdc_agent.UpdateAgentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_update_agent(self, response: gcdc_agent.Agent) -> gcdc_agent.Agent:
        """Post-rpc interceptor for update_agent

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_update_generative_settings(
        self,
        request: agent.UpdateGenerativeSettingsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[agent.UpdateGenerativeSettingsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_generative_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_update_generative_settings(
        self, response: gcdc_generative_settings.GenerativeSettings
    ) -> gcdc_generative_settings.GenerativeSettings:
        """Post-rpc interceptor for update_generative_settings

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_validate_agent(
        self, request: agent.ValidateAgentRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[agent.ValidateAgentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for validate_agent

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_validate_agent(
        self, response: agent.AgentValidationResult
    ) -> agent.AgentValidationResult:
        """Post-rpc interceptor for validate_agent

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
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
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
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
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
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
        before they are sent to the Agents server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Agents server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AgentsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AgentsRestInterceptor


class AgentsRestTransport(_BaseAgentsRestTransport):
    """REST backend synchronous transport for Agents.

    Service for managing
    [Agents][google.cloud.dialogflow.cx.v3beta1.Agent].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AgentsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dialogflow.googleapis.com').
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
        self._interceptor = interceptor or AgentsRestInterceptor()
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
                        "uri": "/v3beta1/{name=projects/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v3beta1/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v3beta1/{name=projects/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v3beta1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v3beta1/{name=projects/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v3beta1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v3beta1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateAgent(_BaseAgentsRestTransport._BaseCreateAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.CreateAgent")

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
            request: gcdc_agent.CreateAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gcdc_agent.Agent:
            r"""Call the create agent method over HTTP.

            Args:
                request (~.gcdc_agent.CreateAgentRequest):
                    The request object. The request message for
                [Agents.CreateAgent][google.cloud.dialogflow.cx.v3beta1.Agents.CreateAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gcdc_agent.Agent:
                    Agents are best described as Natural Language
                Understanding (NLU) modules that transform user requests
                into actionable data. You can include agents in your
                app, product, or service to determine user intent and
                respond to the user in a natural way.

                After you create an agent, you can add
                [Intents][google.cloud.dialogflow.cx.v3beta1.Intent],
                [Entity
                Types][google.cloud.dialogflow.cx.v3beta1.EntityType],
                [Flows][google.cloud.dialogflow.cx.v3beta1.Flow],
                [Fulfillments][google.cloud.dialogflow.cx.v3beta1.Fulfillment],
                [Webhooks][google.cloud.dialogflow.cx.v3beta1.Webhook],
                [TransitionRouteGroups][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup]
                and so on to manage the conversation flows.

            """

            http_options = _BaseAgentsRestTransport._BaseCreateAgent._get_http_options()
            request, metadata = self._interceptor.pre_create_agent(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseCreateAgent._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseAgentsRestTransport._BaseCreateAgent._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseCreateAgent._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._CreateAgent._get_response(
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
            resp = gcdc_agent.Agent()
            pb_resp = gcdc_agent.Agent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_agent(resp)
            return resp

    class _DeleteAgent(_BaseAgentsRestTransport._BaseDeleteAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.DeleteAgent")

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
            request: agent.DeleteAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ):
            r"""Call the delete agent method over HTTP.

            Args:
                request (~.agent.DeleteAgentRequest):
                    The request object. The request message for
                [Agents.DeleteAgent][google.cloud.dialogflow.cx.v3beta1.Agents.DeleteAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseAgentsRestTransport._BaseDeleteAgent._get_http_options()
            request, metadata = self._interceptor.pre_delete_agent(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseDeleteAgent._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseDeleteAgent._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._DeleteAgent._get_response(
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

    class _ExportAgent(_BaseAgentsRestTransport._BaseExportAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ExportAgent")

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
            request: agent.ExportAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export agent method over HTTP.

            Args:
                request (~.agent.ExportAgentRequest):
                    The request object. The request message for
                [Agents.ExportAgent][google.cloud.dialogflow.cx.v3beta1.Agents.ExportAgent].
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

            http_options = _BaseAgentsRestTransport._BaseExportAgent._get_http_options()
            request, metadata = self._interceptor.pre_export_agent(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseExportAgent._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseAgentsRestTransport._BaseExportAgent._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseExportAgent._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._ExportAgent._get_response(
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
            resp = self._interceptor.post_export_agent(resp)
            return resp

    class _GetAgent(_BaseAgentsRestTransport._BaseGetAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.GetAgent")

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
            request: agent.GetAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> agent.Agent:
            r"""Call the get agent method over HTTP.

            Args:
                request (~.agent.GetAgentRequest):
                    The request object. The request message for
                [Agents.GetAgent][google.cloud.dialogflow.cx.v3beta1.Agents.GetAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.agent.Agent:
                    Agents are best described as Natural Language
                Understanding (NLU) modules that transform user requests
                into actionable data. You can include agents in your
                app, product, or service to determine user intent and
                respond to the user in a natural way.

                After you create an agent, you can add
                [Intents][google.cloud.dialogflow.cx.v3beta1.Intent],
                [Entity
                Types][google.cloud.dialogflow.cx.v3beta1.EntityType],
                [Flows][google.cloud.dialogflow.cx.v3beta1.Flow],
                [Fulfillments][google.cloud.dialogflow.cx.v3beta1.Fulfillment],
                [Webhooks][google.cloud.dialogflow.cx.v3beta1.Webhook],
                [TransitionRouteGroups][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup]
                and so on to manage the conversation flows.

            """

            http_options = _BaseAgentsRestTransport._BaseGetAgent._get_http_options()
            request, metadata = self._interceptor.pre_get_agent(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseGetAgent._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseGetAgent._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._GetAgent._get_response(
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
            resp = agent.Agent()
            pb_resp = agent.Agent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_agent(resp)
            return resp

    class _GetAgentValidationResult(
        _BaseAgentsRestTransport._BaseGetAgentValidationResult, AgentsRestStub
    ):
        def __hash__(self):
            return hash("AgentsRestTransport.GetAgentValidationResult")

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
            request: agent.GetAgentValidationResultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> agent.AgentValidationResult:
            r"""Call the get agent validation
            result method over HTTP.

                Args:
                    request (~.agent.GetAgentValidationResultRequest):
                        The request object. The request message for
                    [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3beta1.Agents.GetAgentValidationResult].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.agent.AgentValidationResult:
                        The response message for
                    [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3beta1.Agents.GetAgentValidationResult].

            """

            http_options = (
                _BaseAgentsRestTransport._BaseGetAgentValidationResult._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_agent_validation_result(
                request, metadata
            )
            transcoded_request = _BaseAgentsRestTransport._BaseGetAgentValidationResult._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseAgentsRestTransport._BaseGetAgentValidationResult._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = AgentsRestTransport._GetAgentValidationResult._get_response(
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
            resp = agent.AgentValidationResult()
            pb_resp = agent.AgentValidationResult.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_agent_validation_result(resp)
            return resp

    class _GetGenerativeSettings(
        _BaseAgentsRestTransport._BaseGetGenerativeSettings, AgentsRestStub
    ):
        def __hash__(self):
            return hash("AgentsRestTransport.GetGenerativeSettings")

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
            request: agent.GetGenerativeSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> generative_settings.GenerativeSettings:
            r"""Call the get generative settings method over HTTP.

            Args:
                request (~.agent.GetGenerativeSettingsRequest):
                    The request object. Request for
                [GetGenerativeSettings][google.cloud.dialogflow.cx.v3beta1.Agents.GetGenerativeSettings]
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.generative_settings.GenerativeSettings:
                    Settings for Generative AI.
            """

            http_options = (
                _BaseAgentsRestTransport._BaseGetGenerativeSettings._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_generative_settings(
                request, metadata
            )
            transcoded_request = _BaseAgentsRestTransport._BaseGetGenerativeSettings._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseAgentsRestTransport._BaseGetGenerativeSettings._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = AgentsRestTransport._GetGenerativeSettings._get_response(
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
            resp = generative_settings.GenerativeSettings()
            pb_resp = generative_settings.GenerativeSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_generative_settings(resp)
            return resp

    class _ListAgents(_BaseAgentsRestTransport._BaseListAgents, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ListAgents")

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
            request: agent.ListAgentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> agent.ListAgentsResponse:
            r"""Call the list agents method over HTTP.

            Args:
                request (~.agent.ListAgentsRequest):
                    The request object. The request message for
                [Agents.ListAgents][google.cloud.dialogflow.cx.v3beta1.Agents.ListAgents].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.agent.ListAgentsResponse:
                    The response message for
                [Agents.ListAgents][google.cloud.dialogflow.cx.v3beta1.Agents.ListAgents].

            """

            http_options = _BaseAgentsRestTransport._BaseListAgents._get_http_options()
            request, metadata = self._interceptor.pre_list_agents(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseListAgents._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseListAgents._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._ListAgents._get_response(
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
            resp = agent.ListAgentsResponse()
            pb_resp = agent.ListAgentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_agents(resp)
            return resp

    class _RestoreAgent(_BaseAgentsRestTransport._BaseRestoreAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.RestoreAgent")

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
            request: agent.RestoreAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the restore agent method over HTTP.

            Args:
                request (~.agent.RestoreAgentRequest):
                    The request object. The request message for
                [Agents.RestoreAgent][google.cloud.dialogflow.cx.v3beta1.Agents.RestoreAgent].
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
                _BaseAgentsRestTransport._BaseRestoreAgent._get_http_options()
            )
            request, metadata = self._interceptor.pre_restore_agent(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseRestoreAgent._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseAgentsRestTransport._BaseRestoreAgent._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseRestoreAgent._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._RestoreAgent._get_response(
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
            resp = self._interceptor.post_restore_agent(resp)
            return resp

    class _UpdateAgent(_BaseAgentsRestTransport._BaseUpdateAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.UpdateAgent")

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
            request: gcdc_agent.UpdateAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gcdc_agent.Agent:
            r"""Call the update agent method over HTTP.

            Args:
                request (~.gcdc_agent.UpdateAgentRequest):
                    The request object. The request message for
                [Agents.UpdateAgent][google.cloud.dialogflow.cx.v3beta1.Agents.UpdateAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gcdc_agent.Agent:
                    Agents are best described as Natural Language
                Understanding (NLU) modules that transform user requests
                into actionable data. You can include agents in your
                app, product, or service to determine user intent and
                respond to the user in a natural way.

                After you create an agent, you can add
                [Intents][google.cloud.dialogflow.cx.v3beta1.Intent],
                [Entity
                Types][google.cloud.dialogflow.cx.v3beta1.EntityType],
                [Flows][google.cloud.dialogflow.cx.v3beta1.Flow],
                [Fulfillments][google.cloud.dialogflow.cx.v3beta1.Fulfillment],
                [Webhooks][google.cloud.dialogflow.cx.v3beta1.Webhook],
                [TransitionRouteGroups][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup]
                and so on to manage the conversation flows.

            """

            http_options = _BaseAgentsRestTransport._BaseUpdateAgent._get_http_options()
            request, metadata = self._interceptor.pre_update_agent(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseUpdateAgent._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseAgentsRestTransport._BaseUpdateAgent._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseUpdateAgent._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._UpdateAgent._get_response(
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
            resp = gcdc_agent.Agent()
            pb_resp = gcdc_agent.Agent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_agent(resp)
            return resp

    class _UpdateGenerativeSettings(
        _BaseAgentsRestTransport._BaseUpdateGenerativeSettings, AgentsRestStub
    ):
        def __hash__(self):
            return hash("AgentsRestTransport.UpdateGenerativeSettings")

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
            request: agent.UpdateGenerativeSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gcdc_generative_settings.GenerativeSettings:
            r"""Call the update generative
            settings method over HTTP.

                Args:
                    request (~.agent.UpdateGenerativeSettingsRequest):
                        The request object. Request for
                    [UpdateGenerativeSettings][google.cloud.dialogflow.cx.v3beta1.Agents.UpdateGenerativeSettings]
                    RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.gcdc_generative_settings.GenerativeSettings:
                        Settings for Generative AI.
            """

            http_options = (
                _BaseAgentsRestTransport._BaseUpdateGenerativeSettings._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_generative_settings(
                request, metadata
            )
            transcoded_request = _BaseAgentsRestTransport._BaseUpdateGenerativeSettings._get_transcoded_request(
                http_options, request
            )

            body = _BaseAgentsRestTransport._BaseUpdateGenerativeSettings._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseAgentsRestTransport._BaseUpdateGenerativeSettings._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = AgentsRestTransport._UpdateGenerativeSettings._get_response(
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
            resp = gcdc_generative_settings.GenerativeSettings()
            pb_resp = gcdc_generative_settings.GenerativeSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_generative_settings(resp)
            return resp

    class _ValidateAgent(_BaseAgentsRestTransport._BaseValidateAgent, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ValidateAgent")

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
            request: agent.ValidateAgentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> agent.AgentValidationResult:
            r"""Call the validate agent method over HTTP.

            Args:
                request (~.agent.ValidateAgentRequest):
                    The request object. The request message for
                [Agents.ValidateAgent][google.cloud.dialogflow.cx.v3beta1.Agents.ValidateAgent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.agent.AgentValidationResult:
                    The response message for
                [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3beta1.Agents.GetAgentValidationResult].

            """

            http_options = (
                _BaseAgentsRestTransport._BaseValidateAgent._get_http_options()
            )
            request, metadata = self._interceptor.pre_validate_agent(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseValidateAgent._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseAgentsRestTransport._BaseValidateAgent._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseValidateAgent._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._ValidateAgent._get_response(
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
            resp = agent.AgentValidationResult()
            pb_resp = agent.AgentValidationResult.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_validate_agent(resp)
            return resp

    @property
    def create_agent(
        self,
    ) -> Callable[[gcdc_agent.CreateAgentRequest], gcdc_agent.Agent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_agent(self) -> Callable[[agent.DeleteAgentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_agent(
        self,
    ) -> Callable[[agent.ExportAgentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_agent(self) -> Callable[[agent.GetAgentRequest], agent.Agent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_agent_validation_result(
        self,
    ) -> Callable[[agent.GetAgentValidationResultRequest], agent.AgentValidationResult]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAgentValidationResult(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_generative_settings(
        self,
    ) -> Callable[
        [agent.GetGenerativeSettingsRequest], generative_settings.GenerativeSettings
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGenerativeSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_agents(
        self,
    ) -> Callable[[agent.ListAgentsRequest], agent.ListAgentsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAgents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_agent(
        self,
    ) -> Callable[[agent.RestoreAgentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_agent(
        self,
    ) -> Callable[[gcdc_agent.UpdateAgentRequest], gcdc_agent.Agent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_generative_settings(
        self,
    ) -> Callable[
        [agent.UpdateGenerativeSettingsRequest],
        gcdc_generative_settings.GenerativeSettings,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGenerativeSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def validate_agent(
        self,
    ) -> Callable[[agent.ValidateAgentRequest], agent.AgentValidationResult]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ValidateAgent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseAgentsRestTransport._BaseGetLocation, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = _BaseAgentsRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseGetLocation._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseGetLocation._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._GetLocation._get_response(
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
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(_BaseAgentsRestTransport._BaseListLocations, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = (
                _BaseAgentsRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseListLocations._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseListLocations._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._ListLocations._get_response(
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
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseAgentsRestTransport._BaseCancelOperation, AgentsRestStub
    ):
        def __hash__(self):
            return hash("AgentsRestTransport.CancelOperation")

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
                _BaseAgentsRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request = (
                _BaseAgentsRestTransport._BaseCancelOperation._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseCancelOperation._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(_BaseAgentsRestTransport._BaseGetOperation, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.GetOperation")

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
                _BaseAgentsRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseGetOperation._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseGetOperation._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._GetOperation._get_response(
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

    class _ListOperations(_BaseAgentsRestTransport._BaseListOperations, AgentsRestStub):
        def __hash__(self):
            return hash("AgentsRestTransport.ListOperations")

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
                _BaseAgentsRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request = (
                _BaseAgentsRestTransport._BaseListOperations._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseAgentsRestTransport._BaseListOperations._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = AgentsRestTransport._ListOperations._get_response(
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


__all__ = ("AgentsRestTransport",)
