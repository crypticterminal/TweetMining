import pymongo

def mongo():
  client=pymongo.MongoClient()
  db=client['db']
  tweets=db['tweets']
