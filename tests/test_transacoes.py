from security import criar_hash_senha
from models import Usuario, Transacao


def test_api_esta_funcionando(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "API Financeira funcionando!"
    }


def test_usuario_nao_autenticado_nao_pode_alterar_transacao(client):
    response = client.put(
        "/transacoes/1",
        json={
            "descricao": "Tentativa de alteração",
            "valor": 999,
            "tipo": "entrada",
            "data": "2026-08-13"
        }
    )

    assert response.status_code == 401


def test_usuario_nao_pode_alterar_transacao_de_outro_usuario(
    client,
    db
):
    usuario1 = Usuario(
        nome="Usuario Teste 1",
        email="usuario1@teste.com",
        senha=criar_hash_senha("123456")
    )

    usuario2 = Usuario(
        nome="Usuario Teste 2",
        email="usuario2@teste.com",
        senha=criar_hash_senha("123456")
    )

    db.add_all([usuario1, usuario2])
    db.commit()

    db.refresh(usuario1)
    db.refresh(usuario2)

    transacao = Transacao(
        descricao="Transação do usuario 1",
        valor=100,
        tipo="entrada",
        usuario_id=usuario1.id
    )

    db.add(transacao)
    db.commit()
    db.refresh(transacao)

    login = client.post(
        "/login",
        json={
            "email": "usuario2@teste.com",
            "senha": "123456"
        }
    )

    assert login.status_code == 200

    token = login.json()["access_token"]

    response = client.put(
        f"/transacoes/{transacao.id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "descricao": "Tentativa usuario 2",
            "valor": 999,
            "tipo": "entrada",
            "data": "2026-08-13"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Transação não encontrada"


def test_usuario_nao_pode_excluir_transacao_de_outro_usuario(
    client,
    db
):
    usuario1 = Usuario(
        nome="Usuario Teste 1",
        email="usuario1_delete@teste.com",
        senha=criar_hash_senha("123456")
    )

    usuario2 = Usuario(
        nome="Usuario Teste 2",
        email="usuario2_delete@teste.com",
        senha=criar_hash_senha("123456")
    )

    db.add_all([usuario1, usuario2])
    db.commit()

    db.refresh(usuario1)
    db.refresh(usuario2)

    transacao = Transacao(
        descricao="Transação protegida",
        valor=100,
        tipo="entrada",
        usuario_id=usuario1.id
    )

    db.add(transacao)
    db.commit()
    db.refresh(transacao)

    login = client.post(
        "/login",
        json={
            "email": "usuario2_delete@teste.com",
            "senha": "123456"
        }
    )

    assert login.status_code == 200

    token = login.json()["access_token"]

    response = client.delete(
        f"/transacoes/{transacao.id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Transação não encontrada"

def test_resumo_mostra_apenas_transacoes_do_usuario(
    client,
    db
):
    usuario1 = Usuario(
        nome="Usuario Resumo 1",
        email="usuario_resumo1@teste.com",
        senha=criar_hash_senha("123456")
    )

    usuario2 = Usuario(
        nome="Usuario Resumo 2",
        email="usuario_resumo2@teste.com",
        senha=criar_hash_senha("123456")
    )

    db.add_all([usuario1, usuario2])
    db.commit()

    db.refresh(usuario1)
    db.refresh(usuario2)

    transacao_usuario1 = Transacao(
        descricao="Entrada usuario 1",
        valor=100,
        tipo="entrada",
        usuario_id=usuario1.id
    )

    transacao_usuario2 = Transacao(
        descricao="Entrada usuario 2",
        valor=500,
        tipo="entrada",
        usuario_id=usuario2.id
    )

    db.add_all([
        transacao_usuario1,
        transacao_usuario2
    ])

    db.commit()

    login = client.post(
        "/login",
        json={
            "email": "usuario_resumo1@teste.com",
            "senha": "123456"
        }
    )

    assert login.status_code == 200

    token = login.json()["access_token"]

    response = client.get(
        "/resumo",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    dados = response.json()

    assert dados["total_entradas"] == 100
    assert dados["total_saidas"] == 0
    assert dados["saldo"] == 100

def test_resumo_financeiro_isolado_por_usuario(client, db):
    usuario1 = Usuario(
        nome="Usuario Resumo 1",
        email="resumo1@teste.com",
        senha=criar_hash_senha("123456")
    )

    usuario2 = Usuario(
        nome="Usuario Resumo 2",
        email="resumo2@teste.com",
        senha=criar_hash_senha("123456")
    )

    db.add_all([usuario1, usuario2])
    db.commit()

    db.refresh(usuario1)
    db.refresh(usuario2)

    transacao1 = Transacao(
        descricao="Entrada usuario 1",
        valor=100,
        tipo="entrada",
        usuario_id=usuario1.id
    )

    transacao2 = Transacao(
        descricao="Saida usuario 1",
        valor=30,
        tipo="saida",
        usuario_id=usuario1.id
    )

    transacao3 = Transacao(
        descricao="Entrada usuario 2",
        valor=500,
        tipo="entrada",
        usuario_id=usuario2.id
    )

    db.add_all([transacao1, transacao2, transacao3])
    db.commit()

    login = client.post(
        "/login",
        json={
            "email": "resumo1@teste.com",
            "senha": "123456"
        }
    )

    assert login.status_code == 200

    token = login.json()["access_token"]

    response = client.get(
        "/resumo",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    dados = response.json()

    assert dados["total_entradas"] == 100
    assert dados["total_saidas"] == 30
    assert dados["saldo"] == 70