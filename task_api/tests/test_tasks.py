from fastapi.testclient import TestClient
import main

client = TestClient(main.app)

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

def test_delete_task():
    # Cria uma tarefa para depois deletar
    response_create = client.post(
        "/tasks/",
        json={"title": "Tarefa a deletar", "description": "Será removida"}
    )
    assert response_create.status_code == 200
    task_id = response_create.json()["id"]

    # Deleta a tarefa criada
    response_delete = client.delete(f"/tasks/{task_id}")
    assert response_delete.status_code == 200
    assert response_delete.json()["message"] == "Tarefa deletada com sucesso"

    # Verifica que ela não existe mais
    response_delete_again = client.delete(f"/tasks/{task_id}")
    assert response_delete_again.status_code == 404
    assert response_delete_again.json()["detail"] == "Tarefa não encontrada"

def test_update_task():
    # Criar uma tarefa inicial
    response_create = client.post(
        "/tasks/",
        json={"title": "Tarefa antiga", "description": "Descrição antiga"}
    )
    assert response_create.status_code == 200
    task_id = response_create.json()["id"]

    # Atualizar a tarefa criada
    response_update = client.put(
        f"/tasks/{task_id}",
        json={"title": "Tarefa atualizada", "description": "Nova descrição"}
    )
    assert response_update.status_code == 200
    updated_data = response_update.json()
    assert updated_data["title"] == "Tarefa atualizada"
    assert updated_data["description"] == "Nova descrição"

    # Testar atualização de uma tarefa inexistente
    response_update_not_found = client.put(
        "/tasks/999",
        json={"title": "Teste", "description": "Teste"}
    )
    assert response_update_not_found.status_code == 404
    assert response_update_not_found.json()["detail"] == "Tarefa não encontrada"


