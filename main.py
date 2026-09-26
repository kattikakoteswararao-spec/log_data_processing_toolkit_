from fastapi import FastAPI

from toolkit.csv_processor import read_csv
from toolkit.json_processor import read_json
from toolkit.txt_processor import read_txt
from toolkit.data_utils import (
    get_names,
    get_adult_users,
    create_user_lookup,
    user_generator,
)
from toolkit.user_models import User, UserStatus
from toolkit.data_validator import validate_user
from toolkit.exceptions import InvalidUserError
from toolkit.decorators import log_execution
from toolkit.file_manager import FileManager


app = FastAPI(title="Log_Data_Processind_Toolkit_")


# Read CSV
csv_file = "sample_data/users.csv"
users_csv = read_csv(csv_file)

# API
@app.get("/users")
def get_users():
    return {
        "count": len(users_csv),
        "users": users_csv
    }

@app.get("/users/count")
def get_users_count():
    return {
        "count": len(users_csv)
    }

@app.get("/users/names")
def get_user_names():
    return {
        "names": get_names(users_csv)
    }
    
  
@app.get("/users/adults")
def get_adult_users_api():
    return {
        "adult_users": get_adult_users(users_csv)
    }

@app.get("/users/lookup/{name}")
def lookup_user(name: str):
    user_lookup = create_user_lookup(users_csv)

    if name not in user_lookup:
        return {
            "message": "User not found"
        }

    return user_lookup[name]


@app.get("/users/generator")
def generate_users():
    users = []

    for user in user_generator(users_csv):
        users.append(user)

    return {
        "count": len(users),
        "users": users
    }
    

@app.get("/users/validate/{user_id}")
def validate_user_api(user_id: str):

    for user in users_csv:
        if user["id"] == user_id:

            try:
                validate_user(user)

                return {
                    "valid": True,
                    "message": "User is valid",
                    "user": user
                }

            except InvalidUserError as e:
                return {
                    "valid": False,
                    "message": str(e),
                    "user": user
                }

    return {
        "valid": False,
        "message": "User not found"
    }


@app.get("/file")
def read_file():
    file_path = "sample_data/sample.txt"

    with FileManager(file_path, "r") as file:
        content = file.read()

    return {
        "file": file_path,
        "content": content
    }
    
                
    
print("CSV Users:")
print(users_csv)


# Read JSON
json_file = "sample_data/users.json"
users_json = read_json(json_file)

print("\nJSON Users:")
print(users_json)

# Read TXT
txt_file = "sample_data/sample.txt"
lines = read_txt(txt_file)

print("\nTXT Data:")
for line in lines:
    print(line)
    
    # Data processing
names = get_names(users_csv)

print("\nUser Names:")
print(names)


adult_users = get_adult_users(users_csv)

print("\nUsers age 30 or above:")
print(adult_users)


user_lookup = create_user_lookup(users_csv)

print("\nUser Lookup:")
print(user_lookup)


print("\nUsers using Generator:")
for user in user_generator(users_csv):
    print(user)
    
print("\nDataclass User:")    
    
user=User(
    id=1,name="koti",
    email="koti@gmail.com",
    age=31
)    
print(user)
print("Status:", user.status.value)

print("\nUser Validation:") 
   
try:
    validate_user({
        "name": "koti",
        "email": "koti@gmail.com",
        "age": 31
     })
    
    print ("User is valid")
except InvalidUserError as e:
    print("Validation error:",e)    
    
@log_execution
def process_users(users):
    return len(users)


print("\nDecorator Test:")

count = process_users(users_csv)

print("Number of users:", count)

print("\nContext Manager Test:")

file_path = "sample_data/sample.txt"

with FileManager(file_path, "r") as file:
    content = file.read()
    print(content)