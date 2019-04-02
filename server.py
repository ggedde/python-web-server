import http.server
import ssl
import urllib.parse

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        params = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(self.path).query))
        secret = params.get('secret')

        if secret == '123456789':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'YOUR IN ' + bytes(str(secret), 'utf-8'))

httpd = http.server.HTTPServer(('', 4443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile="server.pem",
                               keyfile="key.pem",
                               ssl_version=ssl.PROTOCOL_TLSv1)
httpd.serve_forever()
