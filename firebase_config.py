import os
import firebase_admin
from firebase_admin import credentials, db

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Firebase credentials and database URL from .env
FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL")

if not FIREBASE_CREDENTIALS:
    raise ValueError("FIREBASE_CREDENTIALS is not set in the .env file.")
if not FIREBASE_DATABASE_URL:
    raise ValueError("FIREBASE_DATABASE_URL is not set in the .env file.")

# Initialize Firebase app only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred, {
        'databaseURL': FIREBASE_DATABASE_URL
    })

# Firebase database reference


def get_database():
    return db.reference("/")
