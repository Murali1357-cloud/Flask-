from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["userflask"]
stud_col = db["stud"]

# Add student

@app.route("/addstud" , methods=["POST"])
def add_student():
       try:
            data = request.get_json()
            stud_col.insert_one(data)
            return jsonify({"message":"Student details added successfully"})
       except:
            return jsonify({"message": "Something went wrong"})

# Get student

@app.route("/getstud" , methods=["GET"])
def getstudent():
    page = int(request.args.get("page",1))
    limit = int(request.args.get("limit",2))
    skip = (page - 1)*limit
    data = list(stud_col.find({},{"_id":0}).skip(skip).limit(limit))
    return jsonify({"page":page,"limit":limit,"items":data})
    '''
     try:
          allstud = list(stud_col.find({},{"_id":0}))
          return jsonify(allstud)   
     except:
          return jsonify({"message": "Something went wrong"})
'''
# Update student 

@app.route("/updatestud/<string:_id>", methods=["PUT"])
def updatestudent(_id):
     try:
           oid = ObjectId(_id)
           data = request.get_json()
           result = stud_col.update_one({"_id":oid},{"$set":data})
           return jsonify ({"message": "Updated user"})
     except:
          return jsonify({"message": "Something went wrong"})
   

# Delete student 

@app.route("/deletestud/<string:_id>", methods=["DELETE"])
def deletestudent(_id):
     try:
          oid = ObjectId(_id)
          stud_col.delete_one({"_id":oid})
          return jsonify ({"message": "User deleted"})
     except:
          return jsonify({"message": "Something went wrong"})

# Task
'''
@app.route("/addstud", methods=["POST"])
def add_student():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid JSON data"})

    email = data.get("email", "").strip().lower()
    phone = data.get("phone", "").strip()
    password = data.get("password", "").strip()

    if not email or not phone or not password:
        return jsonify({"message": "Email, phone, and password are required"})

    existing_user = stud_col.find_one({ "$or": [{"email": email},{"phone": phone}]})

    if existing_user:
        return jsonify({"message": "User already found"})
    else:
        stud_col.insert_one({
            "email": email,
            "phone": phone,
            "password": password
        })
        return jsonify({"message": "User not found — New student added successfully"})

'''
if __name__ == "__main__":
  app.run(debug=True)    