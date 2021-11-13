from flask import Flask, request
from auth.authentification import bp_auth

app = Flask(__name__)

app.register_blueprint(bp_auth)

if __name__ == "__main__":
	app.run()
