from http.server import HTTPServer, BaseHTTPRequestHandler

class HpptHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b"Hello, This is Sam's first web server!")

def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, HpptHandler)

    print(f"Server is running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()