from Database.notes_db_handler  import UserHandler
from fastapi.middleware.cors    import CORSMiddleware
from Schema.notes_data_model    import UserDataModel
from starlette.responses        import Response
from datetime                   import datetime
from fastapi                    import FastAPI
import hashlib
import pyotp


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def get_current_time():
    return datetime.now()

def get_secret_key():
    return pyotp.random_base32()

user_handler = UserHandler()

app = FastAPI(title="Notes API", description="API for notes", version="23.04.17")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])

# REGISTER USER
@app.post("/api/users")
async def add_user(data: UserDataModel):
    user_handler.add(
        username=data.UserName,
        lastname=data.LastName,
        password=hash_password(data.Password),
        email=data.EmailAddress,
        date=get_current_time(),
        secret_key=get_secret_key(),
        status=True
    )

# SHOW ALL USERS
@app.get("/api/users")
async def get_all_users():
    return user_handler.get_all()

# DIACTIVATE USER ACCOUNT
@app.put("/api/users/{id}/diactivate")
async def diactivate_user(id: int):
    user_handler.diactivate(id)

# Reset password:
@app.put("/api/users/{id}/reset_password")
async def update_user(id: int, password: str):
    user_handler.update_password(id, hash_password(password))

# Delete user account
@app.delete("/api/users/{id}")
async def delete_user(id: int):
    user_handler.delete(id)

'''@app.get("/api/")
async def home():
    return {"data": "Success connection!"}

@app.post("/api/notes")
async def add_note(data: NotesDataModel): 
    title     = data.title
    content   = data.content
    time_now  = get_current_time()
    status    = True

    notes_table(title=title, content=content, date=time_now, status=status)
    notes_table.add()
    return {"data": "Note added successfully!"}

@app.put("/api/notes/{id}")
async def update_note(id: int, data: NotesDataModel):
    title    = data.title
    content  = data.content
    time_now = get_current_time()
    status   = data.status
    notes_table(title=title, content=content, date=time_now, status=status)
    notes_table.update(id)
    return {"data": "Note updated successfully!"}

@app.get("/api/notes")
async def view_all_notes():
    all_notes = all_notes_model.get_all()
    return {"data": all_notes}

@app.delete("/api/notes")
async def clear_all_notes():
    all_notes_model.clear_all()
    return {"data": "All notes deleted successfully!"}

@app.delete("/api/notes/{id}")
async def delete_note(id: int):
    note_id_model.delete(id)
    return {"data": "Note deleted successfully!"}

@app.get("/api/notes/{id}")
async def view_note(id: int):
    note_by_id = note_id_model.get(id)
    return {"data": note_by_id}

'''


# Client API 
# API tests https://fastapi.tiangolo.com/tutorial/testing/
# API in Lambda https://fastapi.tiangolo.com/deployment/lambda/
# API in Docker https://fastapi.tiangolo.com/deployment/docker/
# API webapp https://fastapi.tiangolo.com/deployment/web-applications/
# Use AWS DynamoDB https://fastapi.tiangolo.com/deployment/databases/#dynamodb


# API Key
# Database of users and API keys
# API Key in header
# Table: Notes  (FK: User_ID)
# Table: Users  (PK: ID)
