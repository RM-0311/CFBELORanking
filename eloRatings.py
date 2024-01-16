import cfbd
import datetime
import numpy as np
import pandas as pd

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'VqztL88l78/b6EKPDlVIANwQxm+dHUguGb2nlln3qWLdpJNT+4OAhJIsS1r1Lolj'
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_config = cfbd.ApiClient(configuration)
games_api = cfbd.GamesApi(cfbd.ApiClient(configuration))

def get_expected_score(rating, opp_rating):
    exp = (opp_rating - rating) / 400
    return 1 / (1 + 10**exp)

def get_new_elos(home_rating, away_rating, margin):
    k = 25

    #tie
    home_score = 0.5
    if margin > 0:
        # score of 1 for win
        home_score = 1
    elif margin < 0:
        # score of 0 for loss
        home_score = 0

    # get expected home score
    expected_home_score = get_expected_score(home_rating, away_rating)
    # multiply difference of actual and expected
    new_home_score = home_rating + k * (home_score - expected_home_score)

    # repeat these steps for the away team
    # away score is inverse of home score
    away_score = 1 - home_score
    expected_away_score = get_expected_score(away_rating, home_rating)
    new_away_score = away_rating + k * (away_score - expected_away_score)

    return (round(new_home_score), round(new_away_score))

def date_sort(game):
    game_date = datetime.datetime.strptime(game['start_date'], "%Y-%m-%dT%H:%M:%S.000Z")
    return game_date

def elo_sort(team):
    return team[]