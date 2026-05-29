from flask import Flask, jsonify
from ssl_config import create_ssl_context

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "secure server running"
    })

@app.route("/client-info")
def client_info():
    return jsonify({
        "message": "mTLS successful connection",
        "status": "client verified at TLS level"
    })

if __name__ == "__main__":

    context = create_ssl_context()

    app.run(
        host="0.0.0.0",
        port=4433,
        ssl_context=context,
        debug=False
    )
      
