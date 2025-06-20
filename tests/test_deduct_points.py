def test_deduct_6_tickets(client, test_clubs):
    test_club = test_clubs[0]
    old_points = int(test_club.get("points"))
    response = client.post('/purchasePlaces', data={
        'places': 6,
        'competition': "Test Competition",
        'club': 'Test Club'
    })

    assert response.status_code == 200

    test_club = test_clubs[0]
    assert int(test_club.get("points")) == old_points - 6
