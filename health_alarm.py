#Alarm for programmers

#This application plays alarm for water remainder, Study Remainder, Exercise remainder

#Requirnments: 3 audio files
#1) water.mp3
#2) study.mp3
#3) physical.mp3


import time
import sys
from pygame import mixer


print("***************** Health Alarm *****************")

#Time inialization
water_time = time.time()
study_time = time.time()
exe_time = time.time()


while True:
    def getdate():
        import datetime
        return datetime.datetime.now()
    dates =str(getdate())
    
    

#Code for Water remainder 

    if(time.time() - water_time >= 30  * 60):
        mixer.init()
        mixer.music.load("water.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        wat= str(input("\nThis is Water reminder:\nTo stop the alarm Write: Drank  \nTo exit the code type: exit"))
        if(wat == "Drank"):
            mixer.music.stop()
            water_time=time.time()
            f1=open("ex7.txt", "a")
            f1.write(f"Drank water at: [ {dates} ] \n")
            f1.close()
        elif wat1 == "exit":
            sys.exit("You have clossed the application")



#Code for Study remainder 


    if( time.time() - study_time >= 45  * 60):
        mixer.init()
        mixer.music.load("study.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        wat1= str(input("\nThis is Study reminder:\nTo stop the alarm Write: Stdone \n o exit the code type:  exit "))
        if(wat1 == "Stdone"):
            mixer.music.stop()
            study_time = time.time()
            f1=open("ex7.txt", "a")
            f1.write(f"Eye exercise at: [ {dates} ] \n")
            f1.close()
        elif wat1== "exit":
            sys.exit("You have clossed the application")

#Code for Exercise remainder 


    if(time.time() - exe_time >= 60 * 60):
        mixer.init()
        mixer.music.load("physical.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        wat2= str(input("\nThis is Exercise reminder:\nTo stop the alarm Write: exdone \n To exit the code type: exit"))
        if(wat2 == "exdone"):
            mixer.music.stop()
            exe_time = time.time()
            f1=open("ex7.txt", "a")
            f1.write(f"Done exercise at: [ {dates} ] \n")
            f1.close()
        elif wat1 == "exit":
            sys.exit("You have clossed the application")

