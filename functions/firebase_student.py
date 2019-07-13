import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_admin_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def get_name(uid: str) -> dict:
    return db.document('users/{0}'.format(uid)).get().to_dict()


def get_education(uid: str) -> [dict]:
    arr = []
    for doc in db.collection('users/{0}/education'.format(uid)).list_documents():
        arr.append(doc.get().to_dict())

    return arr


def get_experience(uid: str) -> [dict]:
    arr = []
    for doc in db.collection('users/{0}/experience'.format(uid)).list_documents():
        arr.append(doc.get().to_dict())

    return arr


def get_coursework(uid: str) -> [dict]:
    arr = []
    for doc in db.collection('users/{0}/coursework'.format(uid)).list_documents():
        arr.append(doc.get().to_dict())

    return arr
