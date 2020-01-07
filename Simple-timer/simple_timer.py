import time

#ask to count up or count donw?
start=input("Would you like to count time up or count time down? [up/down] : ")
if start=="up":
    print("\n"+"So we will count up")
elif start == "down":
    print("\n"+"OK, we will count down")
else: print("wrong answer")

#counting time up
if start=="up":
    print("\n"+"What time to count to?")
    #hours=input("hours: ")
    minutes_up=int(input("minutes: "))
    seconds_up=int(input("seconds: "))

    Sec=0
    Min=0
#hours option can be added
    while minutes_up>Min or seconds_up>Sec:
        Sec+=1
        print(str(Min)+" min "+ str(Sec)+" sek")
        time.sleep(1)
        if Sec==59:
            Sec=0
            Min+=1
            print(str(Min)+" minutes")
            time.sleep(1)
 #       if Min==59:
 #           Min=0
 #           Hrs+=1
 #           print(str(Hrs)+" hours")""
    print("\n"+"Times up!")

# counting time down

if start=="down":
    print("\n"+"From what time we count down?")
    minutes_down=int(input("minutes: "))
    seconds_down=int(input("seconds: "))

    while minutes_down > 0 or seconds_down > 0:
        seconds_down-=1
        print(str(minutes_down) + " min " + str(seconds_down) + " sek")
        time.sleep(1)
        if seconds_down==0 and minutes_down>0:
            minutes_down-=1
            seconds_down=60

    print("\n" + "Times up!")

input("\n"+"press Enter to exit :)")