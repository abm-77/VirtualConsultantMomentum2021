from itsdangerous import URLSafeTimedSerialiazer
from app import app

def GenerateConfirmationToken(email):
    serializer = URLSafeTimedSerialiazer(app.config["SECRET_KEY"])
    return serializer.dumps(email, salt=app.config["SECURITY_PASSWORD_SALT"])

def ConfirmToken(token, expiration= 3600):
    serializer = URLSafeTimedSerialiazer(app.config["SECRET_KEY"])
    try:
        email = serializer.loads(
            token,
            salt = app.config["SECURITY_PASSWORD_SALT"],
            max_age = expiration
        )
    except:
        return False

    return email
