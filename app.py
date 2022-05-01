from connection import connect_elasticsearch
# from models import *
from flask import Flask, render_template, request
from flask_babel import _

es = connect_elasticsearch()

app = Flask(__name__)


@app.route('/')
@app.route("/index.html", methods=['GET', 'POST'])
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


if __name__ == "__main__":
    app.run(debug=True)

#     # initialize using environment variables


# apm = ElasticAPM(app)

# app.config['ELASTIC_APM'] = {
#     # Set the required service name. Allowed characters:
#     # a-z, A-Z, 0-9, -, _, and space
#     'SERVICE_NAME': 'test',

#     # Use if APM Server requires a secret token
#     'SECRET_TOKEN': 'FEXJW2IoBcN5o1fdmMm4cLWA',

#     # Set the custom APM Server URL (default: http://localhost:8200)
#     'SERVER_URL': 'https://64f5528e99b64681983dfa057f6fa368.apm.us-central1.gcp.cloud.es.io:443',

#     # Set the service environment
#     'ENVIRONMENT': 'production',
# }

# apm = ElasticAPM(app)
