from flask import Blueprint, request
from flask_jwt_extended.utils import get_jwt_identity
from app.security.validation.assetSchema import AssetSchema
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
from app.services.assetService import AssetService
from app.services.siteService import SiteService
import uuid
from app.constants.asset_types import AssetTypes

assets = Blueprint("assets", __name__, url_prefix="/api/v1/assets")
service = AssetService()
managerService = ManagerService()
siteService = SiteService()


@assets.post("/add")
@jwt_required()
def add_asset():
    try:
        data = request.get_json()
        if data is None:
            return bad_request("Veuillez saisir les informations de la machine")
        AssetSchema().load(data)
        manager = managerService.get_manager_by_email(get_jwt_identity())
        site = siteService.get_site_by_uid(data["site_id"])
        site_assets_power_sum = siteService.get_site_total_assets_power(site.uid)

        # the total power of the assets of a site must be lower than the maximum power of the site
        power = (
            site_assets_power_sum[0][0] + data["power"]
            if site_assets_power_sum[0][0] is not None
            else data["power"]
        )
        if power > site.max_power:
            return bad_request("Vous avez depassé la puissance maximale du site")
        if manager.uid != site.manager_id:
            return unauthorized_error()
        service.create_asset(
            uid=uuid.uuid4(),
            name=data["name"],
            asset_type=data["asset_type"],
            power=data["power"],
            site_id=data["site_id"],
        )
        return created_response()
    except Exception as e:
        print(e)
        if isinstance(e, ValidationError):
            return bad_request(e.messages)
        return unknown_error()


@assets.get("/")
@jwt_required()
def getAssets():
    try:
        assets = service.get_all_assets()
        json_assets = []
        for site in assets:
            json_assets.append(
                {
                    "name": site.name,
                    "asset_type": site.asset_type,
                    "power": site.power,
                }
            )
        return success_response(data=json_assets)
    except:
        return unknown_error()


@assets.get("/<string:uid>")
@jwt_required()
def get_asset_by_uid(uid):
    try:
        asset = service.get_asset_by_uid(uid=uid)
        if asset is None:
            return not_found("Cette machine n'existe pas")

        # Only the manager of the site can get informations about the site's assets
        manager = managerService.get_manager_by_email(get_jwt_identity())
        site = siteService.get_site_by_uid(asset.site_id)
        if site.manager_id != manager.uid:
            return unauthorized_error()
        json_asset = {
            "name": asset.name,
            "asset_type": asset.asset_type,
            "power": asset.power,
        }
        return success_response(data=json_asset)
    except:
        return unknown_error()


@assets.delete("/<string:uid>")
@jwt_required()
def delete_asset(uid):
    try:
        asset = service.get_asset_by_uid(uid=uid)
        if asset is None:
            return not_found("Cette machine n'existe pas")

        # Only the manager of the site can get informations about the site's assets
        manager = managerService.get_manager_by_email(get_jwt_identity())
        site = siteService.get_site_by_uid(asset.site_id)
        if site.manager_id != manager.uid:
            return unauthorized_error()
        service.delete_asset_by_uid(uid=uid)
        return success_response(message="Votre machine a été supprimé avec succès")
    except:
        return unknown_error()


@assets.put("/<string:uid>")
@jwt_required()
def update_asset(uid):
    try:
        data = request.get_json()
        asset = service.get_asset_by_uid(uid=uid)
        if asset is None:
            return not_found("Cette machine n'existe pas")

        # Only the manager of the site can update informations about the site's machine
        manager = managerService.get_manager_by_email(get_jwt_identity())
        site = siteService.get_site_by_uid(asset.site_id)

        site_assets_power_sum = siteService.get_site_total_assets_power(site.uid)

        # the total power of the assets of a site must be lower than the maximum power of the site
        if "power" in data and data["power"] is not None:
            power_x = (
                site_assets_power_sum[0][0] + data["power"]
                if site_assets_power_sum[0][0] is not None
                else data["power"]
            )
            if power_x > site.max_power:
                return bad_request("Vous avez depassé la puissance maximale du site")
            if site.manager_id != manager.uid:
                return unauthorized_error()

        if data is None:
            return bad_request("Veuillez saisir les informations à modifier")
        power = None
        name = None
        asset_type = None
        if "power" in data:
            power = data["power"]
        if "asset_type" in data:
            asset_type = data["asset_type"]
        if "name" in data:
            name = data["name"]
        if name is not None:
            AssetSchema().load({"name": name}, partial=True)
        if asset_type is not None:
            AssetSchema().load({"asset_type": asset_type}, partial=True)
        if power is not None:
            AssetSchema().load({"power": power}, partial=True)

        service.update_asset(uid=uid, name=name, power=power, asset_type=asset_type)
        return success_response(
            message="Votre machine a été bien mis à jour avec succès"
        )
    except Exception as e:
        if isinstance(e, ValidationError):
            return bad_request(e.messages)
        return unknown_error()
