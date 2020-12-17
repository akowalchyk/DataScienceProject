import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def play_duration_milliseconds_to_hours(df):
    df = df.rename(columns = {"Play Duration Milliseconds":"Play Duration Hours"}) 
    ser = df["Play Duration Hours"].copy()
    new_ser = []
    for i in range(0, len(ser)):
        new_ser.append((ser[i]/(1000*60*60)) % 24)
    df["Play Duration Hours"] = new_ser  

def reason_for_end_cleaning(df):
    ser = df["End Reason Type"].copy()
    for i in range(0, len(ser)):
        curr = ser[i]
        if (curr == "TRACK_SKIPPED_FORWARDS" or curr == "TRACK_SKIPPED_BACKWARDS" or 
        curr == "MANUALLY_SELECTED_PLAYBACK_OF_A_DIFF_ITEM"):
            ser[i] = "Skipped"
        elif (curr == "NATURAL_END_OF_TRACK" or curr == "SCRUB_END"):
            ser[i] = "NATURAL_END_OF_TRACK"
        elif (curr == "PLAYBACK_MANUALLY_PAUSED"):
            ser[i] = "Paused"
        else:
            ser[i] = "Scrubbed to Beginning"
    df["End Reason Type"] = ser

def add_month_attribute(df):
    month = []
    dates_array = df["Event Start Timestamp"]
    for dates in dates_array:
        if (dates[0:7]== "2019-10"):
            month.append("Oct/2019")
        if (dates[0:7] == "2019-11"):
            month.append("Nov/2019")
        if (dates[0:7] == "2019-12"):
            month.append("Dec/2019")
        if (dates[0:7] == "2020-01"):
            month.append("Jan/2020")
        if (dates[0:7] == "2020-02"):
            month.append("Feb/2020")
        if (dates[0:7] == "2020-03"):
            month.append("Mar/2020")
        if (dates[0:7] == "2020-04"):
            month.append("Apr/2020")
        if (dates[0:7] == "2020-05"):
            month.append("May/2020")
        if (dates[0:7] == "2020-06"):
            month.append("June/2020")
        if (dates[0:7] == "2020-07"):
            month.append("July/2020")
        if (dates[0:7] == "2020-08"):
            month.append("Aug/2020")
        if (dates[0:7] == "2020-09"):
            month.append("Sept/2020")
        if (dates[0:7] == "2020-10"):
            month.append("Oct/2020")
    df["month"] = month

def Song_Counts_by_device(x,y):
    plt.figure()
    plt.bar(x, y)
    plt.title("Total # of Songs listened to from Oct, 2019 - Oct, 2020")
    plt.ylabel("# of songs")
    plt.xlabel("Name of Device")
    plt.show()

def Total_Time_by_device(x,y):
    plt.figure()
    plt.bar(x, y)
    plt.title("Total time listening to music from Oct, 2019 - Oct, 2020")
    plt.ylabel("time in hours")
    plt.xlabel("Name of Device")
    plt.show()

def Change_By__Number_Of_Songs(x,y1,y2,y3):
    plt.figure()
    np.arange(len(x)) 
    plt.bar(x, y1,label="Adams Iphone", color="red") 
    plt.bar(x, y2,label="Annas Iphone", color="Purple")
    plt.bar(x, y3,label="Moms Iphone", color="Green")
   # plt.plot(x, y4, label="Amazon Alexa", color="Black") 
    plt.title("Change in total music played by # of Songs Played")
    plt.xlabel("X Values")
    plt.xticks(x, rotation='30')
    plt.ylabel("Y Values")
    plt.legend()
    plt.show()

def Change_By_Total_Time(x,y,name):
    plt.figure()
    plt.bar(x, y,.5, label=name, color="Black")
    plt.title("Change in total music played by Total Time")
    plt.xticks(x, rotation='30')
    plt.ylabel("Total Hours")
    plt.legend()
    plt.show()

def Genres_by_Device(x,y1,y2,y3,y4):
    plt.figure()
    ind = np.arange(len(x))
    width = .2
    plt.bar(ind, y1, width,  label="Adams Iphone", color="red") 
    plt.bar(ind + width, y2, width, label="Annas Iphone", color="Purple")
    plt.bar(ind - width, y3, width, label="Moms Iphone", color="Green")
    plt.bar(ind -(width*2), y4, width, label="Amazon Alexa", color="Blue") 

    plt.title("Genres Played by Device")
    plt.xticks(ind + width / len(x),x, rotation='20')
    plt.ylabel("Play Duration Hours")
    plt.legend() 
    plt.show()
    
def reason_for_end(x, y1,y2,y3,y4):
    plt.figure() 
    plt.pie(y1, labels=x, autopct="%1.2f%%")
    plt.title("Adams Iphone")
    plt.show()

    plt.figure() 
    plt.pie(y2, labels=x, autopct="%1.2f%%")
    plt.title("Annas Iphone")
    plt.show()

    plt.figure()
    plt.pie(y3, labels=x, autopct="%1.2f%%")
    plt.title("Moms Iphone")
    plt.show()

    plt.figure()
    plt.pie(y4, labels=x, autopct="%1.2f%%")
    plt.title("Amazon Echo")
    plt.show()










