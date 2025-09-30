import time
import grpc
from locust import User, task, between, events
import sys, os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from grpc_server import service_pb2, service_pb2_grpc


class GRPCUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        self.channel = grpc.insecure_channel("127.0.0.1:50051")
        self.stub = service_pb2_grpc.TestServiceStub(self.channel)

    @task
    def get_data(self):
        start = time.perf_counter()
        try:
            request = service_pb2.Request(query="Locust")
            response = self.stub.GetData(request, timeout=5)  # 5s timeout
            total_ms = int((time.perf_counter() - start) * 1000)
            events.request.fire(request_type="grpc", name="GetData", response_time=total_ms, response_length=0, exception=None)
        except Exception as e:
            total_ms = int((time.perf_counter() - start) * 1000)
            events.request.fire(request_type="grpc", name="GetData", response_time=total_ms, response_length=0, exception=e)