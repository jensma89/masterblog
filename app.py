import json as js
from flask import (Flask,
                   render_template,
                   request, redirect,
                   url_for)

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
        new_post = {
            "title": request.form["title"],
            "author": request.form["author"],
            "content": request.form["content"]
        }

        try:
            with open("blog_storage.json", "r") as file:
                blog_posts = js.load(file)
        except FileNotFoundError:
            blog_posts = []

        blog_posts.append(new_post)

        with open("blog_storage.json", "w") as file:
            js.dump(blog_posts, file, indent=4)

        return redirect(url_for("index"))
    return render_template("add.html")








if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)