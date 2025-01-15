import requests
from dotenv import load_dotenv
from flask import jsonify
import os

class TFTApi:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv('tft_api_key')
        self.match_id_list = []
        self.region_map = {
            'EUNE': 'europe',
            'EUW': 'europe',
            'NA': 'americas',
            'KR': 'asia'
        }

    def checkAPIkey(self):
        return self.API_KEY

    def get_region_endpoint(self, region):
        return self.region_map.get(region, 'asia')

    def get_summoner_name(self, region, puuid):
        fetch_region = self.get_region_endpoint(region)
        url = f"https://{fetch_region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{puuid}?api_key={self.API_KEY}"
        headers = {"X-Riot-Token": self.API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('gameName')
        return None

    def get_summoner_PUUID(self, region, summoner, tagline):
        fetch_region = self.get_region_endpoint(region)
        url = f"https://{fetch_region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner}/{tagline}?api_key={self.API_KEY}"
        headers = {"X-Riot-Token": self.API_KEY}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('puuid')
        return None

    def get_matchid_puuid(self, puuid, region, count=20):
        fetch_region = self.get_region_endpoint(region)
        url = f"https://{fetch_region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?count={count}&api_key={self.API_KEY}"
        headers = {"X-Riot-Token": self.API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            match_ids = response.json()
            self.match_id_list.extend(match_ids)
            return self.match_id_list
        return []

    def get_match_details(self, region, limit=5):
        fetch_region = self.get_region_endpoint(region)
        match_details = []
        for match_id in self.match_id_list[:limit]:  # Process up to 'limit' matches
            url = f"https://{fetch_region}.api.riotgames.com/tft/match/v1/matches/{match_id}?api_key={self.API_KEY}"
            headers = {"X-Riot-Token": self.API_KEY}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                match_details.append(response.json())
        return match_details
    
    def get_match_details_by_puuid(self, region, summoner, tagline):
        limit = 10
        fetch_region = self.get_region_endpoint(region)
        puuid = self.get_summoner_PUUID(fetch_region, summoner, tagline)
        
        # Fetch match IDs
        match_ids_url = f"https://{fetch_region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids"
        headers = {"X-Riot-Token": self.API_KEY}
        
        match_ids_response = requests.get(match_ids_url, headers=headers)
        
        if match_ids_response.status_code != 200:
            return {"error": "Failed to fetch match IDs", "status_code": match_ids_response.status_code}
        
        match_ids = match_ids_response.json()
        match_details = []
        
        # Fetch match details for each match ID
        for match_id in match_ids[:limit]:  # Limit to 'limit' matches
            match_url = f"https://{fetch_region}.api.riotgames.com/tft/match/v1/matches/{match_id}"
            match_response = requests.get(match_url, headers=headers)
            if match_response.status_code == 200:
                match_details.append(match_response.json())
            else:
                match_details.append({"error": f"Failed to fetch match details for match_id {match_id}", "status_code": match_response.status_code})
        
        return match_details

