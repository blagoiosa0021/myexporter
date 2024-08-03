from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNTER = Counter('http_requests_total', 'Total number of HTTP requests')

@app.route('/')
def hello():
    REQUEST_COUNTER.inc()
    return "Hello!(my_exporter)"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5555')
