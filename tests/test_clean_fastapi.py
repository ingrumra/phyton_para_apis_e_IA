from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_clean_ok():
    payload = [
        {
            "edad": 55,
            "ciudad": "cali",
            "dpto": "valle",
            "fec_not": "2023-01-03"
        }
    ]
    r = client.post("/clean", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["n"] == 1
    assert "records" in body

def test_clean_validation_error():
    # edad negativa viola el schema (ge=0)
    payload = [{"edad": -5}]
    r = client.post("/clean", json=payload)
    assert r.status_code == 422