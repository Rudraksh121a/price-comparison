import flask
from flask import Flask,  request,jsonify
from amazonscrapper import url_for_product
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    productname = request.args.get("productname")
    if productname:
        data = url_for_product(productname)
        return jsonify(data)
    else:
        return jsonify({"error": "No URL provided"})

@app.route("/get_product_details")
def getproductdetails():
    pass

@app.route("/get_product_reviews")
def todaytrending():
    pass


@app.route("/todaydeals")
def todaydeals():
    pass

if __name__ == "__main__":
    app.run(debug=True,port=5000,host="0.0.0.0")

