import pytest


def test_root(client):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["status"] == "running"


def test_healthcheck(client):
    """Test healthcheck endpoint."""
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_time(client):
    """Test time endpoint."""
    response = client.get("/time")
    assert response.status_code == 200
    assert "server_time" in response.json()


def test_sentry_debug_triggers_error(client):
    """Test that sentry-debug endpoint triggers ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        client.get("/sentry-debug")
