from flask import Blueprint, Response, redirect, render_template, request

from controllers.session import Session
from controllers.session_controllers import create_session_db, find_session_db
from controllers.user import User
from controllers.user_controllers import create_user_db, find_user_db

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("register/", methods=["POST"])
def register():
    if "username" in request.form and "password" in request.form:
        # create user
        user = User(request.form["username"], request.form["password"])
        create_user_db(user)

        # create user's session
        session = Session(user.get_user())
        create_session_db(session)

        # return session id to client
        resp = Response({"status": "success"})
        resp.set_cookie("session-id", session.session_id, expires=session.time_exp)

        return resp
    else:
        return {"status": "fail", "message": "Not enough attributes."}
