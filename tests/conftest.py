
import pytest
import server

@pytest.fixture
def client(monkeypatch):
    test_clubs = [
        {"name": "Mock Club", "email": "mock@club.com", "points": "15"}
    ]
    test_competitions = [
        {"name": "Mock Competition", "date": "2025-12-12 10:00:00", "numberOfPlaces": "20"}
    ]
    monkeypatch.setattr(server, "clubs", test_clubs)
    monkeypatch.setattr(server, "competitions", test_competitions)

    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client
