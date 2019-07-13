import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_admin_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def get_name(uid: str):
    return db.document('users/{0}'.format(uid)).get().to_dict()


def get_coursework(uid: str):
    arr = []
    for course in db.collection('users/{0}/coursework'.format(uid)).list_documents():
        arr.append(course.get().to_dict())

    return arr
