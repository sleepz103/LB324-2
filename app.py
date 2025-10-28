# app.py
from flask import Flask, request, jsonify
from arithmetic import add


app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["GET", "POST"])
def add_endpoint():
    # Accept JSON { "a": 1, "b": 2 } or query params ?a=1&b=2
    if request.method == "POST":
        data = request.get_json() or {}
        a = data.get("a")
        b = data.get("b")
    else:
        a = request.args.get("a", type=float)
        b = request.args.get("b", type=float)
    if a is None or b is None:
        return jsonify({"error": "missing a or b"}), 400
    return jsonify({"result": add(a, b)})


if __name__ == "__main__":
    # Run on port 5000 for local testing; simple dev server is fine for demo.
    app.run(host="127.0.0.1", port=5000)
