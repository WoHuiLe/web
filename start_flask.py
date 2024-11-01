#!/usr/bin/env python3

from flask import Flask, send_from_directory, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder="frontend/dist", static_folder="frontend/dist/assets")
CORS(app)  # 允许所有跨源请求

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1113, debug=True)
