from flask import Blueprint, request
from flask_jwt_extended.utils import get_jwt_identity
from app.security.validation.siteSchema import SiteSchema
from app.helpers.response import (
    created_response,
    not_found,
    success_response,
    unauthorized_error,
    unknown_error,
    bad_request,
)
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.services.managerService import ManagerService
from app.services.siteService import SiteService
import uuid

sites = Blueprint("sites", __name__, url_prefix="/api/v1/sites")
service = SiteService()
managerService = ManagerService()


@sites.post("/add")
@jwt_required()
def add_site():
    try:
        data = request.get_json()
        if data is None:
            return bad_request("Veuillez saisir les informations du site")
        SiteSchema().load(data)
        # If Manager not exist and try to add a site (in real app the jwt may not be valid)
        manager = managerService.get_manager_by_email(get_jwt_identity())
        if manager is None:
            return unauthorized_error()
        service.create_site(
            uid=str(uuid.uuid4()),
            name=data["name"],
            address=data["address"],
            max_power=data["max_power"],
            manager_id=manager.uid,
        )
        return created_response()
    except Exception as e:
        if isinstance(e, ValidationError):
            return bad_request(e.messages)
        return unknown_error()


@sites.get("/")
@jwt_required()
def getSites():
    try:
        sites = service.get_all_sites()
        json_sites = []
        for site in sites:
            json_sites.append(
                {
                    "name": site.name,
                    "address": site.address,
                    "max_power": site.max_power,
                }
            )
        return success_response(data=json_sites)
    except:
        return unknown_error()


@sites.get("/<string:uid>")
@jwt_required()
def get_site_by_uid(uid):
    try:
        site = service.get_site_by_uid(uid=uid)
        if site is None:
            return not_found("Cet site n'existe pas")

        # Only the manager of the site can get informations about it
        identity = get_jwt_identity()
        manager = managerService.get_manager_by_email(identity)
        if manager is None:
            return unauthorized_error()
        if site.manager_id != manager.uid:
            return unauthorized_error()
        json_site = {
            "name": site.name,
            "address": site.address,
            "max_power": site.max_power,
        }
        return success_response(data=json_site)
    except:
        return unknown_error()


@sites.delete("/<string:uid>")
@jwt_required()
def delete_site(uid):
    try:
        site = service.get_site_by_uid(uid=uid)
        if site is None:
            return not_found("Ce site n'existe pas")

        # Only the manager of the site can delete it
        identity = get_jwt_identity()
        manager = managerService.get_manager_by_email(identity)
        if manager is None or site.manager_id != manager.uid:
            return unauthorized_error()
        service.delete_site_by_uid(uid=uid)
        return success_response(message="Votre site a été supprimé avec succès")
    except:
        return unknown_error()


@sites.put("/<string:uid>")
@jwt_required()
def update_site(uid):
    try:
        site = service.get_site_by_uid(uid=uid)
        if site is None:
            return not_found("Ce site n'existe pas")

        # Only the manager of the site can update it
        identity = get_jwt_identity()
        manager = managerService.get_manager_by_email(identity)
        if manager is None or site.manager_id != manager.uid:
            return unauthorized_error()
        data = request.get_json()
        if data is None:
            return bad_request("Veuillez saisir les informations à modifier")
        max_power = None
        name = None
        address = None
        # We update only the fields sent by the client
        if "max_power" in data:
            max_power = data["max_power"]
        if "address" in data:
            address = data["address"]
        if "name" in data:
            name = data["name"]
        if name is not None:
            SiteSchema().load({"name": name}, partial=True)
        if address is not None:
            SiteSchema().load({"address": address}, partial=True)
        if max_power is not None:
            SiteSchema().load({"max_power": max_power}, partial=True)

        service.update_site(uid=uid, name=name, max_power=max_power, address=address)
        return success_response(message="Votre site a été bien mis à jour avec succès")
    except Exception as e:
        if isinstance(e, ValidationError):
            return bad_request(e.messages)
        return unknown_error()


@sites.get("/<string:uid>/assets")
@jwt_required()
def get_site_assets(uid):
    try:
        site = service.get_site_by_uid(uid=uid)
        if site is None:
            return not_found("Ce site n'existe pas")

        # Only the manager of the site can update it
        identity = get_jwt_identity()
        manager = managerService.get_manager_by_email(identity)
        if manager is None or site.manager_id != manager.uid:
            return unauthorized_error()
        json_assets = []
        for asset in site.assets:
            json_assets.append(
                {
                    "name": asset.name,
                    "power": asset.power,
                    "asset_type": asset.asset_type,
                }
            )
        return success_response(data=json_assets)
    except:
        return unknown_error()
