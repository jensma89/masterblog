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

        try:
            with open("blog_storage.json", "r") as file:
                blog_posts = js.load(file)
        except FileNotFoundError:
            print("File not found")
            blog_posts = []

        new_post = {
            "id": len(blog_posts) + 1,
            "title": request.form.get("title", "Untitled"),
            "author": request.form.get("author", "Anonymous"),
            "content": request.form.get("content", "")
        }

        blog_posts.append(new_post)

        with open("blog_storage.json", "w") as file:
            js.dump(blog_posts, file, indent=4)

        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/delete/<int:post_id>", methods=["GET", "POST"])
def delete(post_id):
    try:
        with open("blog_storage.json", "r") as file:
            blog_posts = js.load(file)
    except FileNotFoundError:
        print("File not found")
        blog_posts = []

    blog_posts = [post for post in blog_posts
                  if post["id"] != post_id]

    with open("blog_storage.json", "w") as file:
        js.dump(blog_posts, file, indent=4)

    return redirect(url_for("index"))






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
