from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi25.app import app


def test_root_deve_retornar_ok_e_Hello_World():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK   # Assert
    assert response.json() == {'message': 'Hello World!'}  # Assert


def test_root_deve_retornar_ok_e_Ola_Mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/ola_mundo')  # Act

    assert response.status_code == HTTPStatus.OK   # Assert
    # assert response.text == ["Ola Mundo!"]  # Assert
