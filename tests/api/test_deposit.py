import requests

BASE_URL = "https://test-bees.herokuapp.com"
TIMEOUT = 3

def test_get_successful():
    r = requests.get(url=f'{BASE_URL}/deposits.json', timeout=TIMEOUT)
    print(r.json())
    assert r.status_code == 200


def test_post_new_deposit():
    r = requests.post(url=f'{BASE_URL}/deposits.json', json=
    {"name": "post",
     "address": "teste",
     "city": "teste",
     "state": "teste",
     "zipcode": "teste"
     }, timeout=TIMEOUT)
    assert r.status_code == 201


def test_get_deposit_by_id():
    id = 157
    r = requests.get(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 200

def test_patch_deposit_by_id():
    id = 157
    r = requests.patch(url=f'{BASE_URL}/deposits/{id}.json', json=
    {"city": "patch"
     }, timeout=TIMEOUT)
    assert r.status_code == 200


def test_fail_patch_deposit_by_id():
    id = 0
    r = requests.patch(url=f'{BASE_URL}/deposits/{id}.json', json=
    {"city": "patch"
     }, timeout=TIMEOUT)
    assert r.status_code == 404

def test_delete_deposit_by_id_deposit():
    id = 106
    r = requests.delete(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 204