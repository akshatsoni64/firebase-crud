import firebase_admin
from firebase_admin import firestore, credentials

cred_obj = credentials.Certificate("cred/cred.json")
app = firebase_admin.initialize_app(cred_obj)

db = firestore.client()
# print(db)

co = db.collection('student')
data = {
    "name": "Name 1",
    "eno": "1201"
}
co.add(data)