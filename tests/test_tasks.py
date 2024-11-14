import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession
from app import app
from app.dependencies import get_async_db
from app.schemas.task import CreateTaskRequest


@pytest.fixture
def client():
    return AsyncClient(transport=ASGITransport(app=app), base_url="http://test")


@pytest.mark.asyncio
async def test_create_task(client: AsyncClient):
    request_data = {
        "title": "Test Task",
        "description": "This is a test task description"
    }
    response = await client.post("/tasks", json=request_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["data"]["title"] == request_data["title"]
    assert response_data["data"]["description"] == request_data["description"]


@pytest.mark.asyncio
async def test_create_task_with_invalid_data(client: AsyncClient):
    # Test with missing title field
    request_data = {
        "description": "This is a test task description"
    }
    response = await client.post("/tasks", json=request_data)
    print(response.json())
    assert response.status_code == 400
    response_data = response.json()
    assert response_data["message"] == "Fill in the required fields."


@pytest.mark.asyncio
async def test_get_all_tasks(client: AsyncClient):
    response = await client.get("/tasks")
    assert response.status_code == 200
    response_data = response.json()
    assert "data" in response_data
    assert isinstance(response_data["data"], list)


@pytest.mark.asyncio
async def test_get_task_by_id(client: AsyncClient):
    task_id = 1
    response = await client.get(f"/tasks/{task_id}")
    if response.status_code == 200:
        response_data = response.json()
        assert "data" in response_data
        assert response_data["data"]["id"] == task_id
    elif response.status_code == 404:
        assert response.json()["detail"] == "Task not found"


@pytest.mark.asyncio
async def test_get_task_by_id_not_found(client: AsyncClient):
    # Test with a non-existent task ID
    task_id = -1
    response = await client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


@pytest.mark.asyncio
async def test_update_task(client: AsyncClient):
    task_id = 1
    update_data = {
        "title": "Updated Task Title",
        "description": "Updated description for the task"
    }
    response = await client.put(f"/tasks/{task_id}", json=update_data)
    if response.status_code == 200:
        response_data = response.json()
        assert response_data["data"]["title"] == update_data["title"]
    elif response.status_code == 404:
        assert response.json()["detail"] == "Task not found"


@pytest.mark.asyncio
async def test_delete_task(client: AsyncClient):
    task_id = 1  # Replace with an actual ID in your test environment
    response = await client.delete(f"/tasks/{task_id}")
    if response.status_code == 200:
        response_data = response.json()
        assert response_data["data"]["id"] == task_id
    elif response.status_code == 404:
        assert response.json()["detail"] == "Task not found"


@pytest.mark.asyncio
async def test_partial_update_task(client: AsyncClient):
    task_id = 1
    partial_update_data = {
        "title": "Partially Updated Task Title"
    }
    response = await client.patch(f"/tasks/{task_id}", json=partial_update_data)
    if response.status_code == 200:
        response_data = response.json()
        assert response_data["data"]["title"] == partial_update_data["title"]
    elif response.status_code == 404:
        assert response.json()["detail"] == "Task not found"
