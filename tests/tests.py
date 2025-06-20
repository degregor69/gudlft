import pytest

from .conftest import client
from bs4 import BeautifulSoup

def test_show_summary_with_mock_data(client, test_clubs, test_competitions):
    response = client.post('/showSummary', data={'email': 'test@club.com'})
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')

    assert "test@club.com" in soup.text

