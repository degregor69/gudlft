from bs4 import BeautifulSoup


def test_to_book_more_than_12_tickets(client):
    response = client.post('/purchasePlaces', data={
        'places': 13,
        'competition': "Mock Competition",
        'club': 'Mock Club'
    })
    soup = BeautifulSoup(response.data, 'html.parser')
    assert 'Impossible to book more than 12 tickets' in soup.text
