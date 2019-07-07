import firebase_admin
from firebase_admin import credentials, auth, firestore

import json
import requests

from config import FIREBASE_API_KEY as API_KEY

cred = credentials.Certificate("firebase_admin_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def verify_credentials(email: str, password: str) -> dict:
    response = requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + API_KEY,
                             headers={"content-type": "application/json"},
                             data=json.dumps({"email": email, "password": password, "returnSecureToken": True})).json()
    if 'localId' in response:
        return {'status': 'success', 'uid': response['localId'], 'token': response['idToken']}
    elif 'error' in response:
        return {'status': 'success', 'msg': response['error']['message']}
    else:
        return {'status': 'success', 'msg': 'UNKNOWN_ERROR'}


def verify_token(token: str) -> dict:
    try:
        response = auth.verify_id_token(token)
        return {'status': 'success', 'uid': response['uid']}
    except ValueError as e:
        return {'status': 'error', 'msg': e.args[0]}


def create_user(email: str, password: str) -> dict:
    try:
        student = auth.create_user(email=email, password=password)
        return {'status': 'success', 'uid': student.uid}
    except ValueError as e:
        return {'status': 'error', 'msg': e.args[0]}
    except auth.AuthError as e:
        return {'status': 'error', 'msg': json.loads(e.detail.response.text)['error']['message']}
