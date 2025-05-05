
import jwt

SECRET = "jwt_secret_key"

def authenticate_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload["user_id"]
    except Exception:
        return None
