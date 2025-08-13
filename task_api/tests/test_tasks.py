from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/tasks/",
        json={"title": "Nova tarefa", "description": "Descrição da tarefa"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == "Nova tarefa"
    assert data["description"] == "Descrição da tarefa"

def test_create_task_without_description():
    response = client.post(
        "/tasks/",
        json={"title": "Tarefa sem descrição"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Tarefa sem descrição"
    assert data["description"] is None
