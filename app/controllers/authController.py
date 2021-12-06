from flask import Blueprint, request
from app.helpers.response import (
    bad_request,
    created_response,
    not_found,
    success_response,
    unauthorized_error,
    unknown_error,
)
from app.security.validation.managerSchema import ManagerSchema
from marshmallow import ValidationError
from app.services.managerService import ManagerService
import uuid
from argon2.exceptions import VerifyMismatchError
from flask_jwt_extended import create_access_token, create_refresh_token
from app.helpers.password_hash import hash_password, verify_password
from sqlalchemy import exc

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")
managerService = ManagerService()


@auth.post("/register")
def register():
    try:
        data = request.get_json()
        if data is None:
            return bad_request("Veuillez saisir vos informations")
        ManagerSchema().load(data)

        managerService.create_manager(
            uid=uuid.uuid4(),
            name=data["name"],
            email=data["email"],
            password=hash_password(data["password"]),
        )
        return created_response()
    except Exception as e:
        # This exception occurs in case of unique property violation
        if isinstance(e, exc.IntegrityError):
            return bad_request("Un manager existe déjà avec cet email")
        if isinstance(e, ValidationError):
            return bad_request(e.messages)
        return unknown_error()


@auth.post("/login")
def login():
    try:
        data = request.get_json()
        if data is None or "email" not in data or "password" not in data:
            return bad_request("Veuillez saisir vos identifiants")

        email = data["email"]
        password = data["password"]
        user = managerService.get_manager_by_email(email=email)
        if user is None:
            return not_found("Aucun manager avec cet email")
        passwordIsOk = verify_password(user.password, password=password)

        if passwordIsOk:
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
        # If password is not okay the exception is thrown
        return success_response(
            message="",
            data={"access_token": access_token, "refresh_token": refresh_token},
        )
    except Exception as e:
        if isinstance(e, VerifyMismatchError):
            return unauthorized_error("Votre mot de passe est incorrect")
        print(e)
        return unknown_error()
