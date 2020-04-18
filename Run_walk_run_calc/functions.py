from time import strftime
from time import gmtime
from datetime import datetime

def pace(minutes,seconds):
    return minutes*60+seconds

def run_time(distance,pace):
    return strftime("%H:%M:%S", gmtime(distance*pace))

def galloway_pace(minutes_galloway_run,minutes_galloway_walk,pace,pace_walk,intervals):
    return (pace*minutes_galloway_run+pace_walk*minutes_galloway_walk)/intervals

def compare(time1,time2):
    FMT = '%H:%M:%S'
    return datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
