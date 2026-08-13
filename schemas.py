from typing import Literal
from datetime import date

from pydantic import BaseModel, Field


class TransacaoBase(BaseModel):
    descricao: str = Field(min_length=1)
    valor: float = Field(gt=0)
    tipo: Literal["entrada", "saida"]
    data: date | None = None


class TransacaoCreate(TransacaoBase):
    pass


class TransacaoUpdate(TransacaoBase):
    pass


class TransacaoResponse(TransacaoBase):
    id: int

    class Config:
        from_attributes = True


class UsuarioCreate(BaseModel):
    nome: str = Field(min_length=1)
    email: str
    senha: str = Field(min_length=6)


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True