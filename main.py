from pydantic import BaseModel
from typing import Literal
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import engine, Base, get_db
import models
from schemas import (
    TransacaoCreate,
    TransacaoUpdate,
    TransacaoResponse,
    UsuarioCreate,
    UsuarioResponse
)
from security import criar_hash_senha, verificar_senha, criar_token_jwt, validar_token_jwt

class LoginRequest(BaseModel):
    email: str
    senha: str


app = FastAPI(
    title="API Financeira",
    description="API para gerenciamento de usuários e transações financeiras com autenticação JWT.",
    version="1.0.0"
)

bearer_scheme = HTTPBearer()

def obter_usuario_token(
    credenciais: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    token = credenciais.credentials
    dados = validar_token_jwt(token)

    if not dados:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    return dados

security = HTTPBearer()

Base.metadata.create_all(bind=engine)


def obter_usuario_atual(
    credenciais = Depends(security)
):
    token = credenciais.credentials

    dados = validar_token_jwt(token)

    if not dados:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    return dados

  
@app.get("/")
def home():
    return {"mensagem": "API Financeira funcionando!"}


@app.get("/transacoes")
def listar_transacoes(
    tipo: Literal["entrada", "saida"] | None = None,
    db: Session = Depends(get_db),
    usuario_atual: dict = Depends(obter_usuario_atual)
):
    query = db.query(models.Transacao).filter(
    models.Transacao.usuario_id == int(usuario_atual["sub"])
)

    if tipo:
        query = query.filter(models.Transacao.tipo == tipo)

    return query.all()

@app.get("/resumo")
def resumo_financeiro(
    db: Session = Depends(get_db),
    usuario_atual: dict = Depends(obter_usuario_atual)
):
    usuario_id = int(usuario_atual["sub"])

    total_entradas = db.query(
        func.sum(models.Transacao.valor)
    ).filter(
        models.Transacao.tipo == "entrada",
        models.Transacao.usuario_id == usuario_id
    ).scalar()

    total_saidas = db.query(
        func.sum(models.Transacao.valor)
    ).filter(
        models.Transacao.tipo == "saida",
        models.Transacao.usuario_id == usuario_id
    ).scalar()

    total_entradas = total_entradas or 0
    total_saidas = total_saidas or 0

    saldo = total_entradas - total_saidas

    return {
        "total_entradas": total_entradas,
        "total_saidas": total_saidas,
        "saldo": saldo
    }

@app.post(
    "/transacoes",
    status_code=201,
    response_model=TransacaoResponse
)
def criar_transacao(
    transacao: TransacaoCreate,
    db: Session = Depends(get_db),
    usuario_atual: dict = Depends(obter_usuario_atual)
):
    nova_transacao = models.Transacao(
    descricao=transacao.descricao,
    valor=transacao.valor,
    tipo=transacao.tipo,
    data=transacao.data,
    usuario_id=int(usuario_atual["sub"])
)

    db.add(nova_transacao)
    db.commit()
    db.refresh(nova_transacao)

    return nova_transacao


@app.put(
    "/transacoes/{id}",
    response_model=TransacaoResponse,
    responses={
        404: {"description": "Transação não encontrada"}
    }

)
def atualizar_transacao(
    id: int,
    transacao: TransacaoUpdate,
    db: Session = Depends(get_db),
    usuario_atual: dict = Depends(obter_usuario_atual)
):
    transacao_db = db.query(models.Transacao).filter(
    models.Transacao.id == id,
    models.Transacao.usuario_id == int(usuario_atual["sub"])
).first()

    if transacao_db is None:
        raise HTTPException(
            status_code=404,
            detail="Transação não encontrada"
        )

    transacao_db.descricao = transacao.descricao
    transacao_db.valor = transacao.valor
    transacao_db.tipo = transacao.tipo
    transacao_db.data = transacao.data

    db.commit()
    db.refresh(transacao_db)

    return transacao_db


@app.delete(
    "/transacoes/{id}",
    responses={
        404: {"description": "Transação não encontrada"}
    }
)
def excluir_transacao(
    id: int,
    db: Session = Depends(get_db),
    usuario_atual: dict = Depends(obter_usuario_atual)
):
    transacao_db = db.query(models.Transacao).filter(
    models.Transacao.id == id,
    models.Transacao.usuario_id == int(usuario_atual["sub"])
).first()

    if transacao_db is None:
        raise HTTPException(
            status_code=404,
            detail="Transação não encontrada"
        )

    db.delete(transacao_db)
    db.commit()

    return {
        "mensagem": "Transação excluída com sucesso!",
        "id": id
    }

@app.post(
    "/usuarios",
    status_code=201,
    response_model=UsuarioResponse
)
def criar_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario_existente = db.query(models.Usuario).filter(
        models.Usuario.email == usuario.email
    ).first()

    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="E-mail já cadastrado"
        )

    novo_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=criar_hash_senha(usuario.senha)
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


@app.post("/login")
def login(
    dados: LoginRequest,
    db: Session = Depends(get_db)
):
    usuario = db.query(models.Usuario).filter(
        models.Usuario.email == dados.email
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha inválidos"
        )

    senha_valida = verificar_senha(
        dados.senha,
        usuario.senha
    )

    if not senha_valida:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha inválidos"
        )

    token = criar_token_jwt({
        "sub": str(usuario.id),
        "email": usuario.email
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }