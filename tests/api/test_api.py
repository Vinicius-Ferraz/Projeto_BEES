import pytest
import requests

BASE_URL = "https://test-bees.herokuapp.com"

def test_get_deposits():
    response = requests.get(f'{BASE_URL}/deposits.json')
    assert response.status_code == 200

def test_post_deposit():
    deposit = {
        "name": "Test",
        "address": "Test Address",
        "city": "Test City",
        "state": "Test State",
        "zipcode": "Test Zipcode"
    }
    response = requests.post(f'{BASE_URL}/deposits.json', json=deposit)
    assert response.status_code == 200

def test_get_deposit_by_id():
    id = '166'
    response = requests.get(f'{BASE_URL}/deposits/{id}.json')
    assert response.status_code == 200

def test_patch_deposit_by_id():
    id = '106'
    deposit = {
        "city": "New City"
    }
    response = requests.patch(f'{BASE_URL}/deposits/{id}.json', json=deposit)
    assert response.status_code == 200

def test_put_deposit_by_id():
    id = '170'
    deposit = {
        "name": "Updated",
        "address": "Updated Address",
        "city": "Updated City",
        "state": "Updated State",
        "zipcode": "Updated Zipcode"
    }
    response = requests.put(f'{BASE_URL}/deposits/{id}.json', json=deposit)
    assert response.status_code == 200

def test_delete_deposit_by_id():
    id = '1'
    response = requests.delete(f'{BASE_URL}/deposits/{id}.json')
    assert response.status_code == 200

def test_get_nonexistent_deposit():
    # Tente obter um depósito que não existe
    r = requests.get(url=f'{BASE_URL}/deposits/{999999}.json', timeout=5)
    assert r.status_code == 404

def test_post_deposit_missing_field():
    # Tente criar um novo depósito sem fornecer todos os campos necessários
    r = requests.post(url=f'{BASE_URL}/deposits.json', json=
    {"name": "post",
     "address": "teste",
     "city": "teste",
     "state": "teste"
     # "zipcode" está faltando
     })
    assert r.status_code == 400

def test_patch_nonexistent_deposit():
    # Tente atualizar um depósito que não existe
    r = requests.patch(url=f'{BASE_URL}/deposits/{999999}.json', json=
    {"city": "patch"
     })
    assert r.status_code == 404

def test_delete_nonexistent_deposit():
    # Tente deletar um depósito que não existe
    r = requests.delete(url=f'{BASE_URL}/deposits/{999999}.json')
    assert r.status_code == 404