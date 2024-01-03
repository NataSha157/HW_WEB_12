from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.entity.models import User
from src.repository import contacts as repositories_contacts
from src.schemas.contact import ContactSchema, ContactUpdateSchema, ContactResponse
from src.services.auth import auth_service

router = APIRouter(prefix='/contacts', tags=['contacts'])


@router.get("/", response_model=list[ContactResponse])
async def get_contacts(limit: int = Query(10, ge=10, le=500), offset: int = Query(0, ge=0),
                       db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    contacts = await repositories_contacts.get_contacts(limit, offset, db, user)
    return contacts

# @router.get("/all", response_model=list[ContactResponse])
# async def get_contacts(limit: int = Query(10, ge=10, le=500), offset: int = Query(0, ge=0),
#                        db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
#     contacts = await repositories_contacts.get_all_contacts(limit, offset, db)
#     return contacts

@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db),
                      user: User = Depends(auth_service.get_current_user)):
    contact = await repositories_contacts.get_contact(contact_id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactSchema, db: AsyncSession = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    contact = await repositories_contacts.create_contact(body, db, user)
    return contact


@router.put("/{contact_id}")
async def update_contact(body: ContactUpdateSchema, contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    contact = await repositories_contacts.update_contact(contact_id, body, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    contact = await repositories_contacts.delete_contact(contact_id, db, user)
    return contact


@router.get("/firstname/{firstname}", response_model=list[ContactResponse])
async def get_firstname_contacts(firstname: str = Path(), limit: int = Query(10, ge=10, le=500),
                                 offset: int = Query(0, ge=0),
                                 db: AsyncSession = Depends(get_db),
                                 user: User = Depends(auth_service.get_current_user)):
    firstname_contacts = await repositories_contacts.get_firstname_contacts(firstname, limit, offset, db, user)
    return firstname_contacts


@router.get("/lastname/{lastname}", response_model=list[ContactResponse])
async def get_lastname_contacts(lastname: str = Path(), limit: int = Query(10, ge=10, le=500),
                                offset: int = Query(0, ge=0),
                                db: AsyncSession = Depends(get_db),
                                user: User = Depends(auth_service.get_current_user)):
    lastname_contacts = await repositories_contacts.get_lastname_contacts(lastname, limit, offset, db, user)
    return lastname_contacts


@router.get("/email/{e_mail}", response_model=list[ContactResponse])
async def get_email_contacts(e_mail: EmailStr, limit: int = Query(10, ge=10, le=500), offset: int = Query(0, ge=0),
                             db: AsyncSession = Depends(get_db),
                             user: User = Depends(auth_service.get_current_user)):
    email_contacts = await repositories_contacts.get_email_contacts(e_mail, limit, offset, db, user)
    return email_contacts


@router.get("/birthdays/", response_model=list[ContactResponse])
async def get_birthdays_per_week(limit: int = Query(10, ge=10, le=500), offset: int = Query(0, ge=0),
                                 db: AsyncSession = Depends(get_db),
                                 user: User = Depends(auth_service.get_current_user)):
    contacts = await repositories_contacts.get_birthdays_per_week(limit, offset, db, user)
    return contacts
