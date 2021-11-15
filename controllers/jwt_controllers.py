import base64
import hashlib
import hmac
import json


class JWTToken:
    def __init__(self, header, payload):
        self.__header = header
        self.__payload = payload
        self.__secret_key = b"123456"

    @property
    def header(self):
        header = json.dumps(self.__header)
        base64header = base64.b64encode(header.encode("utf-8"))
        return base64header

    @property
    def payload(self):
        payload = json.dumps(self.__payload)
        base64payload = base64.b64encode(payload.encode("utf-8"))
        return base64payload

    def generate_signature(self):
        if self.__header and self.__payload:
            base64header = self.header
            base64payload = self.payload
            base64sum = (
                base64header.decode("utf-8") + "." + base64payload.decode("utf-8")
            )
            base64sum = base64sum.encode("utf-8")
            signature = hmac.new(
                self.__secret_key, base64sum, hashlib.sha256
            ).hexdigest()

            return signature

    def generate_jwt_token(self):
        header = self.header.decode("utf-8")
        payload = self.payload.decode("utf-8")
        signature = self.generate_signature()
        if signature:
            return f"{header}.{payload}.{signature}"

    def validate_jwt_token(self, token):
        token_header = token.split(".")[0]
        token_payload = token.split(".")[1]
        token_signature = token.split(".")[2]

        signature = hmac.new(
            self.__secret_key,
            f"{token_header}.{token_payload}".encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        if signature == token_signature:
            return True
