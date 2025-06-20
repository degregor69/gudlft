import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def test_competitions():
    return [
        {"name": "Test Competition", "date": "2024-12-31 10:00:00", "numberOfPlaces": "25"},
    ]

def test_show_summary_with_event_in_the_past(client):
    response = client.post('/showSummary', data={'email': 'test@club.com'})
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, 'html.parser')
    li = soup.find('li')

    assert li is not None
    assert "L'événement n'est plus disponible." in li.text
