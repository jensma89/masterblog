from flask import Flask, render_template, request
import json as js

app = Flask(__name__)


@app.route("/")
def index():
    with open("blog_storage.json", "r") as file:
        blog_posts = js.load(file)

    return render_template("index.html",
                           posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        pass
    return render_template("add.html")






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)