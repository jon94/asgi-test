from quart import Quart
from ddtrace.contrib.asgi import TraceMiddleware

app = Quart(__name__)  # Rename the Quart instance to 'app'

@app.route("/api")  # Use the 'app' instance for routing
async def hello():
    return 'hello'

app = TraceMiddleware(app)