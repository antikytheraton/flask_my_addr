from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
    # return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ == '__main__':
    app.run()