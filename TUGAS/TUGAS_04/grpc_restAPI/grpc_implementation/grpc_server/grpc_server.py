import grpc
from concurrent import futures
import time

from grpc_server import service_pb2, service_pb2_grpc


class TestServiceServicer(service_pb2_grpc.TestServiceServicer):
    def GetData(self, request, context):
        response = service_pb2.Response()
        response.message = f"Hello from gRPC, you sent: {request.query}"
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_TestServiceServicer_to_server(TestServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("✅ gRPC server running on port 50051")
    try:
        while True:
            time.sleep(86400)  # one day
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()