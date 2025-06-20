import pytest
import server


@pytest.fixture
def test_clubs(monkeypatch):
    test_clubs = [
        {"name": "Test Club", "email": "test@club.com", "points": "30"},
    ]
    monkeypatch.setattr(server, "clubs", test_clubs)
    return test_clubs

@pytest.fixture
def test_competitions(monkeypatch):
    test_competitions = [
        {"name": "Test Competition", "date": "2025-12-31 10:00:00", "numberOfPlaces": "25"},
    ]
    monkeypatch.setattr(server, "competitions", test_competitions)
    return test_competitions

@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client
