# TFT-Stat-Tracker
This is a very simple API Project using Riot Games Developer API. It gets the match history of the requested user specifically for Teamfight Tactics (TFT) mode.

## Installation:
Prerequisites
- Python 3.8 or higher
- Flask Libary

## Usage:
- Start the backend server (flasker3.py)
- Open web browser and type localhost:5000

# API References

1. **Summoner Name API**
   - URL: `https://{fetch_region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{puuid}?api_key={API_KEY}`
   - Headers: `{"X-Riot-Token": {API_KEY}}`

2. **Summoner PUUID API**
   - URL: `https://{fetch_region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner}/{tagline}?api_key={API_KEY}`
   - Headers: `{"X-Riot-Token": {API_KEY}}`

3. **Match IDs by PUUID API**
   - URL: `https://{fetch_region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?count={count}&api_key={API_KEY}`
   - Headers: `{"X-Riot-Token": {API_KEY}}`

4. **Match Details by Match ID API**
   - URL: `https://{fetch_region}.api.riotgames.com/tft/match/v1/matches/{match_id}?api_key={API_KEY}`
   - Headers: `{"X-Riot-Token": {API_KEY}}`

5. **Match IDs by PUUID API (from `get_match_details_by_puuid`)**
   - URL: `https://{fetch_region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids`
   - Headers: `{"X-Riot-Token": {API_KEY}}`

6. **Match Details by Match ID API (from `get_match_details_by_puuid`)**
   - URL: `https://{fetch_region}.api.riotgames.com/tft/match/v1/matches/{match_id}`
   - Headers: `{"X-Riot-Token": {API_KEY}}`

