from pymongo import MongoClient
  
url = ("mongodb+srv://admin:admin@cluster0.8lw7v.mongodb.net/test")
client = MongoClient(url)
  
db = client.pytech  

collection = db.students

doc = db.students.find()

for data in doc:
    print(data)

