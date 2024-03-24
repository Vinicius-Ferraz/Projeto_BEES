import requests

BASE_URL = "https://test-bees.herokuapp.com"

def test_get_successful():
    r = requests.get(url=f'{BASE_URL}/deposits.json', timeout=5)
    print(r.json())
    assert r.status_code == 200


def test_post_new_deposit():
    r = requests.post(url=f'{BASE_URL}/deposits.json', json=
    {"name": "post",
     "address": "teste",
     "city": "teste",
     "state": "teste",
     "zipcode": "teste"
     })
    assert r.status_code == 201


def test_get_deposit_by_id():
    r = requests.get(url=f'{BASE_URL}/deposits/{157}.json', timeout=5)
    assert r.status_code == 200

def test_patch_deposit_by_id():
    r = requests.patch(url=f'{BASE_URL}/deposits/{157}.json', json=
    {"city": "patch"
     })
    assert r.status_code == 200


def test_fail_patch_deposit_by_id():
    r = requests.patch(url=f'{BASE_URL}/deposits/{0}.json', json=
    {"city": "patch"
     })
    assert r.status_code == 404

def test_delete_deposit_by_id_deposit():
    r = requests.delete(url=f'{BASE_URL}/deposits/{106}.json')
    assert r.status_code == 204