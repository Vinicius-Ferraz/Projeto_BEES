import requests

BASE_URL = "https://test-bees.herokuapp.com"
TIMEOUT = 3


def create_item_to_get_id():
    name = "Get ID"
    height = 10.0
    width = 10.0
    weight = 10.0
    create = requests.post(url=f'{BASE_URL}/items.json', json={
      "name": name,
      "height": height,
      "width": width,
      "weight": weight
     }, timeout=TIMEOUT)
    id = create.json().get('id')
    return create


def test_get_successful():
    r = requests.get(url=f'{BASE_URL}/items.json', timeout=TIMEOUT)
    assert r.status_code == 200


def test_get_item_by_id():
    r = create_item_to_get_id()
    id = r.json().get('id')
    requests.get(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 201
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201


def test_get_item_by_id_fail():
    id = 0
    r = requests.get(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The documentation does not inform the status code for this test


def test_post_new_item():
    name = "Post test"
    height = 10.0
    width = 10.0
    weight = 10.0
    r = requests.post(url=f'{BASE_URL}/items.json', json={
      "name": name,
      "height": height,
      "width": width,
      "weight": weight
     }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201
    # FIXME - This API does not have a field to be required


def test_post_new_item_without_name():
    height = 10.1
    width = 10.1
    weight = 10.1
    r = requests.post(url=f'{BASE_URL}/items.json', json={
      "height": height,
      "width": width,
      "weight": weight
     }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201


def test_post_new_item_without_height():
    name = "Post test no height"
    width = 10.1
    weight = 10.1
    r = requests.post(url=f'{BASE_URL}/items.json', json={
      "name": name,
      "width": width,
      "weight": weight
     }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201


def test_post_new_item_without_width():
    name = "Post test no width"
    height = 10.1
    weight = 10.1
    r = requests.post(url=f'{BASE_URL}/items.json', json={
      "name": name,
      "height": height,
      "weight": weight
     }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201


def test_post_new_item_without_weight():
    name = "Post test no weight"
    height = 10.1
    width = 10.1
    r = requests.post(url=f'{BASE_URL}/items.json', json={
      "name": name,
      "height": height,
      "width": width
     }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201


def test_post_new_item_with_negative_dimension():
    name = "Post test negative dimension"
    height = -10.0
    width = -10.0
    weight = -10.0
    r = requests.post(url=f'{BASE_URL}/items.json', json={
        "name": name,
        "height": height,
        "width": width,
        "weight": weight
    }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201


def test_post_new_tem_with_blank_fields():
    name = ""
    height = ''
    width = ''
    weight = ''
    r = requests.post(url=f'{BASE_URL}/items.json', json={
        "name": name,
        "height": height,
        "width": width,
        "weight": weight
    }, timeout=TIMEOUT)
    assert r.status_code == 201
    id = r.json().get('id')
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201
    # FIXME - This API does not have a field to be required


def test_patch_item_by_id():
    c = create_item_to_get_id()
    id = c.json().get('id')
    weight = 1000.0
    r = requests.patch(url=f'{BASE_URL}/items/{id}.json', json={
      "weight": weight
     }, timeout=TIMEOUT)
    assert r.status_code == 200
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204


def test_patch_item_by_id_fail():
    id = 0
    r = requests.patch(url=f'{BASE_URL}/items/{id}.json', json={
      "weight": 1000.0
     }, timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The documentation does not inform the status code for this test


def test_put_item_by_id():
    c = create_item_to_get_id()
    id = c.json().get('id')
    name = "put but delete"
    height = 10.0
    width = 10.0
    weight = 10.0
    r = requests.put(url=f'{BASE_URL}/items/{id}.json', json={
      "name": name,
      "height": height,
      "width": width,
      "weight": weight
     }, timeout=TIMEOUT)
    assert r.status_code == 200
    d = requests.delete(url=f'{BASE_URL}/items/{id}.json', timeout=TIMEOUT)
    assert d.status_code == 204
    # FIXME - The status code informed at the documentation is 200, but the API is returning 201


def test_put_item_by_id_fail():
    id = 0
    name = "put but delete"
    height = 10.0
    width = 10.0
    weight = 10.0
    r = requests.put(url=f'{BASE_URL}/items/{id}.json', json={
      "name": name,
      "height": height,
      "width": width,
      "weight": weight
     }, timeout=TIMEOUT)
    assert r.status_code == 404
    # FIXME - The documentation does not inform the status code for this test
