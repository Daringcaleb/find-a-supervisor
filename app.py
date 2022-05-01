from urllib import response

from numpy import require
from connection import connect_elasticsearch
from models import *
from flask import Flask, render_template, redirect, url_for, request, g, current_app
from flask_babel import _, get_locale
from elasticsearch import Elasticsearch
from elasticapm.contrib.flask import ElasticAPM
# or configure to use ELASTIC_APM in your application's settings
from elasticapm.contrib.flask import ElasticAPM


es = connect_elasticsearch()

# const_url = "https://researchers.wlv.ac.uk/"

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


if __name__ == "__main__":
    app.run(port=5005, debug=True, host="0.0.0.0")

    # initialize using environment variables


apm = ElasticAPM(app)

app.config['ELASTIC_APM'] = {
    # Set the required service name. Allowed characters:
    # a-z, A-Z, 0-9, -, _, and space
    'SERVICE_NAME': 'test',

    # Use if APM Server requires a secret token
    'SECRET_TOKEN': 'FEXJW2IoBcN5o1fdmMm4cLWA',

    # Set the custom APM Server URL (default: http://localhost:8200)
    'SERVER_URL': 'https://64f5528e99b64681983dfa057f6fa368.apm.us-central1.gcp.cloud.es.io:443',

    # Set the service environment
    'ENVIRONMENT': 'production',
}

apm = ElasticAPM(app)
