from pydantic import BaseModel, Field


class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)


class NoteDB(NoteSchema):
    id: int


class UserSchema(BaseModel):
    user_name:str = ""
    user_pass:str = ""


class UserDB(UserSchema):
    id:int


class CouPonseAct(BaseModel):
    user_id:str = Field(..., min_length=36, max_length=36)
    couponse_id:str = Field(..., min_length=36, max_length=36)

class CreateOrder(BaseModel):
    user_name:str = ""
    user_phone:int = ""
    buyer_num:int = 0
    recharge:bool