from firebase_admin import firestore

db = firestore.client()


def get_info(uid: str) -> dict:
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


def add_education(uid: str, data: dict) -> None:
    db.collection('users/{0}/education'.format(uid)).add(data)


def add_experience(uid: str, data: dict) -> None:
    db.collection('users/{0}/experience'.format(uid)).add(data)


def set_coursework(uid: str, data: [dict]) -> None:
    for doc in db.collection('users/{0}/coursework'.format(uid)).list_documents():
        doc.delete()

    for course in data:
        db.collection('users/{0}/coursework'.format(uid)).add(course)