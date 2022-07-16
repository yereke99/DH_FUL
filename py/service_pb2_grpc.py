# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service_pb2 as py_dot_service__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/pb.Greeter/SayHello',
                request_serializer=py_dot_service__pb2.MessageRequest.SerializeToString,
                response_deserializer=py_dot_service__pb2.MessageReply.FromString,
                )
        self.SayHello2 = channel.unary_unary(
                '/pb.Greeter/SayHello2',
                request_serializer=py_dot_service__pb2.Message2Request.SerializeToString,
                response_deserializer=py_dot_service__pb2.Message2Reply.FromString,
                )
        self.SayHello3 = channel.unary_unary(
                '/pb.Greeter/SayHello3',
                request_serializer=py_dot_service__pb2.Message3Request.SerializeToString,
                response_deserializer=py_dot_service__pb2.Message3Reply.FromString,
                )


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello3(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=py_dot_service__pb2.MessageRequest.FromString,
                    response_serializer=py_dot_service__pb2.MessageReply.SerializeToString,
            ),
            'SayHello2': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello2,
                    request_deserializer=py_dot_service__pb2.Message2Request.FromString,
                    response_serializer=py_dot_service__pb2.Message2Reply.SerializeToString,
            ),
            'SayHello3': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello3,
                    request_deserializer=py_dot_service__pb2.Message3Request.FromString,
                    response_serializer=py_dot_service__pb2.Message3Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Greeter/SayHello',
            py_dot_service__pb2.MessageRequest.SerializeToString,
            py_dot_service__pb2.MessageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Greeter/SayHello2',
            py_dot_service__pb2.Message2Request.SerializeToString,
            py_dot_service__pb2.Message2Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello3(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Greeter/SayHello3',
            py_dot_service__pb2.Message3Request.SerializeToString,
            py_dot_service__pb2.Message3Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
