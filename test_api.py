import pytest
from app import app
from flask_jwt_extended import create_access_token

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def get_access_token(client):
    response = client.post('/login', json={'username': 'admin', 'password': 'password'})
    json_data = response.get_json()
    return json_data['access_token']

def test_get_leads(client):
    response = client.get('/leads')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_create_lead(client):
    access_token = get_access_token(client)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    lead_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'telefone': '123456789',
        'latitude': 37.7749,
        'longitude': -122.4194,
        'temperature': 25.5,
        'interest': 'Tecnologia'
    }
    response = client.post('/leads', json=lead_data, headers=headers)
    assert response.status_code == 201
    assert response.get_json()['message'] == "Lead criado com sucesso!"

def test_get_lead(client):
    response = client.get('/leads/1')  
    if response.status_code == 404:
        assert response.get_json()['error'] == "Lead não encontrado."
    else:
        assert response.status_code == 200
        assert 'name' in response.get_json()

def test_update_lead(client):
    access_token = get_access_token(client)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    lead_data = {
        'name': 'John Doe Updated',
        'email': 'john.updated@example.com',
        'telefone': '987654321'
    }
    response = client.put('/leads/1', json=lead_data, headers=headers) 
    if response.status_code == 404:
        assert response.get_json()['error'] == "Lead não encontrado."
    else:
        assert response.status_code == 200
        assert response.get_json()['message'] == "Lead atualizado com sucesso!"

def test_delete_lead(client):
    access_token = get_access_token(client)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = client.delete('/leads/1', headers=headers)
    if response.status_code == 404:
        assert response.get_json()['error'] == "Lead não encontrado."
    else:
        assert response.status_code == 200
        assert response.get_json()['message'] == "Lead deletado com sucesso!"