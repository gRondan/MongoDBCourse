import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grade = db.grades
query = {}
result = grade.find(query)
result.sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])
flag = -1
for doc in result:
    if doc["student_id"] != flag:
        print doc["student_id"]
        grade.delete_many({"_id":doc["_id"]})
        flag = doc["student_id"]
