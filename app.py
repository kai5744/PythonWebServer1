from http.server import HTTPServer, SimpleHTTPRequestHandler

class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'hello world')

        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')

        elif self.path == '/version':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"version":"1.0.0"}')

        elif self.path.startswith('/echo'):
            from urllib.parse import urlparse, parse_qs
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            import json
            self.wfile.write(json.dumps(query).encode())

        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/uppercase':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
    
            response = body.decode().upper().encode()

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_response(404)
            self.end_headers()
print('I AM A SERVER')
print('hi i am still a server buenos dias')
HTTPServer(("", 8080), HelloWorldHandler).serve_forever()  
