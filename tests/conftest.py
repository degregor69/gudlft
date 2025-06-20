import pytest
import server


@pytest.fixture
def test_clubs():
    return [
        {"name": "Test Club", "email": "test@club.com", "points": "30"},
    ]

@pytest.fixture
def test_competitions():
    return [
        {"name": "Test Competition", "date": "2025-12-31 10:00:00", "numberOfPlaces": "25"},
    ]

@pytest.fixture
def client(monkeypatch, test_clubs, test_competitions):
    monkeypatch.setattr(server, "clubs", test_clubs)
    monkeypatch.setattr(server, "competitions", test_competitions)

    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client
