import json
from elasticsearch import Elasticsearch, helpers
import configparser




def connect_elasticsearch():

    # _es = None
    try:
        _es = None
        _es = Elasticsearch(cloud_id="test:ZWFzdHVzMi5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJDk1NjgxMjUzZDJiYzQ4ZTNiNWFjNzZjMDdlNDliZGY4JDI5YWEyOGQxZTA0MDQxYjJhNzcwNGE5NjZkYzQxZWUw",
                            basic_auth=("elastic", "r3iheQwoQR5JEl4kQ1pEcmv3"), verify_certs=False, request_timeout=100)

        if _es.info():
            print('Connected')
    except Exception as ex:
        print('Not connected!!!!')
        print(str(ex))
    return _es


connect_elasticsearch()


# def load_data():
#     es = connect_elasticsearch()
#     j = open('data.json', 'r', encoding='utf-8')
#     nodes = json.load(j)

#     for node in nodes:
#         es.index(index='profile', document=node)


# load_data()
