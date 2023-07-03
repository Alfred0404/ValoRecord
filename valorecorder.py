import os
import valorant
from valorant.query import exp
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")

client = valorant.Client(API_KEY, locale=None)


lb = client.get_leaderboard(size=200)

players_list = lb.players.get_all(gameName=lambda x: x.startswith('NRG'))

print(players_list[0].gameName, players_list[0].leaderboardRank, players_list[0].rankedRating, players_list[0].numberOfWins)