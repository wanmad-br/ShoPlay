from app import app


def test_catalog_contains_fantasy_items():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    html = response.get_data(as_text=True).lower()
    assert 'sword' in html or 'cape' in html
    assert 'fantasy' in html.lower() or 'shop' in html.lower()


def test_purchase_endpoint_simulates_transaction():
    client = app.test_client()
    response = client.post('/api/purchase', json={
        'item_id': 1,
        'quantity': 2,
    })

    assert response.status_code == 200
    payload = response.get_json()
    assert payload['status'] == 'success'
    assert payload['item']['name']
    assert payload['total'] > 0
    assert payload['receipt']['quantity'] == 2
