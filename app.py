from connection import connect_elasticsearch
# from models import *
from flask import Flask, render_template, request
from flask_babel import _

es = connect_elasticsearch()

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        query = request.form.get('search')
        print(query)

        if query is not None:
            data = es.search(index='profile', query={
                'multi_match': {'query': query, 'fields': ['*']}})
            print(data['hits'])
            return render_template("list.html", query=query, data=data)
    return render_template("index.html")


# @app.route("/profile")
# def profile():
#     return render_template("profile.html")

# @app.route("/index")
# def index():
#     # Opening JSON file
#     f = open('data.json', )

#     # returns JSON object as
#     # a dictionary
#     documents = json.load(f)
#     data = client.index_documents(engine_name, documents)
#     return render_template("about.html", data=data)
