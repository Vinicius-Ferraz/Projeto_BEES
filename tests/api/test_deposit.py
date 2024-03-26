import requests

BASE_URL = "https://test-bees.herokuapp.com"
TIMEOUT = 3


def create_deposit_to_get_id():
    name = "Get ID"
    address = "teste"
    city = "teste"
    state = "teste"
    zipcode = "teste"
    create = requests.post(url=f'{BASE_URL}/deposits.json', json=
    {"name": name,
     "address": address,
     "city": city,
     "state": state,
     "zipcode": zipcode
     }, timeout=TIMEOUT)
    id = create.json().get('id')
    return create


def test_get_successful():
    r = requests.get(url=f'{BASE_URL}/deposits.json', timeout=TIMEOUT)
    assert r.status_code == 200


def test_post_new_deposit():
    name = "Get ID"
    address = "teste"
    city = "teste"
    state = "teste"
    zipcode = "teste"
    r = requests.post(url=f'{BASE_URL}/deposits.json', json=
    {"name": name,
     "address": address,
     "city": city,
     "state": state,
     "zipcode": zipcode
     }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201
    # FIXME - This API does not have a field to be required




def test_get_deposit_by_id():
    r = create_deposit_to_get_id()
    id = r.json().get('id')
    requests.get(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 201
    d = requests.delete(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201


def test_get_deposit_by_id_fail():
    r = create_deposit_to_get_id()
    id = r.json().get('id')
    requests.get(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 201
    d = requests.delete(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204

    id = 0
    r = requests.get(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The documentation does not inform the status code for this test


def test_patch_deposit_by_id():
    c = create_deposit_to_get_id()
    id = c.json().get('id')
    r = requests.patch(url=f'{BASE_URL}/deposits/{id}.json', json=
    {"city": "patch"
     }, timeout=TIMEOUT)
    assert r.status_code == 200
    d = requests.delete(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204


def test_patch_deposit_by_id_fail():
    id = 0
    r = requests.patch(url=f'{BASE_URL}/deposits/{id}.json', json=
    {"city": "patch"
     }, timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The documentation does not inform the status code for this test


def test_put_deposit_by_id():
    c = create_deposit_to_get_id()
    id = c.json().get('id')
    name = "put but delete"
    address = "put"
    city = "put"
    state = "put"
    zipcode = "put"
    r = requests.put(url=f'{BASE_URL}/deposits/{id}.json', json=
    {"name": name,
     "address": address ,
     "city": city,
     "state": state,
     "zipcode": zipcode
     }, timeout=TIMEOUT)
    assert r.status_code == 200
    d = requests.delete(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204


def test_put_deposit_by_id_fail():
    id = 0
    r = requests.put(url=f'{BASE_URL}/deposits/{id}.json', json=
    {"name": "put",
     "address": "put",
     "city": "put",
     "state": "put",
     "zipcode": "put"
     }, timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The documentation does not inform the status code for this test


def test_put_deposit_by_id_incomplete_body():
    c = create_deposit_to_get_id()
    id = c.json().get('id')
    name = "put empty fields"
    address = "put"
    city = "put"
    r = requests.put(url=f'{BASE_URL}/deposits/{id}.json', json=
    {"name": name ,
     "address": address,
     "city": city,
     }, timeout=TIMEOUT)
    assert r.status_code == 200
    d = requests.delete(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The documentation does not inform the status code for this test
    # FIXME - In swagger, the API does not accept a body with missing fields


def test_delete_deposit_by_id_deposit():
    c = create_deposit_to_get_id()
    id = c.json().get('id')
    r = requests.delete(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 204
    # FIXME - The status coe informed at the documentation is 200, but the API is returning 204


def test_delete_deposit_by_id_deposit_fail():
    id = 0
    r = requests.delete(url=f'{BASE_URL}/deposits/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The status coe informed at the documentation is 200, but the API is returning 204
