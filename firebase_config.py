import firebase_admin
from firebase_admin import credentials, db
import os

# Path to your Firebase service account key JSON file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
firebase_cred_path = os.path.join(BASE_DIR, 'firebase-adminsdk.json')

# Initialize the Firebase app only if it hasn’t been initialized already
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_cred_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://your-database-name.firebaseio.com/'
    })
