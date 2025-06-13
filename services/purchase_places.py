from werkzeug.exceptions import BadRequest

def check_nb_tickets_limit(places_required: int):
    if places_required > 12:
        raise BadRequest("Impossible to book more than 12 tickets")