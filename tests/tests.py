from .conftest import client
from bs4 import BeautifulSoup

def test_show_summary_with_mock_data(client):
    response = client.post('/showSummary', data={'email': 'mock@club.com'})
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')

    h2 = soup.find('h2')
    assert h2 is not None
    assert "mock@club.com" in h2.text

def test_to_book_more_than_12_tickets(client):
    response = client.post('/purchasePlaces', data={
        'places': 13,
        'competition': "Mock Competition",
        'club': 'Mock Club'
    })
    soup = BeautifulSoup(response.data, 'html.parser')
    assert 'Impossible to book more than 12 tickets' in soup.text
