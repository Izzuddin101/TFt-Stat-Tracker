from flask import Flask, request, render_template, redirect, url_for, jsonify, Response
import tft_api

app = Flask(__name__)
api = tft_api.TFTApi()

@app.route('/')
def main_page():
    return render_template('main_page_copy.html')  # Matches updated HTML structure

@app.route('/stats_viewer', methods=['GET'])
def stats_viewer():
    return redirect(url_for('main_page'))  # Redirect to main page for now

@app.route('/teambuilder', methods=['GET'])
def team_builder():
    return "Team Builder page under development!"
  
@app.route('/player', methods=['GET'])
@app.route('/player/<summoner>_<tagline>/<region>', methods=['GET'])
def displayResult(summoner=None, tagline=None, region=None):
    # Access URL path variables instead of query parameters
    region = request.args.get('region')  # Get region from URL path
    summoner = request.args.get('summoner')  # Get summoner from URL path
    tagline = request.args.get('tagline')  # Get tagline from URL path
    puuid = api.get_summoner_PUUID(region, summoner, tagline)
    
    print(region, summoner, tagline)

    return render_template('playerStats.html', region=region,
                           summoner=summoner,
                           tagline=tagline,
                           puuid=puuid)


@app.route('/api/match_details/<summoner>_<tagline>/<region>', methods=["GET"])
def getMatchDetails(summoner, tagline, region):
    
    print(region, tagline, summoner)
    
    match_history = api.get_match_details_by_puuid(region=region, summoner=summoner, tagline=tagline)
    return jsonify(match_history)

@app.route('/api/player_details/<summoner>_<tagline>/<region>', methods=['GET'])
def getPlayerDetails(summoner, tagline, region):
    region = request.args.get('region')
    summoner = request.args.get('summoner')
    tagline = request.args.get('tagline')
    puuid = api.get_summoner_PUUID(region, summoner, tagline)
    
    # Create a dictionary with all the details
    player_details = {
        "puuid": puuid,
        "region": region,
        "summoner": summoner,
        "tagline": tagline
    }
    
    # Return the details as a JSON response
    return jsonify(player_details)

if __name__ == '__main__':
    app.run(debug=True)
