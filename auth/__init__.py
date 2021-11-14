from flask import Response, g, request

from auth.authentification import bp_auth
from controllers.jwt_controllers import JWTToken


@bp_auth.before_app_first_request
def before_first_request():
    pass


@bp_auth.before_app_request
def before_request():
    susi_path = ["/auth/register/", "/auth/login/"]

    if request.path not in susi_path:
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].replace("Bearer ", "")
            jwt = JWTToken({}, {})
            valid = jwt.validate_jwt_token(token)
            if not valid:
                return Response(status=401, response="User unauthorized!")
        else:
            return Response(status=401, response="Missing authorization token!")
