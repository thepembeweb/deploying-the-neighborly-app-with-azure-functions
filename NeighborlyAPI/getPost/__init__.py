import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://cosmosaccount-neighborly-dev:rLOQdnOterGUBp1nx52hDQ3fTYli0Qsx6RKz2uUeyDwcGnHzIQGaJCRPRz5cYzDHB37BDbIZs36E9RrZ8LeUog==@cosmosaccount-neighborly-dev.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosaccount-neighborly-dev@"  # TODO1: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['cosmos-neighborly-dev']
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)