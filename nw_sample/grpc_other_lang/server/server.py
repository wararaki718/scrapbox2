from concurrent import futures
import logging

import grpc

import sample_pb2
import sample_pb2_grpc


class Server(sample_pb2_grpc.SampleServerServicer):
    def SampleApi(self, request, context):
        return sample_pb2.SampleResponse(message=f'hello, {request.name}!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_SampleServerServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:9000')
    
    print('start server')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
