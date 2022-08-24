import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import sys

def pull(position, yearinput, weekinput):
    if position == 'QB':
        df = pd.DataFrame(columns=['Year',
                                   'Week',
                                   'Position',
                                   'Rank',
                                   'Player',
                                   'Passing Completions',
                                   'Passing Attempts',
                                   'Passing Completion Percentage',
                                   'Passing Yards',
                                   'Yards per Attempt',
                                   'Touchdowns',
                                   'Interceptions',
                                   'Sacks taken',
                                   'Rushing Attempts',
                                   'Rushing Yards',
                                   'Rushing Touchdowns',
                                   'Flags',
                                   'Games played',
                                   'Fantasy Points',
                                   'Fantasy Points per Week',
                                   'Rostered Percentage'])
    # Downloading contents of the web page
        url = "https://www.fantasypros.com/nfl/stats/qb.php?year={yearinput}&week={weekinput}&scoring=PPR&roster=e&range=week".format(yearinput=str(yearinput),weekinput=str(weekinput))
        data = requests.get(url).text
        # Creating BeautifulSoup object
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find(class_='mobile-table double-header')
        # Collecting Ddata
        for row in table.tbody.find_all('tr'):
            # Find all data for each column
            columns = row.find_all('td')
            if(columns != []):
                rank = columns[0].text.strip()
                player = columns[1].text.strip()
                passing_completions = columns[2].text.strip()
                passing_attempts = columns[3].text.strip()
                passing_completion_percentage = columns[4].text.strip()
                passing_yards = columns[5].text.strip()
                passing_yards_per_attempt = columns[6].text.strip()
                passing_touchdowns = columns[7].text.strip()
                interceptions = columns[8].text.strip()
                sacks_taken = columns[9].text.strip()
                rushing_attempts = columns[10].text.strip()
                rushing_yards = columns[11].text.strip()
                rushing_touchdowns = columns[12].text.strip()
                flags = columns[13].text.strip()
                games_played = columns[14].text.strip()
                fantasy_points = columns[15].text.strip()
                fantasy_points_per_week = columns[16].text.strip()
                rostered_percentage = columns[17].text.strip()
                df = df.append({'Year':yearinput,
                                'Week':weekinput,
                                'Position':'QB',
                                'Rank':rank,
                                'Player':player,
                                'Passing Completions':passing_completions,
                                'Passing Attempts':passing_attempts,
                                'Passing Completion Percentage':passing_completion_percentage,
                                'Passing Yards':passing_yards,
                                'Yards per Attempt':passing_yards_per_attempt,
                                'Touchdowns':passing_touchdowns,
                                'Interceptions':interceptions,
                                'Sacks taken':sacks_taken,
                                'Rushing Attempts':rushing_attempts,
                                'Rushing Yards':rushing_yards,
                                'Rushing Touchdowns':rushing_touchdowns,
                                'Flags':flags,"Games played":games_played,
                                'Fantasy Points':fantasy_points,
                                'Fantasy Points per Week':fantasy_points_per_week,
                                'Rostered Percentage':rostered_percentage}, ignore_index=True)
        df['Player']= df['Player'].str.replace(')','')
        df['Player']=df['Player'].str.split(' \(',1,expand=True)[0]
        df['Player'] = df['Player'].str.replace('[^\w\s]','')
        df['Player'] = df['Player'].str.replace('III','')
        df['Player'] = df['Player'].str.replace('II','')
        df['Player'] = df['Player'].str.replace('IV','')
        df.to_csv(input('Type file name here:')+'.csv',index=False)
        print("File saved in folder")
    elif position == 'RB':
        df = pd.DataFrame(columns=['Year',
                                    'Week',
                                    'Position',
                                    'Rank','Player',
                                    'Rushing Attempts',
                                    'Rushing Yards',
                                    'Yards per Rush',
                                    'Runs >20 Yards',
                                    'Rushing Touchdowns',
                                    'Receptions','Targets',
                                    'Receiving Yards',
                                    'Yards per Reception',
                                    'Receiving Touchdowns',
                                    'Flags',
                                    'Games played',
                                    'Fantasy Points',
                                    'Fantasy Points per Week',
                                    'Rostered Percentage'])
    # Downloading contents of the web page
        url = "https://www.fantasypros.com/nfl/stats/rb.php?year={yearinput}&week={weekinput}&scoring=PPR&roster=e&range=week".format(yearinput=str(yearinput),weekinput=str(weekinput))
        data = requests.get(url).text
        # Creating BeautifulSoup object
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find(class_='mobile-table double-header')
        # Collecting Ddata
        for row in table.tbody.find_all('tr'):
            # Find all data for each column
            columns = row.find_all('td')
            if(columns != []):
                rank = columns[0].text.strip()
                player = columns[1].text.strip()
                rushing_attempts = columns[2].text.strip()
                rushing_yards = columns[3].text.strip()
                yards_per_rush = columns[4].text.strip()
                runs_over_20 = columns[5].text.strip()
                rushing_touchdowns = columns[6].text.strip()
                receptions = columns[7].text.strip()
                targets = columns[8].text.strip()
                receiving_yards = columns[9].text.strip()
                yards_per_reception = columns[10].text.strip()
                receiving_touchdowns = columns[11].text.strip()
                flags = columns[12].text.strip()
                games_played = columns[13].text.strip()
                fantasy_points = columns[14].text.strip()
                fantasy_points_per_week = columns[15].text.strip()
                rostered_percentage = columns[16].text.strip()
                df = df.append({'Year':yearinput,
                                'Week':weekinput,
                                'Position':'RB',
                                'Rank':rank,
                                'Player':player,
                                'Rushing Attempts':rushing_attempts,
                                'Rushing Yards':rushing_yards,
                                'Yards per Rush':yards_per_rush,
                                'Runs >20 yards':runs_over_20,
                                'Rushing Touchdowns':rushing_touchdowns,
                                'Receptions':receptions,
                                'Targets':targets,
                                'Receiving Yards':receiving_yards,
                                'Yards per Reception':yards_per_reception,
                                'Receiving Touchdowns':receiving_touchdowns,
                                'Flags':flags,"Games played":games_played,
                                'Fantasy Points':fantasy_points,
                                'Fantasy Points per Week':fantasy_points_per_week,
                                'Rostered Percentage':rostered_percentage}, ignore_index=True)
        df['Player']= df['Player'].str.replace(')','')
        df['Player']=df['Player'].str.split(' \(',1,expand=True)[0]
        df['Player'] = df['Player'].str.replace('[^\w\s]','')
        df['Player'] = df['Player'].str.replace('III','')
        df['Player'] = df['Player'].str.replace('II','')
        df['Player'] = df['Player'].str.replace('IV','')
        df.to_csv(input('Type file name here:')+'.csv',index=False)
        print("File saved in folder")
    elif position == 'WR':
        df = pd.DataFrame(columns=['Year',
                                    'Week',
                                    'Position',
                                    'Rank',
                                    'Player',
                                    'Receptions',
                                    'Targets',
                                    'Receiving Yards',
                                    'Yards per Reception',
                                    'Longest Reception',
                                    'Catches >20 Yards',
                                    'Receiving Touchdowns',
                                    'Rushing Attempts',
                                    'Rushing Yards',
                                    'Rushing Touchdowns',
                                    'Flags',
                                    'Games played',
                                    'Fantasy Points',
                                    'Fantasy Points per Week',
                                    'Rostered Percentage'])
    # Downloading contents of the web page
        url = "https://www.fantasypros.com/nfl/stats/wr.php?year={yearinput}&week={weekinput}&scoring=PPR&roster=e&range=week".format(yearinput=str(yearinput),weekinput=str(weekinput))
        data = requests.get(url).text
        # Creating BeautifulSoup object
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find(class_='mobile-table double-header')
        # Collecting Ddata
        for row in table.tbody.find_all('tr'):
            # Find all data for each column
            columns = row.find_all('td')
            if(columns != []):
                rank = columns[0].text.strip()
                player = columns[1].text.strip()
                receptions = columns[2].text.strip()
                targets = columns[3].text.strip()
                receiving_yards = columns[4].text.strip()
                yards_per_reception = columns[5].text.strip()
                longest_catch= columns[6].text.strip()
                catches_over_20 = columns[7].text.strip()
                receiving_touchdowns = columns[8].text.strip()
                rushing_attempts = columns[9].text.strip()
                rushing_yards = columns[10].text.strip()
                rushing_touchdowns = columns[11].text.strip()
                flags = columns[12].text.strip()
                games_played = columns[13].text.strip()
                fantasy_points = columns[14].text.strip()
                fantasy_points_per_week = columns[15].text.strip()
                rostered_percentage = columns[16].text.strip()
                df = df.append({'Year':yearinput,
                                'Week':weekinput,
                                'Position':'WR',
                                'Rank':rank,
                                'Player':player,
                                'Receptions':receptions,
                                'Targets':targets,
                                'Receiving Yards':receiving_yards,
                                'Yards per Reception':yards_per_reception,
                                'Longest Catch':longest_catch,
                                'Catches > 20 Yards':catches_over_20,
                                'Receiving Touchdowns':receiving_touchdowns,
                                'Rushing Attempts':rushing_attempts,
                                'Rushing Yards':rushing_yards,
                                'Rushing Touchdowns':rushing_touchdowns,
                                'Flags':flags,
                                'Games played':games_played,
                                'Fantasy Points':fantasy_points,
                                'Fantasy Points per Week':fantasy_points_per_week,
                                'Rostered Percentage':rostered_percentage}, ignore_index=True)
        df['Player']= df['Player'].str.replace(')','')
        df['Player']=df['Player'].str.split(' \(',1,expand=True)[0]
        df['Player'] = df['Player'].str.replace('[^\w\s]','')
        df['Player'] = df['Player'].str.replace('III','')
        df['Player'] = df['Player'].str.replace('II','')
        df['Player'] = df['Player'].str.replace('IV','')
        df.to_csv(input('Type file name here:')+'.csv',index=False)
        print("File saved in folder")
    elif position =='TE':
        df = pd.DataFrame(columns=['Year',
                                    'Week',
                                    'Position',
                                    'Rank',
                                    'Player',
                                    'Receptions',
                                    'Targets',
                                    'Receiving Yards',
                                    'Yards per Reception',
                                    'Longest Reception',
                                    'Catches >20 Yards',
                                    'Receiving Touchdowns',
                                    'Rushing Attempts',
                                    'Rushing Yards',
                                    'Rushing Touchdowns',
                                    'Flags',
                                    'Games played',
                                    'Fantasy Points',
                                    'Fantasy Points per Week',
                                    'Rostered Percentage'])
    # Downloading contents of the web page
        url = "https://www.fantasypros.com/nfl/stats/te.php?year={yearinput}&week={weekinput}&scoring=PPR&roster=e&range=week".format(yearinput=str(yearinput),weekinput=str(weekinput))
        data = requests.get(url).text
        # Creating BeautifulSoup object
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find(class_='mobile-table double-header')
        # Collecting Ddata
        for row in table.tbody.find_all('tr'):
            # Find all data for each column
            columns = row.find_all('td')
            if(columns != []):
                rank = columns[0].text.strip()
                player = columns[1].text.strip()
                receptions = columns[2].text.strip()
                targets = columns[3].text.strip()
                receiving_yards = columns[4].text.strip()
                yards_per_reception = columns[5].text.strip()
                longest_catch= columns[6].text.strip()
                catches_over_20 = columns[7].text.strip()
                receiving_touchdowns = columns[8].text.strip()
                rushing_attempts = columns[9].text.strip()
                rushing_yards = columns[10].text.strip()
                rushing_touchdowns = columns[11].text.strip()
                flags = columns[12].text.strip()
                games_played = columns[13].text.strip()
                fantasy_points = columns[14].text.strip()
                fantasy_points_per_week = columns[15].text.strip()
                rostered_percentage = columns[16].text.strip()
                df = df.append({'Year':yearinput,
                                'Week':weekinput,
                                'Position':'TE',
                                'Rank':rank,
                                'Player':player,
                                'Receptions':receptions,
                                'Targets':targets,
                                'Receiving Yards':receiving_yards,
                                'Yards per Reception':yards_per_reception,
                                'Longest Catch':longest_catch,
                                'Catches > 20 Yards':catches_over_20,
                                'Receiving Touchdowns':receiving_touchdowns,
                                'Rushing Attempts':rushing_attempts,
                                'Rushing Yards':rushing_yards,
                                'Rushing Touchdowns':rushing_touchdowns,
                                'Flags':flags,"Games played":games_played,
                                'Fantasy Points':fantasy_points,
                                'Fantasy Points per Week':fantasy_points_per_week,
                                'Rostered Percentage':rostered_percentage}, ignore_index=True)
        df['Player']= df['Player'].str.replace(')','')
        df['Player']=df['Player'].str.split(' \(',1,expand=True)[0]
        df['Player'] = df['Player'].str.replace('[^\w\s]','')
        df['Player'] = df['Player'].str.replace('III','')
        df['Player'] = df['Player'].str.replace('II','')
        df['Player'] = df['Player'].str.replace('IV','')
        df.to_csv(input('Type file name here:')+'.csv',index=False)
        print("File saved in folder")
    elif position =='K':
        df = pd.DataFrame(columns=['Year',
                                    'Week',
                                    'Position',
                                    'Rank',
                                    'Player',
                                    'Field Goals',
                                    'Field Goal Attempts',
                                    'Percentage',
                                    'Longest Kick',
                                    'Kicks below 20',
                                    'Kicks from 20-29',
                                    'Kicks from 30-39',
                                    'Kicks from 40-49',
                                    '50+',
                                    'Extra Points Made',
                                    'Extra Point Attempts',
                                    'Games played',
                                    'Fantasy Points',
                                    'Fantasy Points per Week',
                                    'Rostered Percentage'])
    # Downloading contents of the web page
        url = "https://www.fantasypros.com/nfl/stats/k.php?year={yearinput}&week={weekinput}&scoring=PPR&roster=e&range=week".format(yearinput=str(yearinput),weekinput=str(weekinput))
        data = requests.get(url).text
        # Creating BeautifulSoup object
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find(class_='mobile-table')
        # Collecting Ddata
        for row in table.tbody.find_all('tr'):
            # Find all data for each column
            columns = row.find_all('td')
            if(columns != []):
                rank = columns[0].text.strip()
                player = columns[1].text.strip()
                field_goals = columns[2].text.strip()
                field_goal_attempts = columns[3].text.strip()
                percentage = columns[4].text.strip()
                longest_kick = columns[5].text.strip()
                kicks_below_20 = columns[6].text.strip()
                kicks_20_29 = columns[7].text.strip()
                kicks_30_39 = columns[8].text.strip()
                kicks_40_49 = columns[9].text.strip()
                _50plus = columns[10].text.strip()
                Extra_points_made = columns[11].text.strip()
                extra_points_attempted = columns[12].text.strip()
                games_played = columns[13].text.strip()
                fantasy_points = columns[14].text.strip()
                fantasy_points_per_week = columns[15].text.strip()
                rostered_percentage = columns[16].text.strip()
                df = df.append({'Year':yearinput,
                                'Week':weekinput,
                                'Position':'K',
                                'Rank':rank,
                                'Player':player,
                                'Field Goals':field_goals,
                                'Field Goal Attempts':field_goal_attempts,
                                'Percentage':percentage,
                                'Longest Kick':longest_kick,
                                'Kicks below 20':kicks_below_20,
                                'Kicks from 20-29':kicks_20_29,
                                'Kicks from 30-39':kicks_30_39,
                                'Kicks from 40-49':kicks_40_49,
                                '50+':_50plus,
                                'Extra Points Made':Extra_points_made,
                                'Extra Points Attempted':extra_points_attempted,
                                'Games played':games_played,
                                'Fantasy Points':fantasy_points,
                                'Fantasy Points per Week':fantasy_points_per_week,
                                'Rostered Percentage':rostered_percentage}, ignore_index=True)
        df['Player']= df['Player'].str.replace(')','')
        df['Player']=df['Player'].str.split(' \(',1,expand=True)[0]
        df['Player'] = df['Player'].str.replace('[^\w\s]','')
        df['Player'] = df['Player'].str.replace('III','')
        df['Player'] = df['Player'].str.replace('II','')
        df['Player'] = df['Player'].str.replace('IV','')
        df.to_csv(input('Type file name here:')+'.csv',index=False)
        print("File saved in folder")
    elif position =='DST':
        df = pd.DataFrame(columns=['Year',
                                    'Week',
                                    'Position',
                                    'Rank',
                                    'Player',
                                    'Sacks',
                                    'Interceptions',
                                    'Fumble Recoveries',
                                    'Forced Fumbles',
                                    'Defensive Touchdowns',
                                    'Safeties',
                                    'Special Teams Touchdowns',
                                    'Games played',
                                    'Fantasy Points',
                                    'Fantasy Points per Week',
                                    'Rostered Percentage'])
    # Downloading contents of the web page
        url = "https://www.fantasypros.com/nfl/stats/dst.php?year={yearinput}&week={weekinput}&scoring=PPR&roster=e&range=week".format(yearinput=str(yearinput),weekinput=str(weekinput))
        data = requests.get(url).text
        # Creating BeautifulSoup object
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find(class_='mobile-table')
        # Collecting Ddata
        for row in table.tbody.find_all('tr'):
            # Find all data for each column
            columns = row.find_all('td')
            if(columns != []):
                rank = columns[0].text.strip()
                player = columns[1].text.strip()
                sacks = columns[2].text.strip()
                interceptions = columns[3].text.strip()
                fumble_recoveries = columns[4].text.strip()
                forced_fumbles = columns[5].text.strip()
                defensive_touchdowns = columns[6].text.strip()
                safeties = columns[7].text.strip()
                special_teams_touchdowns = columns[8].text.strip()
                games_played = columns[9].text.strip()
                fantasy_points = columns[10].text.strip()
                fantasy_points_per_week = columns[11].text.strip()
                rostered_percentage = columns[12].text.strip()
                df = df.append({'Year':yearinput,
                                'Week':weekinput,
                                'Position':'DST',
                                'Rank':rank,
                                'Player':player,
                                'Sacks':sacks,
                                'Interceptions':interceptions,
                                'Fumble Recoveries':fumble_recoveries,
                                'Forced Fumbles':forced_fumbles,
                                'Defensive Touchdowns':defensive_touchdowns,
                                'Safeties':safeties,
                                'Special Teams Touchdowns':special_teams_touchdowns,
                                'Games played':games_played,
                                'Fantasy Points':fantasy_points,
                                'Fantasy Points per Week':fantasy_points_per_week,
                                'Rostered Percentage':rostered_percentage}, ignore_index=True)
        df['Player']= df['Player'].str.replace(')','')
        df['Player']=df['Player'].str.split(' \(',1,expand=True)[0]
        df['Player'] = df['Player'].str.replace('[^\w\s]','')
        df['Player'] = df['Player'].str.replace('III','')
        df['Player'] = df['Player'].str.replace('II','')
        df['Player'] = df['Player'].str.replace('IV','')
        df.to_csv(input('Type file name here:')+'.csv',index=False)
        print("File saved in folder")
    else:
        print('Incorrect position input')

