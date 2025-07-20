import jwt


def make_jwt(login: str, password: str) -> str:
    return jwt.encode(payload={"login": login, "password": password},
                      key='qyn!\:_FCKi6KEN>OVT?Qf2jD+>EzT~_[%+(fr@I"4U.$l-gdpr',
                      algorithm="HS256")


def decode_jwt(token: str) -> dict:
    try:
        return jwt.decode(jwt=token, key='qyn!\:_FCKi6KEN>OVT?Qf2jD+>EzT~_[%+(fr@I"4U.$l-gdpr', algorithms=['HS256'])
    except:
        return {}
