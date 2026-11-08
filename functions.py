import data as d
from i_o import get_number,get_str

# שאלה_1
def get_id_and_name():
    id = get_number("what is teams id ?")
    name = get_str("what is teams name ?")
    return id ,name

def check(id, name):    
    for item in d.teams:
        if item["id"] == id:
            print("the id is alredy exists !!!")
            return False
    for item in d.teams:
        if item["name"] == name:
            print("the name is alredy exists !!!")
            return False
    return True
def create_team():
    id , name = get_id_and_name
    return {"id": id ,"name": name}
def Add_team(teams: list):
    id, name = get_id_and_name()
    while not check(id,name):
        id, name = get_id_and_name()
    d.teams.append(create_team())
    print("adding successfully")

# שאלה2
def Show_all_teams():
    for item in d.teams:
        print(item["name"])

# שאלה_3
def get_id():    
    home_team_id = input("what is id of teams home ?")
    away_team_id = input("what is id of teams away ?")
    home_goals = input("How many goals were scored for the teams home ?")
    away_goals = input("How many goals were scored for the teams away ?")
    return home_team_id,away_team_id ,home_goals,away_goals

def cheking_id_home():
    home_team_id,away_team_id ,home_goals,away_goals = get_id()
    for item in d.teams:
        if item["id"] == home_team_id and home_team_id != away_team_id:
            return True
    return False


def cheking_id_away():
    home_team_id,away_team_id ,home_goals,away_goals = get_id()
    for item in d.teams:
        if item["id"] == away_team_id:
            return True
    return False

def cheking_gols():
    home_team_id,away_team_id ,home_goals,away_goals = get_id()
    if home_goals.isdigit() and away_goals.isdigit():
        return True
    return False

def cheking_duble():
    home_team_id,away_team_id ,home_goals,away_goals = get_id()
    for item in d.matches:
        if home_team_id == item["home_team_id"] and away_team_id == item["away_team_id"] or home_team_id == item["away_team_id"] and away_team_id == item["home_team_id"]:
            return False
    return True 
def creat_match():
    home_team_id,away_team_id ,home_goals,away_goals = get_id()
    return {"home_team_id": home_team_id , "away_team_id": away_team_id, "home_goals": home_goals, "away_goals": away_goals}

def Add_match_result():
    home_team_id,away_team_id ,home_goals,away_goals = get_id()
    function = [cheking_gols(),cheking_id_away(),cheking_id_home(),cheking_duble()]
    while all(function):
        home_team_id,away_team_id ,home_goals,away_goals = get_id()
    d.matches.append(creat_match())
    print("adding successfully")

# שאלה_4
    
def 
    
    
        

    
