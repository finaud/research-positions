from firebase_admin import firestore
from google.cloud.firestore_v1 import ArrayUnion, ArrayRemove

db = firestore.client()


def get_info(uid: str) -> dict:
    return db.document('users/{0}'.format(uid)).get().to_dict()


def set_about(uid: str, data: str) -> None:
    db.document('users/{0}'.format(uid)).update({'about': data})


def add_experience(uid: str, data: dict) -> None:
    db.document('users/{0}'.format(uid)).update({'experience': ArrayUnion([data])})


def remove_experience(uid: str, data: dict) -> None:
    db.document('users/{0}'.format(uid)).update({'experience': ArrayRemove([data])})


def add_education(uid: str, data: dict) -> None:
    db.document('users/{0}'.format(uid)).update({'education': ArrayUnion([data])})


def remove_education(uid: str, data: dict) -> None:
    db.document('users/{0}'.format(uid)).update({'education': ArrayRemove([data])})


def add_coursework(uid: str, data: dict) -> None:
    db.document('users/{0}'.format(uid)).update({'coursework': ArrayUnion([data])})


def remove_coursework(uid: str, data: dict) -> None:
    db.document('users/{0}'.format(uid)).update({'coursework': ArrayRemove([data])})
