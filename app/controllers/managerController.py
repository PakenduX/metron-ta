from flask import Blueprint, request
from flask_jwt_extended.utils import get_jwt_identity
from app.security.validation.managerSchema import ManagerSchema
from app.services.managerService import ManagerService
from app.helpers.response import (
    not_found,
    success_response,
    unauthorized_error,
    unknown_error,
    bad_request,
)
from flask_jwt_extended import jwt_required
from app.helpers.password_hash import hash_password
from marshmallow import ValidationError

managers = Blueprint("managers", __name__, url_prefix="/api/v1/managers")
service = ManagerService()


@managers.get("/")
@jwt_required()
def getManagers():
    try:
        managers = service.get_all_managers()
        json_managers = []
        for manager in managers:
            json_managers.append({"name": manager.name, "email": manager.email})
        return success_response(data=json_managers)
    except:
        return unknown_error()


@managers.get("/<string:email>")
@jwt_required()
def get_manager_by_email(email):
    try:
        manager = service.get_manager_by_email(email=email)
        if manager is None:
            return not_found("Aucun manager avec cet email")

        # A manager can only get his own information
        identity = get_jwt_identity()
        if identity != email:
            return unauthorized_error()
        json_manager = {"name": manager.name, "email": manager.email}
        return success_response(data=json_manager)
    except:
        return unknown_error()


@managers.delete("/<string:uid>")
@jwt_required()
def delete_manager(uid):
    try:
        manager = service.get_manager_by_uid(uid=uid)
        if manager is None:
            return not_found("Aucun manager avec cet email")

        # A manager can only delete his own information
        identity = get_jwt_identity()
        if identity != manager.email:
            return unauthorized_error()
        service.delete_manager_by_uid(uid=uid)
        return success_response(message="Votre compte a été supprimé avec succès")
    except Exception as e:
        return unknown_error()


@managers.put("/<string:uid>")
@jwt_required()
def update_manager(uid):
    try:
        manager = service.get_manager_by_uid(uid=uid)
        if manager is None:
            return not_found("Aucun manager avec cet email")

        # A manager can only update his own information
        identity = get_jwt_identity()
        if identity != manager.email:
            return unauthorized_error()
        data = request.get_json()
        if data is None:
            return bad_request("Veuillez saisir les informations à modifier")
        email = None
        password = None
        name = None
        hashed_password = None
        if "email" in data:
            email = data["email"]
        if "password" in data:
            password = data["password"]
        if "name" in data:
            name = data["name"]
        if name is not None:
            ManagerSchema().load({"name": name}, partial=True)
        if email is not None:
            ManagerSchema().load({"email": email}, partial=True)
        if password is not None:
            ManagerSchema().load({"password": password}, partial=True)
            hashed_password = hash_password(password)

        service.update_manager(
            uid=uid, name=name, password=hashed_password, email=email
        )
        return success_response(
            message="Votre compte a été bien mis à jour avec succès"
        )
    except Exception as e:
        if isinstance(e, ValidationError):
            return bad_request(e.messages)
        return unknown_error()


@managers.get("/<string:email>/sites")
@jwt_required()
def get_manager_sites(email):
    try:
        manager = service.get_manager_by_email(email=email)
        if manager is None:
            return not_found("Aucun manager avec cet email")

        # A manager can only get his own information
        identity = get_jwt_identity()
        if identity != email:
            return unauthorized_error()

        json_data = []
        for site in manager.sites:
            json_data.append(
                {
                    "name": site.name,
                    "address": site.address,
                    "max_power": site.max_power,
                }
            )

        return success_response(data=json_data)
    except:
        return unknown_error()
