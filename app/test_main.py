from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


def test_get_or_create_short_link_pass():
    response = client.post(
        "/short_link/", json={"long_link": "string", "expiration_date": "3"}
    )
    assert response.status_code == 200
    assert response.json() == {"short_link": "Mw"}


def test_get_or_create_short_link_default():
    response = client.post("/short_link/", json={"long_link": "link"})
    assert response.status_code == 200
    assert response.json() == {"short_link": "NA"}


def test_redirect_long_link_pass():
    pass


def test_redirect_long_link_fail():
    pass
