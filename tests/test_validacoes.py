import pytest
from pydantic import ValidationError
from schemas import TransacaoCreate


def test_valor_nao_pode_ser_zero():
    with pytest.raises(ValidationError):
        TransacaoCreate(
            descricao="Teste",
            valor=0,
            tipo="entrada",
            data="2026-08-13"
        )


def test_valor_nao_pode_ser_negativo():
    with pytest.raises(ValidationError):
        TransacaoCreate(
            descricao="Teste",
            valor=-100,
            tipo="entrada",
            data="2026-08-13"
        )