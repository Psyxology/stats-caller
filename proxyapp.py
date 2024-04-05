from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
# Enable CORS for all domains on all routes
CORS(app)

SITE_NAME = 'https://d2hfhz0c37x28y.cloudfront.net/prod/stats?details=true'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    # Forward the original query parameters to the external service
    response = requests.get(f'{SITE_NAME}{path}', params=request.args)
    # Return the content of the response from the external service
    # along with the correct content type and status code.
    return (response.content, response.status_code, response.headers.items())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
