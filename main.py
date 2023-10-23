from flask import Flask, render_template
import requests

BLOGS_API = "https://api.npoint.io/78c651803da57909e433"


# print(all_content)

app = Flask(__name__)

@app.route("/")
def home_page():
    all_content = requests.get(BLOGS_API).json()
    return render_template("index.html", all_content=all_content)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def get_post(id):
    all_content = requests.get(BLOGS_API).json()
    picked_post = all_content[id - 1]
    return render_template("post.html", post=picked_post)


if __name__ == "__main__":
    app.run(debug=True)