import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school           
collection = db.students         
iter = collection.find()
for document in iter:
    print document['_id']
    min = 9999999
    posMin = -1
    iter = -1
    for arrayItem in document['scores']:
        iter = iter +1
        if ((arrayItem['type'] == "homework") and (min > arrayItem['score']) ):
            posMin = iter
            min =  arrayItem['score']
    print posMin
    collection.update({'_id': document['_id']}, {'$pull': {'scores': {'score': min}}})
    #collection.update({'_id': document['_id']}, {'$pull': {"scores": "null"}})