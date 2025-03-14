# Neotopia Backend Django Server

## Description
A Django web application.

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


3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

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

## License
This project is licensed under the MIT License.

