import pytest


@pytest.fixture
def usuario_teste():
    return {
        "nome": "Alex",
        "email": "alex@email.com"
    }
