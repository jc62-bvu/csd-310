from pymongo import MongoClient
  
url = ("mongodb+srv://admin:admin@cluster0.8lw7v.mongodb.net/test")
client = MongoClient(url)
  
db = client.pytech
  

collection = db.students
  
student_1 = {
        "first_name":"Thorin",
        "last_name" : "Oakenshield",
        "student_id":1007,
        
        }
student_2 = {
        "first_name":"Bilbo",
        "last_name" : "Baggins",
        "student_id":"1008",
        
        }
student_3 = {
        "first_name" : "Frodo",
        "last_name" : "Baggins",
        "student_id" : "1009",
        }
  
student_1 = collection.insert_one(student_1)
student_2 = collection.insert_one(student_2)
student_3 = collection.insert_one(student_3)
  
print(student_1,student_2,student_3)
  
docs = collection.find_one({student_1})
print(docs)
