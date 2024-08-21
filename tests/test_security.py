from http import HTTPStatus

from jwt import decode

from fast_zero.security import ALGORITHM, SECRETE_KEY, create_access_token


def test_jwt():
    data = {'teste': 'teste@teste.com'}
    token = create_access_token(data)

    decoded = decode(token, SECRETE_KEY, algorithms=[ALGORITHM])

    assert decoded['teste'] == data['teste']
    assert decoded['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer invalid-token'}
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'could not validate credentials'}
