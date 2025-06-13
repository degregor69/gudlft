def check_nb_tickets_limit(places_required: int):
    if places_required > 12:
        return False
    return True
