import http.server
import json

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_Get(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('conten-type', 'application/json')
            self.send_header()
            self.wfile.write(bytes(json.dumps(data), "utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = 'OK'
            self.wfile.write(byte(json.dumps(info), "utf-8"))
        elif self.path == '/info':
             self.send_response(200)
             self.send_header('Content-type', 'application/json')
             self.end_headers()
             info = {"version": "1.0", "description": "A simple API built with http.server"}
             self.wfile.write*(bytes(json.dumps(info), "utf-8"))

        elif self.send_response(404):
            self.send_header('content-type', 'text/html')
            self.send_header()
            message = '404 Not found'
            self.wfile.write(bytes(message, "utf8"))

def run(server_class=http.server.HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}...'.format(server_address[1]))
    httpd.serve_forever()

if __name__ == "__main__":
    run()
