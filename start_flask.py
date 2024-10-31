# #!/usr/bin/env python3
# import flask

# app = flask.Flask(__name__,
#                   template_folder="web-app",
#                   static_folder="web-app/assets")

# @app.route("/")
# def index():
#     return flask.render_template("index.html")

# if __name__ == "__main__":
#     print("启动 Flask 应用...")
#     app.run(host="0.0.0.0", port=1111, debug=True)

from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='dist')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=1111, debug=True)
