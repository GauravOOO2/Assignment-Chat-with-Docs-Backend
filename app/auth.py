from fastapi import APIRouter, HTTPException
from google.oauth2 import id_token
from google.auth.transport import requests
from .config import settings
from . import crud, schemas

router = APIRouter()

@router.post("/auth/google")
async def google_auth(idToken: str):
    try:
        # Verify the token
        idinfo = id_token.verify_oauth2_token(idToken, requests.Request(), settings.GOOGLE_CLIENT_ID)

        # Get user information
        user_email = idinfo['email']
        user_name = idinfo['name']

        # Here you can create a new user in your database or retrieve existing user
        user = crud.get_user_by_email(user_email)  # Implement this function in crud.py
        if not user:
            user = crud.create_user(email=user_email, name=user_name)  # Implement this function in crud.py

        return {"user": {"email": user.email, "name": user.name}}  # Return user data

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid token")
