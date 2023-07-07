from Database.notes_db_models   import UsersTable, session
from sqlalchemy.orm.exc         import NoResultFound
from fastapi                    import HTTPException


class UserHandler:
    # Add User Account 
    def add(self, username: str, lastname: str, password: str, email: str, date: str, secret_key: str, status: bool):
        self.username    = username
        self.lastname    = lastname
        self.password    = password
        self.email       = email
        self.date        = date
        self.secret_key  = secret_key
        self.status      = status

        user = UsersTable(  
            UserName      = self.username, 
            LastName      = self.lastname, 
            Password      = self.password, 
            EmailAddress  = self.email, 
            DateCreated   = self.date, 
            SecretKey     = self.secret_key, 
            StatusAccount = self.status
            )
        session.add(user)
        session.commit()
        return user

    # Reset Password
    def update_password(self, user_id: int, password: str):
        try:
            user = session.query(UsersTable).filter(UsersTable.UserID == user_id).one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail=f"User is not found")
        user.Password = password
        session.commit()
        return user

    # Delete User Account
    def delete(self, user_id: int):
        try:
            user = session.query(UsersTable).filter(UsersTable.UserID == user_id).one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail=f"User is not found")
        session.delete(user)
        session.commit()
        return user

    # Get list of all users
    def get_all(self):
        return session.query(UsersTable).all()
    
    # Diactivate User Account
    def diactivate(self, user_id: int):
        try:
            user = session.query(UsersTable).filter(UsersTable.UserID == user_id).one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail=f"User is not found")
        user.StatusAccount = False
        session.commit()
        return user
    
'''    
    # Delete User Account
    def delete(self, user_id: int):
        try:
            user = session.query(UsersTable).filter(UsersTable.UserID == user_id).one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail=f"User is not found")
        session.delete(user)
        session.commit()
        return user

    # Get list of all users
    def get_all(self):
        return session.query(UsersTable).all()

'''
'''
class NotesHandler:        
    def add(self, title: str, content: str, date: str, status: bool):
        self.title   = title
        self.content = content
        self.date    = date
        self.status  = status

        table = NotesTable(title = self.title, 
            content = self.content, 
            date    = self.date, 
            status  = self.status
            )
        session.add(add_note)
        session.commit()
        return add_note
    
    def delete(self, note_id: int):
        try:
            note = session.query(Notes).filter(Notes.id == note_id).one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail=f"Note is not found")
        session.delete(note)
        session.commit()
        return note

    def update(self, id: int):
        note = session.query(Notes).filter(Notes.id == id).first()
        if note is None:
            raise HTTPException(status_code=404, detail=f"Note is not found")
        else:
            note.title    = self.title
            note.content  = self.content
            note.date     = self.date
            note.status   = self.status
            session.commit()


class AllNotesModel:
    def get_all(self):
        notes = session.query(Notes).all()
        return notes
    
    def clear_all(self):
        session.query(Notes).delete()
        session.commit()



class NoteIDModel:
    def delete(self, id):
        note = session.query(Notes).filter(Notes.id == id).first()
        if note is None:
            raise HTTPException(status_code=404, detail="Note is not found")
        else:
            session.delete(note)
            session.commit()

    def get(self, id):
        note = session.query(Notes).filter(Notes.id == id).first()
        if note is None:
            print("Note is not found")
            raise HTTPException(status_code=404, detail="Note is not found")
        else:
            return note

'''