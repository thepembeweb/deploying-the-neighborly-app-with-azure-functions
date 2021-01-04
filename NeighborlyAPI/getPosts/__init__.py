import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://cosmosaccount-neighborly-dev:rLOQdnOterGUBp1nx52hDQ3fTYli0Qsx6RKz2uUeyDwcGnHzIQGaJCRPRz5cYzDHB37BDbIZs36E9RrZ8LeUog==@cosmosaccount-neighborly-dev.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosaccount-neighborly-dev@"  # TODO1: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['cosmos-neighborly-dev']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)