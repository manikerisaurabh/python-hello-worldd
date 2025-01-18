from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Parse query parameters
        query = urlparse(self.path).query
        params = parse_qs(query)

        # Extract parameters
        submission_id = params.get('submission_id', [None])[0]
        assignment_id = params.get('assignment_id', [None])[0]
        user_id = params.get('user_id', [None])[0]

        # Response content
        response_message = (
            f"Submission ID: {submission_id}\n"
            f"Assignment ID: {assignment_id}\n"
            f"User ID: {user_id}\n"
        )

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_message.encode('utf-8'))
        return
