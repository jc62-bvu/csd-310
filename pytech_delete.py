from pymongo import MongoClient
  
url = ("mongodb+srv://admin:admin@cluster0.8lw7v.mongodb.net/test")
client = MongoClient(url)
  
db = client.pytech  

collection = db.students

doc = db.students.find_one({"student_id": 1009})

delete = db.students.delete_many({"first_name": "Brad"})

docs = db.students.find()

update = db.students.update_one({"student_id": 1007}, {"$set": {"last_name": "Smith"}})

for data in doc:
    print(doc)

