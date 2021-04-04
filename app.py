from firebase_admin import firestore, credentials, initialize_app

# Initialize the app
# GET YOU CRED FILE FROM SERVICE ACCOUNTS INSIDE YOUR FIREBASE DB PROJECT'S CONSOLE
cred_obj = credentials.Certificate("cred/cred.json")
myapp = initialize_app(cred_obj)

# Database connection
db = firestore.client()

# Student collection
student = db.collection('student')