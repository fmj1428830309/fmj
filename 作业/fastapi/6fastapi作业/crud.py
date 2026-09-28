
from fastapi import HTTPException

from sqlalchemy.exc import DataError, IntegrityError
from sqlmodel import Session, select
from models import User,UserCreate,UserPatch

def list_User(session: Session)->list[User]:
    return session.exec(select(User)).all()
def read_User(session: Session,user_id:int)->User:
    user = session.get(User,user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def CreateUser(session: Session,data:UserCreate)->User:
    user = User(**data.model_dump())
    user.id=None
    session.add(user)
    try:
        session.commit()
    except(IntegrityError,DataError) as e:
        session.rollback()
        print(e)
        raise HTTPException(status_code=400,detail="User already exists")
    session.refresh(user)
    return user

def UpdateUser(session: Session,user_id:int,patch:UserPatch)->User:
    data=patch.model_dump(exclude_unset=True)
    if not data:
        raise HTTPException(status_code=404,detail="User not found")
    user = read_User(session,user_id)
    for k,v in data.items():
        setattr(user,k,v)
    try:
        session.commit()
    except(IntegrityError,DataError) as e:
        session.rollback()
        print(e)
        raise HTTPException(status_code=400,detail="User already exists")
    session.refresh(user)
    return user
def remove_User(session: Session,user_id:int)->User:
    user = read_User(session,user_id)
    session.delete(user)
    session.commit()
    return user

