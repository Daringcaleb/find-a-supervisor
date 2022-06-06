from elasticsearch import Elasticsearch




def connect_elasticsearch():

    # _es = None
    try:
        _es = None
        _es = Elasticsearch(cloud_id="test:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDY2ZTg1MDE4NGQ1ZDQwZTJhYzRlNjJmNTE4MzE5YmNkJGI4YWY4ZjJlYWU4NDRjOGY5MzhhYzE3MzhhY2Q2YWE1",
                            basic_auth=("elastic", "2ycWZCoHaEESN5xvl7GhHzUP"), verify_certs=False, request_timeout=100)

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
