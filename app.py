from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! ArgoCD Now running our CD pipeline"

@app.route("/status")
def status():
    response = app.response_class(
        response = json.dumps({"result": "OK - healthy"}),
        status = 200,
        mimetype = "application/json"
    )
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
       response = json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 123 }}),
       status = 200,
       mimetype = 'application/json'
    )
   
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')

