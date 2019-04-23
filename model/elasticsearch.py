import os
import warnings
from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch_dsl import Search
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class ElasticSearchDB:
    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        awsauth = AWS4Auth(
            os.getenv("AWS_ACCESS_KEY"),
            os.getenv("AWS_SECRET_KEY"),
            os.getenv("AWS_REGION"),
            os.getenv("AWS_SERVICE"))
        
        es = Elasticsearch(
            hosts=[{"host": os.getenv("ELASTICSEARCH_HOST").replace("https://", ""), "port": int(os.getenv("ELASTICSEARCH_PORT"))}],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
            )

        return es
    
    def scan(self, index):
        s = Search(using=self.connection, index=index)
        s = s.params(size=10000)
        return s.scan()

    def count(self, index):
        s = Search(using=self.connection, index=index)
        return s.count()
