from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a paritcular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')


# define called a function and a class.
def adder_function(x, y):
    return x+y

class MyFuncs:
    def mul(self, x, y):
        return x * y


def main():
    # Create server
    with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
        # register an introspection function
        # the introspection function is to change the content of an object at runtime.
        server.register_introspection_functions()

        # register functions and an instance.
        server.register_function(pow)
        server.register_function(adder_function, 'add')
        server.register_instance(MyFuncs())

        # Run main server
        server.serve_forever()
    
    return 0


if __name__ == '__main__':
    main()
