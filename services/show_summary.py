from datetime import datetime


def enrich_competitions_with_future_flag(competitions):
    now = datetime.now()
    for comp in competitions:
        comp_date = datetime.strptime(comp['date'], "%Y-%m-%d %H:%M:%S")
        comp['is_future'] = comp_date > now
    return competitions