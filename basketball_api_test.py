import requests
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import re

#from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats
#, get_game_logs, get_player_headshot
#from basketball_reference_scraper.seasons import get_schedule, get_standings
#from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.pbp import get_pbp
from basketball_reference_scraper.shot_charts import get_shot_chart
#from basketball_reference_scraper.injury_report import get_injury_report
#from basketball_reference_scraper.drafts import get_draft_class


date = '2022-04-10'
home = 'HOU'
away = 'ATL'
d = get_shot_chart(date, home, away)
homesize = len(d[home])
awaysize = len(d[away])



class Shot():
    x = 0
    y = 0
    quarter = 0
    timeleft = 0
    player = ""
    make_miss = ""
    value = 0
    distance = 0
    team = ""
    def __init__(self, _x,_y,qtr,time,_player,made,val,dist,_team):
        self.x = _x
        self.y = _y
        self.quarter = qtr
        self.timeleft = time
        self.player = _player
        self.make_miss = made
        self.value = val
        self.distance = dist
        self.team = _team

    def setX(self, int):
        self.x = int

    def getX(self):
        return self.x

    def setY(self, int):
        self.y = int

    def getY(self):
        return self.y

    def getQuarter(self):
        return self.quarter

    def getTime(self):
        return self.timeleft

    def getPlayer(self):
        return self.player

    def getMake(self):
        return self.make_miss

    def getValue(self):
        return self.value

    def getDistance(self):
        return self.distance

    def getTeam(self):
        return self.team


def doesitwork():

    x_arrA = [0.0 for i in range(len(d[away]))]
    y_arrA = [0.0 for i in range(len(d[away]))]
    shotArr = [0.0 for i in range(len(d[away]) + len(d[home]))]

    for i in range(awaysize):
        x = d[away].iloc[i].get('x')
        y = d[away].iloc[i].get('y')
        x = x[0:4:1]
        x = float(x)
        y = y[0:4:1]
        y = float(y)
        quarter = d[away].iloc[i].get('QUARTER')
        tr = d[away].iloc[i].get('TIME_REMAINING')
        plr = d[away].iloc[i].get('PLAYER')
        made = d[away].iloc[i].get('MAKE_MISS')
        val = d[away].iloc[i].get('VALUE')
        dist = d[away].iloc[i].get('DISTANCE')
        dist = dist[0:2:1]
        team = away
        s = Shot(x,y,quarter,tr,plr,made,val,dist,team)
        shotArr[i] = s

    for i in range(homesize):
        x = d[home].iloc[i].get('x')
        y = d[home].iloc[i].get('y')
        x = x[0:4:1]
        x = float(x)
        y = y[0:4:1]
        y = float(y)
        quarter = d[home].iloc[i].get('QUARTER')
        tr = d[home].iloc[i].get('TIME_REMAINING')
        plr = d[home].iloc[i].get('PLAYER')
        made = d[home].iloc[i].get('MAKE_MISS')
        val = d[home].iloc[i].get('VALUE')
        dist = d[home].iloc[i].get('DISTANCE')
        dist = float(dist[0:2:1])
        team = home
        s = Shot(x,y,quarter,tr,plr,made,val,dist,team)
        shotArr[i + awaysize] = s

    shotArr.sort(reverse = True, key = sortFunc)
    plotpoint(shotArr)

def sortFunc(shot):
    return shot.getTime()

# Function to draw basketball court
def create_court(ax, color):
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))

    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))

    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))

    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-275, 275)
    ax.set_ylim(0, 470)

    # General plot parameters
    mpl.rcParams['font.family'] = 'Avenir'
    mpl.rcParams['font.size'] = 18
    mpl.rcParams['axes.linewidth'] = 2

