from fastapi.testclient import TestClient

from st4r.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_task_lifecycle():
    response = client.post("/tasks", json={"title": "Write a report", "course": "Management"})
    assert response.status_code == 201
    task = response.json()
    assert task["status"] == "todo"
    assert task["title"] == "Write a report"

    listed = client.get("/tasks")
    assert listed.status_code == 200
    assert any(item["id"] == task["id"] for item in listed.json())

    finished = client.patch(f"/tasks/{task['id']}/complete")
    assert finished.status_code == 200
    assert finished.json()["status"] == "done"

    assert client.delete(f"/tasks/{task['id']}").status_code == 204
    assert client.patch(f"/tasks/{task['id']}/complete").status_code == 404


def test_validation():
    assert client.post("/tasks", json={"title": ""}).status_code == 422
