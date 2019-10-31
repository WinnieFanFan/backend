from backend.apis import api
from flask import Flask, Response
import json

app = Flask(__name__)

api.init_app(app)

@app.route("/health")
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
