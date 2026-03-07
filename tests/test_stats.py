from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)

def test_stats_route():
    response = client.get("/api/v1/stats")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Si tiene contenido, comprobar estructura mínima
    if data:
        assert "comuna" in data[0]
        assert "cantidad" in data[0]
