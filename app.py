import flask
from flask import Flask,  request,jsonify
from amazonscrapper import url_for_product


app = Flask(__name__)

@app.route("/")
def index():
    url = request.args.get("url")
    if url:
        data = url_for_product(url)
        return jsonify(data)
    else:
        return jsonify({"error": "No URL provided"})
    

if __name__ == "__main__":
    app.run(debug=True)

