from flask import Flask

#建立Flask應用
app = Flask(__name__)

@app.route("/")
def home():
    return "Easysplit (Python) is running!"

if __name__ == "__main__":
    app.run(debug=True, host ="127.0.0.1", port = 5000)


@app.get("/api/health")
def health():
    return jsonify(status="ok")

@app.get("/api/hello")
def hello():
    return jsonify(message="Hello from Flask", ok=True)