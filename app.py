from flask import Flask, redirect, url_for, render_template, request
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import csv


class Shoe:
    def __init__(self, name, price,link):
        self.name = name
        self.price = price
        self.link = link

app = Flask(__name__)

#Landing page
@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("result"))
    else:
        return render_template("index.html")

#User searches for shoe name
@app.route("/results", methods=["POST","GET"])
def result():
    if request.method == "POST":
        shoe_name = request.form["sn"]
        return redirect(url_for("display_results",result=shoe_name))
    else:
        return render_template("results.html")

#Results of users search
@app.route("/<result>",methods=["POST","GET"])
def display_results(result):
    if request.method == "POST":
        return redirect(url_for("result"))
    else:
        csv_file = csv.reader(open("products.csv", "r"), delimiter=",")
        list = []
        for row in csv_file:
            if result.lower() == row[0].lower():
                new_shoe = Shoe(row[0], row[1],row[2])
                list.append(new_shoe)
        return render_template("data.html", data=list)

if __name__ == "__main__":
    app.run(debug=False)
