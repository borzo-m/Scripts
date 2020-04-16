print("welcome in our calculator, it's good choice to run galloway")
print ("now we can calculate, how much long you will run, if you run galloway. Set your normal pace first")



#check pace
minutes=int(input("set minutes "))
seconds=int(input("seconds "))
pace=minutes*60+seconds
print ("your pace is "+str(minutes)+":"+str(seconds))
#check distance
distance=int(input("what is your distance in km? : "))

#calculate time in normal
time_normal=(distance*pace)/60
print ("your time for "+str(distance)+" km "+" is "+str(time_normal)+" minutes.")

print("now we calculate Galloway time")
