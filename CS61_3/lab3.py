import pymongo
import urllib.parse
from bson import ObjectId
import json


def get_database():
    f = open (r'URI.json')
    content = json.load(f)
    f.close()

    URI = content["user"] + urllib.parse.quote(content["password"]) + content["server"]
    client = pymongo.MongoClient(URI)
    
    db = client.lab3
    return db

#Assumes every document id equals city zip code and is unique 
def question2(db):
    total = db.zipcodes.count_documents({})
    # total = 0
    # for document in cursor:
    #      total += 1
    print("Question 2: " + str(total))
    return total

def question3(db):
    total = db.zipcodes.count_documents({"state":{"$in":['CT', 'RI', 'MA', 'VT', 'NH', 'ME']}})
    print("Question 3: " + str(total))
    return total


def question4(db):
    cursor = db.zipcodes.aggregate([
        
        {
            "$group": {"_id": {'state': "$state", 'population': '$population'},'total': {"$sum": '$pop'}}
        },

        {
             "$match": {"_id":{'state': 'RI'}}
         }
       
    ])
    for document in cursor:
        print("Question 4: " + str(document))

def question5(db):
    cursor = db.zipcodes.find().sort("pop", 1).limit(5)
    
    for document in cursor:
        print("Question 5: " + str(document))


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
    # Get the database
    db = get_database()
    answer2 = question2(db)
    answer3 = question3(db)
    answer4 = question4(db)
    answer5 = question5(db)
    # answer6 = question6(db)


    
