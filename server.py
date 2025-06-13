import json
from flask import Flask, render_template, request, redirect, flash, url_for, abort
from datetime import datetime
from services.purchase_places import check_nb_tickets_limit

app = Flask(__name__)
app.secret_key = 'something_special'


def load_clubs():
    with open('clubs.json') as c:
        return json.load(c)['clubs']


def load_competitions():
    with open('competitions.json') as comps:
        return json.load(comps)['competitions']


clubs = load_clubs()
competitions = load_competitions()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/book/<competition>/<club>')
def book(competition,club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html',club=found_club,competition=found_competition)
    else:
        flash("Something went wrong – please try again.")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])

    if not check_nb_tickets_limit(places_required):
        flash("Impossible to book more than 12 tickets")
        return render_template('welcome.html', club=club, competitions=competitions)

    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-places_required
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
