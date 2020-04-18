from time import strftime
from time import gmtime
from functions import *

print("welcome in our calculator, it's good choice to run galloway")
print ("now we can calculate, how much long you will run, if you run galloway."+"\n"+"\n"+"Set your normal pace first")

#check pace
minutes=int(input("set minutes "))
seconds=int(input("seconds "))
pace_run=pace(minutes,seconds)

print ("your pace is "+str(minutes)+":"+str(seconds))

#check distance
distance=int(input("what is your distance in km? : "))

#calculate time in normal
time_normal=run_time(distance,pace_run)

print ("your time for "+str(distance)+" km "+" is "+str(time_normal))

print("\n"+"So, now we calculate Galloway time")
print("In Galloway running you run, walk and run. You have to enter your walk pace, and how many minutes you walk how many minutes you run.")


#check interwals
minutes_galloway_run=int(input("set minutes you will run "))
minutes_galloway_walk=int(input("set minutes you will walk "))
sum_of_intervals=minutes_galloway_walk+minutes_galloway_run

#walk pace
print ("\n"+"Now tell us what is your walk pace?")
walk_pace_minutes=int(input("set minutes "))
walk_pace_seconds=int(input("seconds "))
pace_walk=pace(walk_pace_minutes,walk_pace_seconds)

#galloway_pace
galloway_pace=galloway_pace(minutes_galloway_run,minutes_galloway_walk,pace_run,pace_walk,sum_of_intervals)

#calculate time
time_galloway=run_time(distance,galloway_pace)
print("So your normal time is: "+time_normal+" And By Galloway your time is "+str(time_galloway))
time_difference=compare(time_normal,time_galloway)
print("So the diffrence is: ",time_difference," You run slower but healthier :)")