def teamnamepull(yearinput, weekinput):
    #yearinput = input('What year would you like to pull data for:')
    #weekinput = input('What week would you like to pull data for:')
    df = pd.DataFrame(columns=['Year','Week','Player','Position', 'Team'])
    url = "https://github.com/fantasydatapros/data/blob/master/weekly/{year}/week{week}.csv".format(year=str(yearinput),week=str(weekinput))
    data = requests.get(url).text
    # Creating BeautifulSoup object
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find("table", {"class": "js-csv-data csv-data js-file-line-container"})
    # Collecting Ddata
    for row in table.tbody.find_all('tr'):
        # Find all data for each column
        columns = row.find_all('td')
        if(columns != []):
            player = columns[1].text.strip()
            position = columns[2].text.strip()
            team = columns[3].text.strip()
            df = df.append({'Year':yearinput,
                            'Week':weekinput,
                            'Player':player,
                            'Position':position,
                            'Team':team}, ignore_index=True)
    df['Team']=df['Team'].str.replace('OTI','TEN')
    df['Team']=df['Team'].str.replace('KAN','KC')
    df['Team']=df['Team'].str.replace('HTX','HOU')
    df['Team']=df['Team'].str.replace('RAI','LV')
    df['Team']=df['Team'].str.replace('CLT','IND')
    df['Team']=df['Team'].str.replace('GNB','GB')
    df['Team']=df['Team'].str.replace('NWE','NE')
    df['Team']=df['Team'].str.replace('RAV','BAL')
    df['Team']=df['Team'].str.replace('SDG','LAC')
    df['Team']=df['Team'].str.replace('NOR','NO')
    df['Team']=df['Team'].str.replace('TAM','TB')
    df['Team']=df['Team'].str.replace('SFO','SF')
    df['Team']=df['Team'].str.replace('CRD','ARI')
    df['Team']=df['Team'].str.replace('RAM','LAR')
    df.to_csv(input('Type file name here:')+'.csv',index=False)
    print("File saved in folder")

def combine():
    print('Be sure you are combining files from the same position')
    df = pd.concat(map(pd.read_csv,[input('Type file name here:')+'.csv', input('Type file name here:')+'.csv']), ignore_index=True)
    df.to_csv(input('Type file name here:')+'.csv',index=False)
    print("File saved in folder")

def teamcorrection(file1,file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df3 = pd.merge(df1, df2, on=['Year', 'Week','Player'], how='left')
    df3.to_csv(input('Type corrected teamname file here')+'.csv',index=False)
    print("File saved in folder")
