import os
from flask import Flask, jsonify

# 建立 Flask 應用
app = Flask(__name__)

# 從環境變數讀取 SECRET_KEY，沒有就用 dev-secret
SECRET_KEY = os.getenv("SECRET_KEY", "my-secret-09081111")
app.config["SECRET_KEY"] = SECRET_KEY

@app.route("/")
def home():
    return f"Easysplit (Python) is running! SECRET_KEY = {SECRET_KEY}"

@app.get("/api/health")
def health():
    return jsonify(status="ok")

@app.get("/api/hello")
def hello():
    return jsonify(message="Hello from Flask", ok=True)

# ⚠️ 本地開發才需要這一段，上線 Render 時可以註解掉

#if __name__ == "__main__":
#    app.run(debug=True, host="127.0.0.1", port=5000)

from sqlalchemy import create_engine, text
import os

engine = create_engine(os.getenv("DATABASE_URL"))

@app.get("/api/dbtest")
def dbtest():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT now()")).scalar()
        return {"time": str(result)}