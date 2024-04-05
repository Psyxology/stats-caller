from flask import Flask
from requests import get

app = Flask(__name__)
SITE_NAME = 'https://d2hfhz0c37x28y.cloudfront.net/prod/stats?details=true'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  return get(f'{SITE_NAME}{path}').content

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
