from email import message
from dh import*
import logging
from concurrent.futures import ThreadPoolExecutor

import grpc
import time

import service_pb2  
import service_pb2_grpc 



class Greeter():
    client_public_keys = 0
    client_part_keys= 0
    server_partKey = 0
    server_full_key = 0

    server_public_key = 151151
    server_private_key = 157157

    def SayHello(self, request, context):
        client_public_key = request.name
        print('Client"s public key: %s' % request.name)
        Greeter.client_public_keys = int(client_public_key)
        """
        client_public_key = int(message)
        server = DH_Endpoint(int(client_public_key), server_public_key, server_private_key)
        partial_key = server.generate_partial_key()
        """ 
        return service_pb2.MessageReply(message=str(Greeter.server_public_key))
    
    def SayHello2(self, request, context):
        message = request.name
         
        print('Client"s part key: %s' % message)
        Greeter.client_part_keys = int(message)
        server = DH_Endpoint(Greeter.server_public_key, int(Greeter.client_public_keys), Greeter.server_private_key)
        Greeter.server_partKey = server.generate_partial_key() 
        return service_pb2.Message2Reply(message=str(Greeter.server_partKey))

    def SayHello3(self, request, context):
        message = request.name
        print('The key: %s' % request.name)
        #Greeter.client_part_keys = int(message)
        server = DH_Endpoint(Greeter.server_public_key, int(Greeter.client_public_keys), Greeter.server_private_key)
        Greeter.server_full_key = server.generate_full_key(Greeter.client_part_keys)
        print("The full key: ", Greeter.server_full_key)
        return service_pb2.Message3Reply(message='Server is generated full key: %s' % "server generated the full key!")


    
def server():
    server = grpc.server(ThreadPoolExecutor(max_workers=1))
    service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server=server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        server.stop()

if __name__ == "__main__":
    logging.basicConfig()
    print("Server started...")
    server()