def plotpoint(shotArr):
    x_arr = [0.0 for i in range(awaysize + homesize)]
    y_arr = [0.0 for i in range(awaysize + homesize)]
    for i in range(len(shotArr)):
        x_arr[i] = shotArr[i].getX()
        y_arr[i] = shotArr[i].getY()

    # Draw basketball court
    fig = plt.figure(figsize=(4, 3.76))
    ax = fig.add_axes([0, 0, 1, 1])
    ax = create_court(ax, 'black')

    with cbook.get_sample_data('toycen.jpg') as image_file:
        image = plt.imread(image_file)

    plt.imshow(image, origin='upper', extent=(-275, 275, 0, 470))

    #x_num = np.array(x_arr)
    #y_num = np.array(y_arr)
    #plt.hexbin(x_num * 10 - 275, y_num * 10 + 60, gridsize=(15, 15), extent=(-275, 275, 0, 470), bins='log', cmap='Blues')

    makes = 0
    shots = 0
    TPmakes = 0
    TPshots = 0
    longest = 0
    indexLong = 0
    team = ''
    homepoints = 0
    awaypoints = 0

    for i in range(len(shotArr)):
        if int(shotArr[i].getDistance()) > int(longest):
            if shotArr[i].getMake() == 'MAKE':
                longest = shotArr[i].getDistance()
                indexLong = i

    for i in range(len(shotArr)):
        plt.pause(0.1)
        if i == indexLong:
            #image = plt.imread(get_player_headshot(shotArr[i].getPlayer()))
            #plt.imshow(image, origin='upper', extent=((x_arr[i] * 10 - 265), (x_arr[i] * 10 - 285), (y_arr[i] * 10 + 50), (y_arr[i] * 10 + 70)))
            plt.plot((x_arr[i] * 10 - 275), y_arr[i] * 10 + 60, 'y*--', linewidth=2, markersize=15, mec='black')
        if shotArr[i].getMake() == 'MAKE':
            if i != indexLong:
                if shotArr[i].getTeam() == home:
                    plt.plot((x_arr[i] * 10 - 275), y_arr[i] * 10 + 60, 'bo--', linewidth=2, markersize=12, mec='black')
                else:
                    plt.plot((x_arr[i] * 10 - 275), y_arr[i] * 10 + 60, 'ro--', linewidth=2, markersize=12, mec='black')
            shots += 1
            makes += 1
            if shotArr[i].getValue() == 3:
                if int(shotArr[i].getDistance()) > 27:
                    print(shotArr[i].getPlayer() + " makes a DEEEEEP " + str(shotArr[i].getValue()) + "!")
                else:
                    print(shotArr[i].getPlayer() + " makes a " + str(shotArr[i].getValue()) + "!")
            elif int(shotArr[i].getDistance()) > 5:
                print(shotArr[i].getPlayer() + " makes a midrange " + str(shotArr[i].getValue()) + "!")
            else:
                print(shotArr[i].getPlayer() + " makes a layup " + str(shotArr[i].getValue()) + "!")

            if shotArr[i].getValue() == 3:
                TPshots += 1
                TPmakes += 1
                if shotArr[i].getTeam() == home:
                    homepoints += 3
                else:
                    awaypoints += 3
            else:
                if shotArr[i].getTeam() == home:
                    homepoints += 2
                else:
                    awaypoints += 2
        else:
            if shotArr[i].getTeam() == home:
                plt.plot((x_arr[i] * 10 - 275), y_arr[i] * 10 + 60, 'bx--', linewidth=2, markersize=12)
            else:
                plt.plot((x_arr[i] * 10 - 275), y_arr[i] * 10 + 60, 'rx--', linewidth=2, markersize=12)
            shots += 1
            if shotArr[i].getValue() == 3:
                print(shotArr[i].getPlayer() + " misses a " + str(shotArr[i].getValue()) + "...")
                TPshots += 1
            elif int(shotArr[i].getDistance()) > 5:
                print(shotArr[i].getPlayer() + " misses a midrange " + str(shotArr[i].getValue()) + "...")
            else:
                print(shotArr[i].getPlayer() + " misses a layup " + str(shotArr[i].getValue()) + "...")



    fgm = int((makes/shots) * 100)
    TPfgm = int((TPmakes/TPshots) * 100)
    print(str(fgm) + " FG%")
    print(str(TPfgm) + " 3PT%")
    print("Home: " + str(homepoints) + "\nAway: " + str(awaypoints))
    plt.show()

if __name__ == "__main__":
    doesitwork()

