from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import json
from datetime import datetime

class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        response_data = {
            "message": "Redirecting to https://samlee.us",
            "status": "success",
            "redirect": True,
            "url": "https://samlee.us",
            "data": {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "server": "Python HTTP Server",
                "port": 8000
            }
        }
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, HttpHandler)

    print(f"Server is running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()