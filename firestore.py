import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("firebase_admin_key.json")
firebase_admin.initialize_app(cred)

db = firebase_admin.firestore.client()
