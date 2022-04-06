import requests
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/rpc',)


def main():
    # The port should be dynamically determined, and communicated
    # with the app through stdout.
    with SimpleXMLRPCServer(
        ('localhost', 7676),
        requestHandler=RequestHandler
    ) as server:
        server.register_introspection_functions()

        @server.register_function
        def send_request(
            method,
            host,
            port,
            path
        ):
            response = requests.request(
                method,
                f"{host}:{port}{path}"
            )
            return {
                "status_code": response.status_code
            }

        server.serve_forever()


if __name__ == '__main__':
    main()
