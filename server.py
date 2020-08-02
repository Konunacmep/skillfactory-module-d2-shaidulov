import os
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
from bottle import route, run, Bottle

sentry_sdk.init(
    dsn="https://76aaf7fce9b043459c0e035cbbe25209@o421101.ingest.sentry.io/5340365",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route("/")
def index():
    return "use '/success' or '/fail'"

@app.route("/success")
def success():
  return "nothing bad happened"

@app.route("/fail")
def fail():
    raise RuntimeError("an error has occured")
    return

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=2,
    )
else:
    app.run(host="localhost", port=8080, debug=True)
