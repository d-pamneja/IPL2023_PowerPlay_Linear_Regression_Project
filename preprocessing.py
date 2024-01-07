import pandas as pd

data_ball = pd.read_csv('data/IPL_Ball_by_Ball_2008_2022.csv')
data_match = pd.read_csv('data/IPL_Matches_2008_2022.csv')

def drop_redundant_fea_bowl(data):
  #Storing all the redundant features in a List
  L = ['extra_type', 'batsman_run', 'extras_run','non_boundary', 'isWicketDelivery', 'player_out', 'kind',
        'fielders_involved','ballnumber','non-striker']
  #Using drop feature to remove them from our data
  data = data.drop(L,axis = 1)
  return data

data_ball = drop_redundant_fea_bowl(data_ball)

def powerplay_cap(data):
  #Selecting all overs from 0-6 (since indexing begins at 0, we select <= 5)
  data = data[data_ball['overs']<= 5]
  return data

data_ball = powerplay_cap(data_ball)

def merge_strings_data(data):
  #We use agg() function to aggregate the column values based on grouping by 'ID' and 'innings'
  #Using ',' is a way by which we are cumilating these values with the de limiter of a ,
  #Now we use join(set(_)) to join these values by removing duplicates in the way
  #Also, since 'total_run' is a numeric value, we can use 'sum' straight away to aggregate those values
  merged = data.groupby(['ID', 'innings']).agg({'batter': lambda g: ','.join(set(g)),'bowler': lambda g: ','.join(set(g)),'BattingTeam': lambda g: ','.join(set(g)),'total_run': 'sum'}).reset_index()
  return merged

merged = merge_strings_data(data_ball)

def merge_databases(data1,data2):
  #We use merge function to merge both the dataframes on the common column i.e. 'ID'
  data = pd.merge(data1,data2, on = ['ID'])
  return data

data = merge_databases(merged,data_match)

def drop_redundant_fea_match(data):
  #We store those redundant columns in a List and drop those from our dataframe
  L = ['WinningTeam', 'WonBy', 'Margin', 'method',
       'Player_of_Match','TossWinner', 'TossDecision',
       'SuperOver', 'WinningTeam', 'WonBy', 'Margin', 'method',
       'Player_of_Match','Umpire1',
       'Umpire2','City','Date','Season','MatchNumber','Team1Players','Team2Players']
  data = data.drop(L,axis = 1)
  return data

data = drop_redundant_fea_match(data)

def bowling_team_creation(data):
  if data['BattingTeam'] == data["Team1"]:
      return data["Team2"]
  if data["BattingTeam"] == data["Team2"]:
      return data["Team1"]

def bowl_team(data):
  #We use apply function and the function created above to add bowling team in our data set
  data['BowlingTeam'] = data.apply(bowling_team_creation,axis = 1)
  return data

data = bowl_team(data)

#Now, we can drop Team1 and Team2 from our data, as their work is now done
data = data.drop(['Team1','Team2'],axis = 1)

def rename_reindex(data):
  #We will rename certain columns and reindex them as per our requirements
  data = data.rename(columns={'Venue': 'venue', 'batter': 'batsmen', 'bowler': 'bowlers','BattingTeam':'batting_team','BowlingTeam':'bowling_team'})
  data = data.reindex(columns=['venue', 'innings', 'batting_team', 'bowling_team','batsmen','bowlers','total_run'])
  return data

data = rename_reindex(data)

#We can store our final data in the variable x
x = data

