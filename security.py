from passlib.context import CryptContext
from jose import jwt


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

SECRET_KEY = "chave-secreta-financeiro-api"
ALGORITHM = "HS256"


def criar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)


def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)


def criar_token_jwt(dados: dict) -> str:
    return jwt.encode(
        dados,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def validar_token_jwt(token: str) -> dict:
    try:
        dados = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return dados

    except Exception:
        return {}