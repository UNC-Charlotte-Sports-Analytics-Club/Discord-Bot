import os 
import discord
from discord.ext import commands 
import logging
import requests 

#setup logging 
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=getattr(logging, LOG_LEVEL))
LOGGER = logging.getLogger(__name__)

TEAM_ID = int(os.getenv("TEAM_ID", "0"))

class EspnEndpoints:
    @staticmethod 
    def schedule(year, week):
        url = f"http://cdn.espn.com/core/nfl/schedule?xhr=1&year={year}&week={week}"
        LOGGER.debug(f"Requesting: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            LOGGER.error(f"Failed to fetch schedule: {response.status_code}")
            return None
    
    @staticmethod
    def scoreboard(limit=50):
        url = f"https://cdn.espn.com/core/nfl/scoreboard?xhr=1&limit={limit}"
        LOGGER.debug(f"Requesting: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError as e:
                LOGGER.error(f"Failed to parse JSON: {e}")
                return None
        else: 
            LOGGER.error(f"Failed to fetch scoreboard: {response.status_code}")
            return None

    @staticmethod 
    def extractGames(scoreboard_json):
        games = []
        try:
            # Events are directly inside the root JSON, under 'events'
            events = scoreboard_json.get("events", [])
            for event in events: 
                competition = event.get("competitions", [{}])[0]
                competitors = competition.get("competitors", [])
                
                # Identify home and away teams
                home_team = next((c for c in competitors if c.get("homeAway") == "home"), None)
                away_team = next((c for c in competitors if c.get("homeAway") == "away"), None)
                
                if home_team and away_team:
                    home_name = home_team.get("team", {}).get("shortDisplayName", "Unknown")
                    away_name = away_team.get("team", {}).get("shortDisplayName", "Unknown")
                    
                    home_score = home_team.get("score", "0")
                    away_score = away_team.get("score", "0")
                    
                    status = event.get("status", {}).get("type", {}).get("shortDetail", "Status Unknown")

                    games.append({
                        "home" : home_name,
                        "away" : away_name,
                        "score_home" : home_score,
                        "score_away" : away_score,
                        "status" : status,
                    })
                
        except Exception as e:
            LOGGER.error(f"Error parsing scoreboard data: {e}")

        return games


if __name__ == "__main__":
    scoreboard = EspnEndpoints.scoreboard()
    if scoreboard:
        games = EspnEndpoints.extractGames(scoreboard)
        for game in games:
            print(f"{game['home']} vs {game['away']} | {game['score_home']}-{game['score_away']} | {game['status']}")
    else:
        LOGGER.error("No scoreboard data retrieved.")




