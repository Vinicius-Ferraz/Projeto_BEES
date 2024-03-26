import requests

BASE_URL = "https://test-bees.herokuapp.com"
TIMEOUT = 3


def create_inventory_to_get_id():
    item_id = 190
    deposit_id = 34
    item_count = 0
    create = requests.post(url=f'{BASE_URL}/inventories.json', json={
     "item_id": item_id,
     "deposit_id": deposit_id,
     "item_count": item_count,
     }, timeout=TIMEOUT)
    id = create.json().get('id')
    return create


def test_get_successful():
    r = requests.get(url=f'{BASE_URL}/inventories.json', timeout=TIMEOUT)
    assert r.status_code == 200


def test_get_inventory_by_id():
    r = create_inventory_to_get_id()
    id = r.json().get('id')
    requests.get(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 201
    d = requests.delete(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201


def test_get_inventory_by_id_fail():
    id = 0
    r = requests.get(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The documentation does not inform the status code for this test


def test_post_new_inventory():
    item_id = 190
    deposit_id = 34
    item_count = 0
    r = requests.post(url=f'{BASE_URL}/inventories.json', json={
     "item_id": item_id,
     "deposit_id": deposit_id,
     "item_count": item_count,
     }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201
    # FIXME - This API does not have a field to be required


def test_post_new_inventory_without_deposit_id():
    r = requests.post(url=f'{BASE_URL}/inventories.json', json={
     "item_id": 190,
     "item_count": 0,
     }, timeout=TIMEOUT)
    assert r.status_code == 422


def test_post_new_inventory_without_item_id():
    deposit_id = 34
    item_count = 0
    r = requests.post(url=f'{BASE_URL}/inventories.json', json={
     "deposit_id": deposit_id,
     "item_count": item_count,
     }, timeout=TIMEOUT)
    assert r.status_code == 422


def test_post_new_inventory_without_item_count():
    item_id = 190
    deposit_id = 34
    r = requests.post(url=f'{BASE_URL}/inventories.json', json={
     "item_id": item_id,
     "deposit_id": deposit_id,
     }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204


def test_post_new_inventory_with_negative_item_count():
    item_id = 190
    deposit_id = 34
    item_count = -1
    r = requests.post(url=f'{BASE_URL}/inventories.json', json={
     "item_id": item_id,
     "deposit_id": deposit_id,
     "item_count": item_count,
     }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201
    # FIXME - Item count should not be negative


def test_post_new_inventory_with_an_taken_item():
    item_id = 199
    deposit_id = 34
    item_count = 0
    r = requests.post(url=f'{BASE_URL}/inventories.json', json={
     "item_id": item_id,
     "deposit_id": deposit_id,
     "item_count": item_count,
     }, timeout=TIMEOUT)
    assert r.status_code == 422
    # FIXME - the documentation does not inform the status code for this test


def test_post_new_inventory_with_an_taken_deposit():
    item_id = 190
    deposit_id = 281
    item_count = 0
    r = requests.post(url=f'{BASE_URL}/inventories.json', json={
      "item_id": item_id,
      "deposit_id": deposit_id,
      "item_count": item_count,
      }, timeout=TIMEOUT)
    assert r.status_code == 422
    # FIXME - the documentation does not inform the status code for this test


def test_patch_inventory_by_id():
    r = create_inventory_to_get_id()
    id = r.json().get('id')
    item_count = 1
    r = requests.patch(url=f'{BASE_URL}/inventories/{id}.json', json={
      "item_count": item_count
    }, timeout=TIMEOUT)
    assert r.status_code == 200
    d = requests.delete(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204


def test_patch_inventory_by_id_fail():
    id = 0
    r = requests.patch(url=f'{BASE_URL}/inventories/{id}.json', json={
      "item_count": 1
    }, timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The documentation does not inform the status code for this test


def test_patch_inventory_by_id_with_negative_item_count():
    r = create_inventory_to_get_id()
    id = r.json().get('id')
    item_count = -1
    r = requests.patch(url=f'{BASE_URL}/inventories/{id}.json', json={
      "item_count": item_count
    }, timeout=TIMEOUT)
    assert r.status_code == 200
    d = requests.delete(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - Item count should not be negative


def test_patch_inventory_by_id_with_an_taken_item():
    r = create_inventory_to_get_id()
    id = r.json().get('id')
    item_id = 199
    r = requests.patch(url=f'{BASE_URL}/inventories/{id}.json', json={
      "item_id": item_id
    }, timeout=TIMEOUT)
    assert r.status_code == 422
    # FIXME - the documentation does not inform the status code for this test


def test_patch_inventory_by_id_with_an_taken_deposit():
    r = create_inventory_to_get_id()
    id = r.json().get('id')
    deposit_id = 281
    r = requests.patch(url=f'{BASE_URL}/inventories/{id}.json', json={
      "deposit_id": deposit_id
    }, timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - the documentation does not inform the status code for this test


def test_put_inventory_by_id():
    r = create_inventory_to_get_id()
    id = r.json().get('id')
    item_id = 232
    deposit_id = 390
    item_count = 5
    r = requests.put(url=f'{BASE_URL}/inventories/{id}.json', json={
      "item_id": item_id,
      "deposit_id": deposit_id,
      "item_count": item_count
    }, timeout=TIMEOUT)
    assert r.status_code == 200
    d = requests.delete(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204


def test_put_inventory_by_id_fail():
    id = 0
    item_id = 232
    deposit_id = 364
    item_count = 5
    r = requests.put(url=f'{BASE_URL}/inventories/{id}.json', json={
      "item_id": item_id,
      "deposit_id": deposit_id,
      "item_count": item_count
    }, timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The documentation does not inform the status code for this test


def test_put_inventory_by_id_with_negative_item_count():
    r = create_inventory_to_get_id()
    id = r.json().get('id')
    item_count = -1
    r = requests.put(url=f'{BASE_URL}/inventories/{id}.json', json={
      "item_count": item_count
    }, timeout=TIMEOUT)
    assert r.status_code == 200
    d = requests.delete(url=f'{BASE_URL}/inventories/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - Item count should not be negative


def test_put_inventory_by_id_with_an_taken_item():
    r = create_inventory_to_get_id()
    id = r.json().get('id')
    item_id = 199
    r = requests.put(url=f'{BASE_URL}/inventories/{id}.json', json={
      "item_id": item_id
    }, timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - the documentation does not inform the status code for this test


def test_put_inventory_by_id_with_an_taken_deposit():
    r = create_inventory_to_get_id()
    id = r.json().get('id')
    deposit_id = 281
    r = requests.put(url=f'{BASE_URL}/inventories/{id}.json', json={
      "deposit_id": deposit_id
    }, timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - the documentation does not inform the status code for this test

