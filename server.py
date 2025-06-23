import json
from flask import Flask, render_template, request, redirect, flash, url_for, abort
from datetime import datetime

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

if not clubs:
    clubs = load_clubs()
if not competitions:
    competitions = load_competitions()


def get_clubs():
    return clubs

def get_competitions():
    return competitions

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    print(clubs)
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
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-places_required
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
