# Filename: app.py
# pip install Quart==0.19.4 ddtrace==2.6.3 Hypercorn==0.16.0
# Run script with (on python3.9): DD_SERVICE=monkey QUART_APP=test:app1 ddtrace-run hypercorn -b 127.0.0.1:8000 test:app
# Navigate to http://localhost:8001/hello in a browser to send a trace
from quart import Quart
from ddtrace.contrib.asgi import TraceMiddleware

app1 = Quart(__name__)

@app1.route('/hello')
async def hello():
    return 'hello'

app = TraceMiddleware(app1)