import firebase_admin
from firebase_admin import credentials, db
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS"))
    firebase_admin.initialize_app(cred, {
        "databaseURL": os.getenv("FIREBASE_DATABASE_URL")
    })

# Reference to the Firebase database
firebase_ref = db.reference("/")

# User CRUD operations


def get_user(request, uid):
    ref = db.reference(f'users/{uid}')
    user = ref.get()
    return JsonResponse(user or {}, safe=False)


def get_all_users(request):
    ref = db.reference('users')
    users = ref.get()
    return JsonResponse(users or {}, safe=False)


@csrf_exempt
def create_user(request):
    data = json.loads(request.body)
    uid = data.get('uid')
    if not uid:
        return JsonResponse({'error': 'UID is required'}, status=400)
    ref = db.reference(f'users/{uid}')
    if ref.get() is not None:
        return JsonResponse({'error': 'User already exists'}, status=400)
    ref.set({'name': data.get('name', ''),
            'subscribed_notes': data.get('subscribed_notes', [])})
    return JsonResponse({'message': 'User created successfully'})


@csrf_exempt
def update_user(request, uid):
    data = json.loads(request.body)
    ref = db.reference(f'users/{uid}')
    ref.update(data)
    return JsonResponse({'message': 'User updated successfully'})


@csrf_exempt
def delete_user(request, uid):
    ref = db.reference(f'users/{uid}')
    ref.delete()
    return JsonResponse({'message': 'User deleted successfully'})

# Note CRUD operations


def get_note(request, note_id):
    ref = db.reference(f'notes/{note_id}')
    note = ref.get()
    return JsonResponse(note or {}, safe=False)


def get_all_notes(request):
    ref = db.reference('notes')
    notes = ref.get()
    return JsonResponse(notes or {}, safe=False)


@csrf_exempt
def create_note(request):
    data = json.loads(request.body)
    note_id = data.get('note_id')
    if not note_id:
        return JsonResponse({'error': 'Note ID is required'}, status=400)
    ref = db.reference(f'notes/{note_id}')
    if ref.get() is not None:
        return JsonResponse({'error': 'Note already exists'}, status=400)
    ref.set({'small_notes': data.get('small_notes', {})})
    return JsonResponse({'message': 'Note created successfully'})


@csrf_exempt
def update_note(request, note_id):
    data = json.loads(request.body)
    ref = db.reference(f'notes/{note_id}')
    ref.update(data)
    return JsonResponse({'message': 'Note updated successfully'})


@csrf_exempt
def delete_note(request, note_id):
    ref = db.reference(f'notes/{note_id}')
    ref.delete()
    return JsonResponse({'message': 'Note deleted successfully'})
