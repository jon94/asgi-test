from quart import Quart
from ddtrace.contrib.asgi import TraceMiddleware

app = Quart(__name__)
app.asgi_app = TraceMiddleware(app.asgi_app)

@app.route("/")
async def hello():
    return "Hello!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
