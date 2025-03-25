# Neotopia Backend Django Server

## Description

This is Neotopia Django backend server

###

## Installation

### Prerequisites

- Python (recommended: latest version, managed with [pyenv](https://github.com/pyenv/pyenv))
- Virtual environment tool (e.g., `venv` or `virtualenv`)
- Git

### Steps

1. **Clone the Repository**

   ```bash
   git clone git@github.com:neotopia-app/server.git
   cd server
   ```

2. **Set Up a Virtual Environment**

   ### Configure VS Code to Use the Virtual Environment

   1. Open **VS Code**.
   2. Open the **Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac).
   3. Search for **"Python: Select Interpreter"** and select it.
   4. You should see an option like:

      ```bash
      ./venv/bin/python  # macOS/Linux
      venv\Scripts\python  # Windows
      ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Get Firebase service account
   Create a `.env` file in the root directory with the following variables:

   - FIREBASE_DATABASE_URL
   - FIREBASE_CREDENTIALS

## Running the Server

1. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

2. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## Running Tests

```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

# Firebase Realtime Database API Doucmentation - Django

This API provides CRUD operations for managing users and notes stored in Firebase Realtime Database.

## Base URL

```ts
// For Testing:
base-url: http://127.0.0.1 
http://<base-url>/apis/
```

## Users Endpoints

### Get All Users

**GET** `/apis/users/get`

**Response:**

```json
{
  "UID_1": {
    "name": "John Doe",
    "subscribed_notes": ["noteId_1", "noteId_2"]
  },
  "UID_2": {
    "name": "Jane Doe",
    "subscribed_notes": ["noteId_1"]
  }
}
```

### Get User by UID

**GET** `/apis/users/get/<uid>`

**Response:**

```json
{
  "name": "John Doe",
  "subscribed_notes": ["noteId_1", "noteId_2"]
}
```

### Create User

**POST** `/apis/users/create`

**Request Body:**

```json
{
  "uid": "UID_3",
  "name": "Alice Smith",
  "subscribed_notes": ["noteId_3"]
}
```

**Response:**

```json
{
  "message": "User created successfully"
}
```

### Update User

**PATCH** `/apis/users/update/<uid>`

**Request Body:**

```json
{
  "name": "Alice Johnson"
}
```

**Response:**

```json
{
  "message": "User updated successfully"
}
```

### Delete User

**DELETE** `/apis/users/delete/<uid>`

**Response:**

```json
{
  "message": "User deleted successfully"
}
```

## Notes Endpoints

### Get All Notes

**GET** `/apis/notes/get`

**Response:**

```json
{
  "noteId_1": {
    "small_notes": {
      "smallNote_1": {
        "orderId": 1,
        "noteBody": "This is a small note inside noteId_1.",
        "completed": false
      }
    }
  }
}
```

### Get Note by ID

**GET** `/apis/notes/get/<note_id>`

**Response:**

```json
{
  "small_notes": {
    "smallNote_1": {
      "orderId": 1,
      "noteBody": "This is a small note inside noteId_1.",
      "completed": false
    }
  }
}
```

### Create Note

**POST** `/apis/notes/create`

**Request Body:**

```json
{
  "note_id": "noteId_3",
  "small_notes": {
    "smallNote_5": {
      "orderId": 1,
      "noteBody": "A new note",
      "completed": false
    }
  }
}
```

**Response:**

```json
{
  "message": "Note created successfully"
}
```

### Update Note

**PATCH** `/apis/notes/update/<note_id>`

**Request Body:**

```json
{
  "small_notes": {
    "smallNote_5": {
      "orderId": 1,
      "noteBody": "Updated note content",
      "completed": true
    }
  }
}
```

**Response:**

```json
{
  "message": "Note updated successfully"
}
```

### Delete Note

**DELETE** `/apis/notes/delete/<note_id>`

**Response:**

```json
{
  "message": "Note deleted successfully"
}
```

## Notes

- All request bodies should be sent as JSON.
- Ensure the Firebase database is correctly initialized before making API requests.
- Use valid UIDs and note IDs to perform CRUD operations.

This README provides the necessary API documentation for testing endpoints in Postman or any API client.

## License

This project is licensed under the MIT License.
