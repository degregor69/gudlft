import json
from flask import Flask, render_template, request, redirect, flash, url_for
from services.purchase_places import check_nb_tickets_limit
from services.show_summary import enrich_competitions_with_future_flag

app = Flask(__name__)
app.secret_key = 'something_special'

clubs = []
competitions = []


def load_clubs():
    with open('clubs.json') as c:
        return json.load(c)['clubs']

def load_competitions():
    with open('competitions.json') as comps:
        return json.load(comps)['competitions']


def init_data():
    global clubs, competitions
    clubs = load_clubs()
    competitions = load_competitions()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary', methods=['POST'])
def show_summary():
    club = [club for club in clubs if club['email'] == request.form['email']]
    club = club[0]
    enriched_comps = enrich_competitions_with_future_flag(competitions)
    return render_template('welcome.html', club=club, competitions=enriched_comps)

@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong – please try again.")
        enriched_comps = enrich_competitions_with_future_flag(competitions)
        return render_template('welcome.html', club=club, competitions=enriched_comps)

@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])

    if not check_nb_tickets_limit(places_required):
        flash('Impossible to book more than 12 tickets')
        enriched_comps = enrich_competitions_with_future_flag(competitions)
        return render_template('welcome.html', club=club, competitions=enriched_comps)

    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    club['points'] = str(int(club['points']) - places_required)

    flash('Great-booking complete!')
    enriched_comps = enrich_competitions_with_future_flag(competitions)
    return render_template('welcome.html', club=club, competitions=enriched_comps)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_data()
    app.run()
