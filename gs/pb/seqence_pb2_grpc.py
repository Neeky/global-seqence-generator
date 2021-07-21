# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gs.pb import seqence_pb2 as seqence__pb2


class SeqenceStub(object):
    """Seqence 服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_id = channel.unary_unary(
                '/Seqence/get_id',
                request_serializer=seqence__pb2.Request.SerializeToString,
                response_deserializer=seqence__pb2.SeqenceID.FromString,
                )


class SeqenceServicer(object):
    """Seqence 服务
    """

    def get_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SeqenceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_id': grpc.unary_unary_rpc_method_handler(
                    servicer.get_id,
                    request_deserializer=seqence__pb2.Request.FromString,
                    response_serializer=seqence__pb2.SeqenceID.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Seqence', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Seqence(object):
    """Seqence 服务
    """

    @staticmethod
    def get_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Seqence/get_id',
            seqence__pb2.Request.SerializeToString,
            seqence__pb2.SeqenceID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)