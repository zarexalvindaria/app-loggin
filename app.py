from flask import Flask, json
import logging

app = Flask(__name__)


@app.route("/")
def hello():

    app.logger.info('Main request successful.')
    return "Hello world!"


@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Status endpoint was reached.')
    return response


@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics endpoint was reached.')

    return response


if __name__ == "__main__":
    # create the log file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='0.0.0.0')
