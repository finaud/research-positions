from firebase_admin import firestore

db = firestore.client()


def get_info(uid: str) -> dict:
    return db.document('users/{0}'.format(uid)).get().to_dict()

