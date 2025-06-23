from .conftest import client
from bs4 import BeautifulSoup

def test_show_summary_with_mock_data(client):
    response = client.post('/showSummary', data={'email': 'mock@club.com'})
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')

    h2 = soup.find('h2')
    assert h2 is not None
    assert "mock@club.com" in h2.text

