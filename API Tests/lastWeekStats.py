from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import boxscoreadvancedv2
from nba_api.stats.endpoints import leaguegamelog
from nba_api.stats.endpoints import playergamelogs


import pprint as pp
import requests
import pandas


'''
With a list of known players and IDs, search for the stats of the last week's games
Headers: 
['SEASON_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS', 'VIDEO_AVAILABLE']
Players: 
{'first_name': 'Victor',
  'full_name': 'Victor Wembanyama',
  'id': 1641705,
  'is_active': True,
  'last_name': 'Wembanyama'},
{'first_name': 'Jayson',
  'full_name': 'Jayson Tatum',
  'id': 1628369,
  'is_active': True,
  'last_name': 'Tatum'},
{'first_name': 'Karl-Anthony',
  'full_name': 'Karl-Anthony Towns',
  'id': 1626157,
  'is_active': True,
  'last_name': 'Towns'},
{'first_name': 'Giannis',
  'full_name': 'Giannis Antetokounmpo',
  'id': 203507,
  'is_active': True,
  'last_name': 'Antetokounmpo'},
{'first_name': 'Jimmy',
  'full_name': 'Jimmy Butler',
  'id': 202710,
  'is_active': True,
  'last_name': 'Butler'},
{'first_name': 'Luka',
  'full_name': 'Luka Doncic',
  'id': 1629029,
  'is_active': True,
  'last_name': 'Doncic'},
  {'first_name': 'Kevin',
  'full_name': 'Kevin Durant',
  'id': 201142,
  'is_active': True,
  'last_name': 'Durant'},
 {'first_name': 'Shai',
  'full_name': 'Shai Gilgeous-Alexander',
  'id': 1628983,
  'is_active': True,
  'last_name': 'Gilgeous-Alexander'},
{'first_name': 'LeBron',
  'full_name': 'LeBron James',
  'id': 2544,
  'is_active': True,
  'last_name': 'James'},
{'first_name': 'Nikola',
  'full_name': 'Nikola Jokic',
  'id': 203999,
  'is_active': True,
  'last_name': 'Jokic'},

'''



playersList=[
{'first_name': 'Karl-Anthony',
  'full_name': 'Karl-Anthony Towns',
  'id': 1626157},
{'first_name': 'Giannis',
  'full_name': 'Giannis Antetokounmpo',
  'id': 203507},
{'first_name': 'Jimmy',
  'full_name': 'Jimmy Butler',
  'id': 202710},
  {'first_name': 'Kevin',
  'full_name': 'Kevin Durant',
  'id': 201142},
{'first_name': 'LeBron',
  'full_name': 'LeBron James',
  'id': 2544},
{'first_name': 'Nikola',
  'full_name': 'Nikola Jokic',
  'id': 203999}
]

#game id spot = 7
def searchLastNGames(ID,n):
    lastGames = playergamelogs.PlayerGameLogs(last_n_games_nullable=5, player_id_nullable=ID) 
    DF = lastGames.get_data_frames()
    print(DF)
    last5IDs=[]

    for j in range(5):
        lg = lastGames.get_dict()['resultSets'][0]['rowSet'][j][7]
        print('curently on player id: '+str(ID) +' on game number '+ str(j))
        print(lg)
        last5IDs.append(lg)
    playersList[n]['last5IDs']= last5IDs


for i in range(len(playersList)):
    searchLastNGames(playersList[i]['id'],i)


#print(playersList)