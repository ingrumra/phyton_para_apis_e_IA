
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_validate_ok():
    payload = {"edad": 55, "ciudad": "cali", "dpto": "valle", "fec_not": "2023-01-03"}
    r = client.post("/validate", json=payload)
    assert r.status_code == 200
    assert r.json()["edad"] == 55

def test_validate_rejects_bad_age():
    payload = {"edad": -1}
    r = client.post("/validate", json=payload)
    assert r.status_code == 422