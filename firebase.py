import firebase_admin
from firebase_admin import credentials, auth, firestore

import json
import requests

from config import FIREBASE_API_KEY as api_key

cred = credentials.Certificate("firebase_admin_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def verify_user(email: str, password: str) -> dict:
    return requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + api_key,
                         headers={"content-type": "application/json"},
                         data=json.dumps({"email": email, "password": password, "returnSecureToken": True})
                         ).json()


def verify_token(token: str) -> dict:
    return auth.verify_id_token(token)
