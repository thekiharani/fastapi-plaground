from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=['bcrypt'], deprecated='auto')


def bcrypt(password: str):
    return pwd_ctx.hash(password)


def verify(hashed: str, plain_text: str):
    return pwd_ctx.verify(plain_text, hashed)


class Hash:
    pass
