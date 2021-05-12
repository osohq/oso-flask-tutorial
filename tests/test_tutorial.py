# def test_guest(test_client):


def test_user(test_client):
    resp = test_client.get("/expenses/1", headers={"user": "alice@foo.com"})
    assert resp.status_code == 200

    resp = test_client.get("/expenses/2", headers={"user": "alice@foo.com"})
    assert resp.status_code == 200
    assert resp.data.decode().startswith("Expense")
