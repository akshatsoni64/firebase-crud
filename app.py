from firebase_admin import firestore, credentials, initialize_app

# Initialize the app
cred_obj = credentials.Certificate("cred/cred.json")
myapp = initialize_app(cred_obj)

# Database connection
db = firestore.client()

# Student collection
student = db.collection('student')