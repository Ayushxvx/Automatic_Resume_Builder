from flask import Flask , request , render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def make_resume():
    if request.method == "POST":
    url = request.form.get("url")
    response = requests.get(url)
    soup = BeautifulSoup(response,'html.parser')