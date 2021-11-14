from datetime import datetime

from flask import Blueprint, Response, redirect, render_template, request

from controllers.session import Session
from controllers.session_controllers import create_session_db, find_session_db, remove_session_db
from controllers.user import User
from controllers.user_controllers import (create_user_db,
                                          find_user_by_username_db,
                                          find_user_db)

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


@bp_auth.route("login/", methods=["POST"])
def login():
    if "username" in request.form and "password" in request.form:
        user = find_user_by_username_db(request.form["username"])
        if (
            user
            and user["username"] == request.form["username"]
            and user["password"] == request.form["password"]
        ):
            # create user's session
            session = Session(user)
            create_session_db(session)

            # return session id to client
            resp = Response(str({"status": "success", "user": user}))
            resp.set_cookie("session-id", session.session_id, expires=session.time_exp)

            return resp
        else:
            return {"status": "fail", "message": "Username or password incorrect."}
    else:
        return {"status": "fail", "message": "Not enough attributes."}


@bp_auth.route("profile/", methods=["POST"])
def profile():
    if "session-id" in request.cookies:
        session = find_session_db(request.cookies["session-id"])
        if session:
            time_now = int(datetime.utcnow().timestamp())
            session_datetime = datetime.strptime(
                request.cookies["Expires"], "%a, %d %b %Y %H:%M:%S GMT"
            )
            session_time = int(session_datetime.timestamp())

            if session_time > time_now:
                user = find_user_db(request.form["user_id"])
                if user:
                    return {"status": "success", "user": str(user)}
                else:
                    return {"status": "fail", "message": "User not found."}
            
            remove_session_db(request.cookies["session-id"])
            return {"status": "fail", "message": "Session expired."}
        
        return  {"status": "fail", "message": "Session not found."}
    else:
        return {"status": "fail", "message": "Send session in request."}