def stadium_cleaning(x):
  #We use replace function to change all same stadiums to a common name
  x['venue'] = x['venue'].replace(['Punjab Cricket Association Stadium, Mohali','Punjab Cricket Association IS Bindra Stadium'],'Punjab Cricket Association Stadium')
  x['venue'] = x['venue'].replace(['Feroz Shah Kotla','Arun Jaitley Stadium, Delhi','Arun Jaitley Stadium'],'Arun Jaitley Stadium')
  x['venue'] = x['venue'].replace(['M.Chinnaswamy Stadium','M Chinnaswamy Stadium'],'M.Chinnaswamy Stadium')
  x['venue'] = x['venue'].replace(['Eden Gardens','Eden Gardens, Kolkata'],'Eden Gardens')
  x['venue'] = x['venue'].replace(['Maharashtra Cricket Association Stadium','Maharashtra Cricket Association Stadium, Pune'],'Maharashtra Cricket Association Stadium')
  x['venue'] = x['venue'].replace(['Dr DY Patil Sports Academy','Dr DY Patil Sports Academy, Mumbai'],'Dr DY Patil Sports Academy')
  x['venue'] = x['venue'].replace(['MA Chidambaram Stadium, Chepauk','MA Chidambaram Stadium, Chepauk, Chennai'],'MA Chidambaram Stadium')
  x['venue'] = x['venue'].replace(['Sheikh Zayed Stadium','Zayed Cricket Stadium, Abu Dhabi'],'Zayed Cricket Stadium')
  x['venue'] = x['venue'].replace(['Wankhede Stadium','Wankhede Stadium, Mumbai'],'Wankhede Stadium')
  x['venue'] = x['venue'].replace(['Rajiv Gandhi International Stadium, Uppal','Rajiv Gandhi International Stadium'],'Rajiv Gandhi International Stadium')
  x['venue'] = x['venue'].replace(['Narendra Modi Stadium, Ahmedabad','Sardar Patel Stadium, Motera'],'Narendra Modi Stadium')
  x['venue'] = x['venue'].replace(['Brabourne Stadium, Mumbai'],'Brabourne Stadium')


  return x

x = stadium_cleaning(x)

def teams_cleaning(x):
  x['batting_team'] = x['batting_team'].replace(['Pune Warriors','Rising Pune Supergiants','Rising Pune Supergiant'],'Rising Pune Supergiants')
  x['bowling_team'] = x['bowling_team'].replace(['Pune Warriors','Rising Pune Supergiants','Rising Pune Supergiant'],'Rising Pune Supergiants')
  x['batting_team'] = x['batting_team'].replace(['Gujarat Lions','Gujarat Titans'],'Gujarat Titans')
  x['bowling_team'] = x['bowling_team'].replace(['Gujarat Lions','Gujarat Titans'],'Gujarat Titans')
  x['batting_team'] = x['batting_team'].replace(['Delhi Daredevils','Delhi Capitals'],'Delhi Capitals')
  x['bowling_team'] = x['bowling_team'].replace(['Delhi Daredevils','Delhi Capitals'],'Delhi Capitals')
  x['batting_team'] = x['batting_team'].replace(['Deccan Chargers','Sunrisers Hyderabad'],'Sunrisers Hyderabad')
  x['bowling_team'] = x['bowling_team'].replace(['Deccan Chargers','Sunrisers Hyderabad'],'Sunrisers Hyderabad')
  x['batting_team'] = x['batting_team'].replace(['Kings XI Punjab','Punjab Kings'],'Punjab Kings')
  x['bowling_team'] = x['bowling_team'].replace(['Kings XI Punjab','Punjab Kings'],'Punjab Kings')

  return x

x = teams_cleaning(x)

def present_teams_wise(x):
  teams = ['Kolkata Knight Riders', 'Royal Challengers Bangalore',
       'Chennai Super Kings', 'Punjab Kings', 'Rajasthan Royals',
       'Delhi Capitals', 'Mumbai Indians', 'Sunrisers Hyderabad',
       'Gujarat Titans', 'Lucknow Super Giants']
  #We use isin() function to cull out those entries which are required
  x = x[x['batting_team'].isin(teams)]
  x = x[x['bowling_team'].isin(teams)]

  return x

x = present_teams_wise(x)

def hashing(x):
  import hashlib
  for col in ['venue', 'batting_team', 'bowling_team', 'batsmen','bowlers']:
    hashed_col = x[col].apply(lambda i: hash(i)) #Here, we use lambda to create a numeric hash value for each entry in all categorical values and replace the string value with it's numeric counterpart
    x[col] = hashed_col
  return x

x = hashing(x)

X = x.drop('total_run',axis = 1)
y = x['total_run']




