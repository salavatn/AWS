from pydantic import BaseModel, Field

# RegEx for email validation:
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

class UserDataModel(BaseModel):
    UserName:     str  = Field(..., min_length=2,  max_length=50, description="Username must be at least 2 characters long")
    LastName:     str  = Field(..., min_length=2,  max_length=50, description="Lastname must be at least 2 characters long")
    Password:     str  = Field(..., min_length=6,  max_length=50, description="Password must be at least 6 characters long")
    EmailAddress: str  = Field(..., min_length=7,  max_length=50, description="Email must be valid", regex=email_regex)
    # DateCreated:  str  = Field(..., min_length=10, max_length=10)
    
'''
class NotesDataModel(BaseModel):
    # id > 0, unique
    # id:      int  = Field(..., ge=1)
    title:   str  = Field(..., max_length=30, min_length=1)
    content: str  = Field(..., max_length=200, min_length=1)
    status:  bool   # = Field(..., max_length=1, min_length=1)

    # date: str    = BaseModel.Field(...)

'''