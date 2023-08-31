from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__) # creates flask instance
print(__name__) # name is __main__


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name) # anytime we hit the route directory url ending in /<username> it will hit our server

@app.route("/work")
def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=["POST", "GET"]) # get means browser wants us to send info post means browser wants us to send info
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return 'did not save to database'
    else:
        return "somthing went wrong. Try again!"