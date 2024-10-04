from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)
data = pd.read_csv('imdb_data.csv')

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/main', methods=['GET', 'POST'])
def home():
    genre_filter = request.args.get('genre')
    actor_filter = request.args.get('actor')
    director_filter = request.args.get('director')

    filtered_data = data

    if genre_filter:
        filtered_data = filtered_data[filtered_data['Genre'].str.contains(genre_filter, case=False, na=False)]

    if actor_filter:
        filtered_data = filtered_data[filtered_data['Actors'].str.contains(actor_filter, case=False, na=False)]

    if director_filter:
        filtered_data = filtered_data[filtered_data['Director'].str.contains(director_filter, case=False, na=False)]

    return render_template('index.html', movies=filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
