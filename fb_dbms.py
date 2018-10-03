import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("xpend-5acc1-firebase-adminsdk-qb7eh-92a96ef78c.json")
firebase_admin.initialize_app(cred)