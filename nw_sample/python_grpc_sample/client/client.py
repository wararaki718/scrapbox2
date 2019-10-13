import logging

import grpc

import sample_pb2
import sample_pb2_grpc


def main():
    print('server access')
    with grpc.insecure_channel('localhost:9000') as channel:
        stub = sample_pb2_grpc.SampleServerStub(channel)
        response = stub.SampleApi(sample_pb2.SampleRequest(name='test'))
    print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    main()
