from flask import Flask, request

app = Flask(__name__)

sites = {}
reports = {}


@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    sites[data["id"]] = data["html"]
    return {"ok": True}


@app.route("/site/<id>")
def site(id):
    return sites.get(id, "not found")


@app.route("/report", methods=["POST"])
def report():
    data = request.json
    reports[data["id"]] = data
    print("📊 REPORT:", data)
    return {"ok": True}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)