from flask import jsonify
from app import jwt

"""
    These functions are used to respond to the clients with
    success or error messages
"""


def success_response(message=None, data=None):
    return jsonify({"status": "success", "message": message, "data": data}), 200


def created_response():
    return "", 201


def bad_request(message):
    return jsonify({"status": "error", "message": message}), 400


def unknown_error():
    return (
        jsonify({"status": "error", "message": "Une erreur inconnue s'est produite"}),
        500,
    )


def unauthorized_error(message=None):
    return (
        jsonify(
            {
                "status": "error",
                "message": message
                if message is not None
                else "Vous n'êtes pas autorisé à effectuer cette action",
            }
        ),
        401,
    )


def not_found(message):
    return (
        jsonify(
            {
                "status": "error",
                "message": message
                if message is not None
                else "Ressource non disponible",
            }
        ),
        404,
    )


@jwt.expired_token_loader
def token_expired(jwt_header, jwt_payload):
    return (
        jsonify(
            {
                "status": "error",
                "message": "Votre token a expiré, veuillez vous reconnecter",
            }
        ),
        401,
    )


@jwt.invalid_token_loader
def token_invalid(jwt_header, jwt_payload):
    return (
        jsonify(
            {
                "status": "error",
                "message": "Votre token est invalide, veuillez vous reconnecter",
            }
        ),
        401,
    )
