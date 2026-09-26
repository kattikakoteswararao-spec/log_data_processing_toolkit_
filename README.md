# Log & Data Processing Toolkit

A modular Python toolkit for reading, validating, processing, and managing user data from CSV, JSON, and TXT files.

## Features

Read CSV files
Read JSON files
Read TXT files
Process user data
Validate user information
Generate users using generators
Use list and dictionary comprehensions
Use dataclasses and enums
Custom exception handling
Execution-time logging using decorators
Safe file handling using context managers
Unit testing using unittest
REST APIs using FastAPI

## Project Structure

textlog_data_processing_toolkit/
│
├── sample_data/
│   ├── sample.txt
│   ├── users.csv
│   └── users.json
│
├── tests/
│   ├── __init__.py
│   └── test_toolkit.py
│
├── toolkit/
│   ├── __init__.py
│   ├── csv_processor.py
│   ├── data_utils.py
│   ├── data_validator.py
│   ├── decorators.py
│   ├── exceptions.py
│   ├── file_manager.py
│   ├── json_processor.py
│   ├── txt_processor.py
│   └── user_models.py
│
├── main.py
├── DESIGN_NOTE.md
└── README.md

Requirements:

Python 3.10 or higher is recommended.

Install the required packages:
pip install fastapi uvicorn

Running the Application

Activate the virtual environment.

Windows PowerShell
.\venv\Scripts\Activate.ps1

Run the FastAPI application:
uvicorn main:app --reload

The application will start at:
http://127.0.0.1:8000

FastAPI Documentation

FastAPI provides interactive API documentation.

Open:
http://127.0.0.1:8000/docs

Available APIs

## 1. Get Users

Endpoint:
GET /users

Example:
http://127.0.0.1:8000/users

Example response:

{
    "count": 4,
    "users": [
        {
            "id": "1",
            "name": "Koti",
            "email": "koti@gmail.com",
            "age": "31"
        },
        {
            "id": "2",
            "name": "Ravi",
            "email": "ravi@gmail.com",
            "age": "28"
        },
        {
            "id": "3",
            "name": "Siri",
            "email": "siri@gmail.com",
            "age": "30"
        },
        {
            "id": "4",
            "name": "John",
            "email": "john@gmail.com",
            "age": "35"
        }
    ]
}

## 2. Get User Count

Endpoint:
GET /users/count

Example:
http://127.0.0.1:8000/users/count

Responce:

{
    "count": 4
}

## 3. Get User Names

Endpoint:
GET /users/names
Example:
http://127.0.0.1:8000/users/names

Response:

{
    "names": [
        "Koti",
        "Ravi",
        "Siri",
        "John"
    ]
}

## 4. Generate Users

Endpoint:
GET /users/generator

Example:
http://127.0.0.1:8000/users/generator

{
    "count": 4,
    "users": [
        {
            "id": "1",
            "name": "Koti",
            "email": "koti@gmail.com",
            "age": "31"
        },
        {
            "id": "2",
            "name": "Ravi",
            "email": "ravi@gmail.com",
            "age": "28"
        },
        {
            "id": "3",
            "name": "Siri",
            "email": "siri@gmail.com",
            "age": "30"
        },
        {
            "id": "4",
            "name": "John",
            "email": "john@gmail.com",
            "age": "35"
        }
    ]
}

Running Unit Tests

Run the tests using:
python -m unittest discover -s tests -v

Expected result

Ran 4 tests

OK

Data Validation

The toolkit validates user information before processing.

Example:

user = {
    "name": "Test",
    "email": "test@gmail.com",
    "age": 15
}

If the user does not satisfy the validation rules, the application raises:
InvalidUserError

Example: List Comprehension

names = [user["name"] for user in users]

This creates a list containing the names of all users.

Example: Dictionary Comprehension

user_ages = {
    user["name"]: user["age"]
    for user in users
} user_ages = {
    user["name"]: user["age"]
    for user in users
}

This creates a dictionary containing each user’s name and age.

Example: Generator

def user_generator(users):
    for user in users:
        yield user

Generators return users one at a time and can help reduce memory usage when processing large collections.

Example: Lambda

get_age = lambda user: user["age"]

age = get_age({
    "name": "Koti",
    "age": 31
})

print(age)
output:31 

## Testing

The project contains unit tests for:

Valid users
Missing user fields
Underage users
User validation

Run:
python -m unittest discover -s tests -v

Git

Initialize the repository:
git init

Check the files:
git status

Add the project files:
git add .

Commit the changes:

git commit -m "Complete Week 1 Log Data Processing Toolkit"





