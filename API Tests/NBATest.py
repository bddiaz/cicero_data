#print('Time to test APIs!')

from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import boxscoreadvancedv2
from nba_api.stats.endpoints import leaguegamelog


import pprint as pp
import requests
import pandas

games = leaguegamelog.LeagueGameLog()
gamesDF= games.get_data_frames()[0].iloc[1249]['GAME_ID']

print(gamesDF)

lg = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id='0022300597')


lgDF = lg.get_data_frames()[0].iloc[14]

lgDict = lg.get_dict()

demarResults = lgDict['resultSets'][0]['rowSet'][12]

headers = lgDict['resultSets'][0]['headers']

DemarDict ={}

for i in range(len(headers)):
    DemarDict[headers[i]]= demarResults[i]

print(DemarDict)



'''
{'GAME_ID': '0022300597', 'TEAM_ID': 1610612741, 'TEAM_ABBREVIATION': 'CHI', 'TEAM_CITY': 'Chicago', 'PLAYER_ID': 201942, 'PLAYER_NAME': 'DeMar DeRozan', 'NICKNAME': 'DeMar', 'START_POSITION': 'F', 'COMMENT': '', 'MIN': '36.000000:36', 'E_OFF_RATING': 118.9, 'OFF_RATING': 118.4, 'E_DEF_RATING': 89.7, 'DEF_RATING': 88.2, 'E_NET_RATING': 29.2, 'NET_RATING': 30.3, 'AST_PCT': 0.286, 'AST_TOV': 8.0, 'AST_RATIO': 25.8, 'OREB_PCT': 0.026, 'DREB_PCT': 0.088, 'REB_PCT': 0.056, 'TM_TOV_PCT': 3.2, 'EFG_PCT': 0.375, 'TS_PCT': 0.414, 'USG_PCT': 0.261, 'E_USG_PCT': 0.268, 'E_PACE': 98.65, 'PACE': 99.67, 'PACE_PER40': 83.06, 'POSS': 76, 'PIE': 0.1} 

'''











# Nikola Jokić
#areer = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
#statsdf = career.get_data_frames()[0]

# Today's Score Board
#games = scoreboard.ScoreBoard()

#print(games.get_json)
# json
#games.get_json()

# dictionary
#todays = games.get_dict()
#pp.pprint(todays['scoreboard']['games'][1])

#get_active_players()

"""
            "estimatedOffensiveRating", 
            "offensiveRating", 
            "estimatedDefensiveRating", 
            "defensiveRating", 
            "estimatedNetRating", 
            "netRating", 
            "assistPercentage", 
            "assistToTurnover", 
            "assistRatio", 
            "offensiveReboundPercentage", 
            "defensiveReboundPercentage", 
            "reboundPercentage", 
            "turnoverRatio", 
            "effectiveFieldGoalPercentage", 
            "trueShootingPercentage", 
            "usagePercentage", 
            "estimatedUsagePercentage", 
            "estimatedPace", 
            "pace", 
            "pacePer40", 
            "possessions", 
"""







