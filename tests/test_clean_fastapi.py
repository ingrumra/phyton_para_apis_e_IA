from fastapi.testclient import TestClient
from src.app.main import app

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
    assert body["columns"] == ["edad", "ciudad", "dpto", "fec_not"]

# ya no se produce error de validación, /clean solo transforma

def test_clean_accepts_bad_age():
    payload = [{"edad": -5}]
    r = client.post("/clean", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["n"] == 1
    assert body["records"][0]["edad"] == -5


def test_clean_file(tmp_path):
    import pandas as pd
    df = pd.DataFrame([{"a": 1, "b": 2}])
    file = tmp_path / "test.csv"
    df.to_csv(file, sep=";", index=False)
    with open(file, "rb") as f:
        r = client.post("/clean-file", files={"file": ("test.csv", f, "text/csv")})
    assert r.status_code == 200
    body = r.json()
    assert "records" in body
    assert body["columns"] == ["a", "b"]