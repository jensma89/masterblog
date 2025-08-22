"""
app.py

A little web-application to add, update, delete,
like and dislike blogs.
"""

import json as js
from flask import (Flask,
                   render_template,
                   request, redirect,
                   url_for)

app = Flask(__name__)


@app.route("/")
def index():
    """Load and show the root page."""
    with open("blog_storage.json", "r") as file:
        blog_posts = js.load(file)

    return render_template("index.html",
                           posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Load the page to add a new post and save it."""
    if request.method == "POST":

        try:
            with open("blog_storage.json", "r") as file:
                blog_posts = js.load(file)
        except FileNotFoundError:
            print("File not found")
            blog_posts = []

        # Create the new entry in the dictionary
        new_post = {
            "id": len(blog_posts) + 1,
            "title": request.form.get("title", "Untitled"),
            "author": request.form.get("author", "Anonymous"),
            "content": request.form.get("content", ""),
            "likes": 0,
            "dislikes": 0
        }

        blog_posts.append(new_post)

        with open("blog_storage.json", "w") as file:
            js.dump(blog_posts, file, indent=4)

        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/delete/<int:post_id>", methods=["GET", "POST"])
def delete(post_id):
    """Delete a post via button or URL.
    And remove it from dictionary"""
    try:
        with open("blog_storage.json", "r") as file:
            blog_posts = js.load(file)
    except FileNotFoundError:
        print("File not found")
        blog_posts = []

    # Check for the right id
    blog_posts = [post for post in blog_posts
                  if post["id"] != post_id]

    with open("blog_storage.json", "w") as file:
        js.dump(blog_posts, file, indent=4)

    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Edit a post via an html form."""
    try:
        with open("blog_storage.json", "r") as file:
            blog_posts = js.load(file)
    except FileNotFoundError:
        print("File not found")
        blog_posts = []

    # Check for existing post
    post = next((p for p in blog_posts
                 if p["id"] == post_id), None)
    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        post["title"] = request.form.get("title",
                                         post["title"])
        post["author"] = request.form.get("author",
                                          post["author"])
        post["content"] = request.form.get("content",
                                           post["content"])

        with open("blog_storage.json", "w") as file:
            js.dump(blog_posts, file, indent=4)

        return redirect(url_for("index"))

    return render_template("update.html", post=post)


@app.route("/like/<int:post_id>", methods=["POST"])
def like(post_id):
    """Add a like to the blog
    and increase the count to show."""
    try:
        with open("blog_storage.json", "r") as file:
            blog_posts = js.load(file)
    except FileNotFoundError:
        print("File not found")
        blog_posts = []

    # Increment by click
    for post in blog_posts:
        if post["id"] == post_id:
            post["likes"] += 1
            break

    with open("blog_storage.json", "w") as file:
        js.dump(blog_posts, file, indent=4)

    return redirect(url_for("index"))


@app.route("/dislike/<int:post_id>", methods=["POST"])
def dislike(post_id):
    """Add a dislike to the blog
    and increase the count to show."""
    try:
        with open("blog_storage.json", "r") as file:
            blog_posts = js.load(file)
    except FileNotFoundError:
        print("File not found")
        blog_posts = []

    # Increment by click
    for post in blog_posts:
        if post["id"] == post_id:
            post["dislikes"] += 1
            break

    with open("blog_storage.json", "w") as file:
        js.dump(blog_posts, file, indent=4)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
